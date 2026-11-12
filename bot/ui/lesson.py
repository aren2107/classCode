import re
import random
import time
from datetime import datetime, timedelta
from bot.timezone import manila_now, manila_timestamp, manila_today
from collections import defaultdict

import discord

from bot.database import db
from bot.learning.mastery import (
    _add_xp_in_transaction,
    _complete_lesson_in_transaction,
    _publish_xp_result,
    add_xp,
    award_badge,
    ensure_user_in_transaction,
    record_goal,
)
from bot.learning.cpp import CPP_CURRICULUM
from bot.learning.java import JAVA_CURRICULUM
from bot.learning.schema import validate_curriculum
from bot.learning.progress import get_status, sync_progress, get_review_recommendations


# -----------------------------
# Curriculum helpers
# -----------------------------

def curriculum_for(language: str):
    normalized = language.lower()
    if normalized in ("cpp", "c++"):
        return CPP_CURRICULUM
    if normalized == "java":
        return JAVA_CURRICULUM
    raise ValueError(f"Unsupported learning language: {language}")


# Fail fast at startup/import time if a lesson record is structurally broken.
validate_curriculum(CPP_CURRICULUM, "cpp")
validate_curriculum(JAVA_CURRICULUM, "java")


def code_language(language: str) -> str:
    return "cpp" if language.lower() in ("cpp", "c++") else "java"


def clean_code(code: str) -> str:
    return (
        code.replace("```cpp", "")
        .replace("```c++", "")
        .replace("```java", "")
        .replace("```", "")
        .strip()
    )


def topic_number(language: str, topic_id: str) -> tuple[int, int]:
    curriculum = curriculum_for(language)
    index = next((i for i, t in enumerate(curriculum) if t["id"] == topic_id), 0)
    return index + 1, len(curriculum)


# -----------------------------
# Teaching content
# -----------------------------

def line_explanation(line: str, language: str) -> str:
    s = line.strip()
    if not s:
        return ""
    if s.startswith("#include"):
        return "loads a C++ header that provides library features"
    if s.startswith("using namespace"):
        return "lets this C++ program use common names without repeatedly writing the namespace"
    if s.startswith("import "):
        return "imports a Java package or class so its features can be used"
    if s.startswith("public class") or s.startswith("class "):
        return "declares a class, which is a blueprint for objects"
    if re.search(r"\b(public static void main|main)\s*\(", s):
        return "defines the program's entry point"
    if s.startswith("if") or re.match(r"^else\b", s):
        return "chooses what code should run based on a condition"
    if s.startswith("switch") or s.startswith("case ") or s == "default:":
        return "selects one branch from several possible cases"
    if re.match(r"^(for|while|do)\b", s):
        return "repeats a block of code while the loop rules allow it"
    if "cout" in s or "System.out" in s:
        return "prints information to the console"
    if "cin" in s or "Scanner" in s:
        return "reads input from the user"
    if "return" in s:
        return "sends a value back to the caller of a function or method"
    if "new " in s:
        return "creates an object or dynamically created value"
    if "push_back" in s or ".add(" in s:
        return "adds an item to a collection"
    if "getline" in s:
        return "reads a complete line of text, including spaces"
    if "vector<" in s or "ArrayList" in s or "HashMap" in s:
        return "declares or uses a collection for multiple values"
    if "++" in s or "--" in s:
        return "changes a numeric value by one"
    if "=" in s and "==" not in s and ">=" not in s and "<=" not in s:
        return "assigns a value to a variable or field"
    if "(" in s and ")" in s and ("{" in s or ";" in s):
        return "calls or defines a function or method"
    if s in ("{", "}") or s.endswith("{") or s.startswith("}"):
        return "marks the beginning or end of a code block"
    return "performs part of the program's logic"


def breakdown(code: str, language: str) -> str:
    lines = []
    for number, raw in enumerate(clean_code(code).splitlines(), 1):
        if not raw.strip():
            continue
        text = raw.strip().replace("`", "")[:120]
        lines.append(f"**{number}.** `{text}`\n\u21b3 {line_explanation(raw, language)}")
        if len("\n\n".join(lines)) > 3200:
            lines.append("\u2026more lines are available in the example above.")
            break
    return "\n\n".join(lines) or "No example code was provided yet."


def lesson_objective(topic: dict, language: str) -> str:
    return "\n".join(f"• {item}" for item in topic["learning_objectives"])


def why_it_matters(topic: dict) -> str:
    return topic["introduction"]


def key_rules(topic: dict, language: str) -> list[str]:
    return topic.get("beginner_tips", [])[:4]


def practice_plan(topic: dict) -> str:
    return (
        "1. Read the requirement and identify the input/state.\n"
        "2. Predict the expected behavior before coding.\n"
        "3. Implement the smallest correct version.\n"
        "4. Test a normal case, a boundary case, and one invalid/empty case where relevant."
    )


def common_mistakes(topic: dict, language: str) -> list[str]:
    return topic.get("common_mistakes", [])[:3]


# -----------------------------
# Lesson-specific mastery checks
# -----------------------------
# Each lesson receives three questions. The first question is deliberately
# tied to the lesson concept; the other two reinforce code reading and the
# practical purpose of the concept. This keeps the checks useful without
# requiring an enormous separate quiz cog for every lesson.

QUESTION_OVERRIDES = {
    # C++ fundamentals
    "cpp_vars": [
        ("Which type is most appropriate for a whole-number age?", ["int", "double", "string", "bool"], 0, "An age such as 18 is a whole number, so int is a natural choice."),
        ("What does `int age = 18;` do?", ["Declares age and gives it 18", "Prints age", "Reads age", "Deletes age"], 0, "The declaration creates the variable and the initializer stores 18 in it."),
        ("Which name is clearest for a student's grade?", ["x", "a1", "studentGrade", "thing"], 2, "Descriptive names make code easier to read and maintain."),
    ],
    "cpp_io": [
        ("Which operator is used with `cin` to read a value?", [">>", "<<", "==", "&&"], 0, "`cin >> value` extracts input from the input stream."),
        ("Which statement prints a message?", ["cout << \"Hi\";", "cin >> \"Hi\";", "cout >> \"Hi\";", "print << \"Hi\";"], 0, "`cout` uses `<<` to send output to the console."),
        ("Why should a program decide its required input first?", ["So the program knows what data it must read", "To avoid using variables", "To remove all conditions", "To make loops infinite"], 0, "Knowing the input contract helps you design the rest of the solution correctly."),
    ],
    "cpp_operators": [
        ("What does `%` calculate for integers?", ["Remainder", "Power", "Average", "Percentage automatically"], 0, "Modulo gives the remainder after integer division."),
        ("Which operator checks equality?", ["=", "==", "!=", ">="], 1, "`==` compares two values; `=` assigns a value."),
        ("What is the value of `10 % 3`?", ["0", "1", "2", "3"], 1, "3 goes into 10 three times with a remainder of 1."),
    ],
    "cpp_conditionals": [
        ("Which construct is best for checking whether a mark is at least 75?", ["if", "for", "vector", "class"], 0, "A condition is the natural tool for choosing between pass and fail."),
        ("What does `else` represent?", ["The alternative when the earlier condition is false", "A loop", "A variable", "A function parameter"], 0, "`else` runs when its preceding condition did not match."),
        ("Why test boundary values such as 75?", ["Because the boundary determines which rule applies", "Because 75 is always invalid", "Because loops require it", "Because C++ only accepts 75"], 0, "Boundary values are where many condition mistakes appear."),
    ],
    "cpp_loops": [
        ("Which loop is convenient when the iteration count is known?", ["for", "class", "switch", "try"], 0, "A for loop keeps initialization, condition, and update together."),
        ("What can cause an infinite loop?", ["The loop condition never becomes false", "Using an int", "Printing output", "Using braces"], 0, "A loop needs a path toward its stopping condition."),
        ("How many times does `for(int i=0;i<3;i++)` run?", ["2", "3", "4", "0"], 1, "The values are 0, 1, and 2: three iterations."),
    ],
    "cpp_arrays": [
        ("What is the first index of a normal C++ array?", ["0", "1", "-1", "Depends on the compiler"], 0, "C++ arrays use zero-based indexing."),
        ("For `int a[5]`, what is the last valid index?", ["5", "4", "3", "6"], 1, "Five elements occupy indexes 0 through 4."),
        ("Why is checking the array size important?", ["To avoid accessing memory outside the valid range", "To make all values strings", "To remove loops", "To force sorting"], 0, "Out-of-range access can cause incorrect behavior or runtime problems."),
    ],
    "cpp_vectors": [
        ("What is a major advantage of `vector` over a raw fixed array?", ["It can grow and shrink", "It cannot store integers", "It never uses memory", "It replaces every loop"], 0, "A vector manages a resizable sequence for you."),
        ("Which operation adds an item to the end of a vector?", ["push_back", "add_end", "append_only", "insert_last_only"], 0, "`push_back` appends a value to the vector."),
        ("What should you test with a collection?", ["Empty and multiple-item cases", "Only one huge case", "Only invalid syntax", "Nothing"], 0, "Edge cases expose indexing and logic mistakes early."),
    ],
    "cpp_functions": [
        ("What is a function's return type?", ["The type of value it returns", "The number of loops", "The class name", "The user's input"], 0, "The return type tells C++ what kind of result the function produces."),
        ("Why use functions?", ["To organize reusable logic", "To make all code global", "To remove parameters", "To prevent testing"], 0, "Functions divide a program into focused, reusable pieces."),
        ("What should a small function usually have?", ["One clear responsibility", "Every feature in the program", "No inputs ever", "An infinite loop"], 0, "Focused functions are easier to understand and test."),
    ],
    "cpp_classes": [
        ("What is a class?", ["A blueprint for objects", "A loop", "A compiler error", "A file extension"], 0, "A class describes data and behavior that objects can have."),
        ("Why make a member private?", ["To control direct access to the object's state", "To make it global", "To prevent methods", "To disable constructors"], 0, "Private members support encapsulation."),
        ("What is an object?", ["An instance created from a class", "A header file", "A loop condition", "A return type"], 0, "The class is the blueprint; the object is an instance of that blueprint."),
    ],
    "cpp_oop": [
        ("Which OOP idea lets a derived class provide a different implementation?", ["Polymorphism", "Input", "Modulo", "Iteration"], 0, "Polymorphism lets code work through a common interface while behavior varies by object."),
        ("Why use a virtual function in C++ polymorphism?", ["To allow dynamic dispatch through a base interface", "To create a loop", "To read input", "To allocate an array only"], 0, "Virtual functions enable the derived override to be selected at runtime through a base reference or pointer."),
        ("Which is an OOP principle?", ["Encapsulation", "Modulo", "Tokenization", "Compilation only"], 0, "Encapsulation is one of the core object-oriented ideas."),
    ],
    "cpp_files": [
        ("Which stream is commonly used to write to a file?", ["ofstream", "ifstream", "coutonly", "Scanner"], 0, "`ofstream` is designed for output to files."),
        ("Which stream is commonly used to read from a file?", ["ifstream", "ofstream", "cinonly", "vector"], 0, "`ifstream` is designed for input from files."),
        ("What should you check after opening a file?", ["Whether it opened successfully", "Whether it became a vector", "Whether it is a class", "Whether it has a loop"], 0, "A failed file open should be handled before reading or writing."),
    ],
    "cpp_strings": [
        ("Which function reads a complete line including spaces?", ["getline", "cin_only", "push_back_only", "scanfline"], 0, "`getline` reads until the line delimiter and preserves spaces in the input."),
        ("Why use strings?", ["To represent text", "To represent only loops", "To replace every integer", "To create files automatically"], 0, "Strings are the normal representation for text in these exercises."),
        ("What is a useful first test for text processing?", ["Empty and multi-word input", "Only a single letter", "No input", "Only compiler flags"], 0, "Text bugs often appear around empty input and spaces."),
    ],
    "cpp_references": [
        ("What does a C++ reference provide?", ["Another name for an existing object", "A new array", "A file", "A class hierarchy"], 0, "A reference aliases an existing object rather than creating a separate object."),
        ("Why pass by reference?", ["To let a function work with the caller's original object", "To always copy data", "To prevent changes", "To remove parameters"], 0, "A non-const reference can modify the original object."),
        ("What symbol declares a reference?", ["&", "#", "@", "%"], 0, "In a declaration such as `int& x`, `&` makes x a reference."),
    ],
    "cpp_pointers": [
        ("What does a pointer store?", ["An address", "Only a string", "A loop count", "A class definition"], 0, "Pointers hold memory addresses."),
        ("What does dereferencing a pointer access?", ["The value at the pointed-to address", "The compiler version", "A file path", "The class name"], 0, "Dereferencing follows the pointer to the object/value it points at."),
        ("Why check for `nullptr`?", ["To avoid using an invalid null pointer", "To make a loop faster", "To convert int to string", "To create a vector"], 0, "A null pointer does not point to a valid object."),
    ],
    "cpp_recursion": [
        ("What must a recursive function have?", ["A base case", "An infinite loop", "A global variable", "A vector"], 0, "The base case stops the recursive process."),
        ("What should each recursive call do?", ["Move toward the base case", "Make the problem larger forever", "Delete the function", "Skip all parameters"], 0, "Without progress toward the base case, recursion can fail to terminate."),
        ("What is a good first recursion test?", ["The smallest valid input", "The largest possible input", "A random huge input", "No input"], 0, "Small cases make the recursive structure easier to verify."),
    ],
    "cpp_templates": [
        ("What problem do templates solve?", ["They let code work with multiple compatible types", "They replace all classes", "They make code run without compiling", "They remove functions"], 0, "Templates support generic programming."),
        ("A template function can be instantiated for what?", ["Different types that satisfy its operations", "Only strings", "Only files", "Only booleans"], 0, "The compiler can generate versions for the types used."),
        ("Why use a template for a max function?", ["To avoid rewriting the same logic for each type", "To force one type", "To remove comparisons", "To disable testing"], 0, "Generic code can reuse the same algorithm across compatible types."),
    ],
    "cpp_lambdas": [
        ("What is a lambda?", ["A compact anonymous function", "A file stream", "A class constructor only", "A compiler"], 0, "A lambda defines callable behavior without needing a named function."),
        ("Where are lambdas often useful?", ["With algorithms and local operations", "Only for file storage", "Only for inheritance", "Only for input"], 0, "Lambdas are convenient when behavior is short and local."),
        ("What is one benefit of a lambda?", ["It can keep small behavior close to where it is used", "It removes all variables", "It prevents reuse everywhere", "It avoids compilation"], 0, "Local behavior can be expressed without creating a separate named function."),
    ],
    "cpp_problem_solving": [
        ("What should you identify before coding a specification?", ["Inputs, rules, processing, and outputs", "Only the variable names", "Only the final print statement", "Only the class name"], 0, "Breaking requirements into these parts turns a large task into smaller decisions."),
        ("Why validate input?", ["To prevent invalid data from corrupting the program's logic", "To make programs longer", "To remove all loops", "To avoid output"], 0, "Validation protects the rest of the program from bad assumptions."),
        ("What is a good debugging strategy?", ["Test one requirement at a time", "Change everything at once", "Skip edge cases", "Ignore the specification"], 0, "Small, focused tests make failures easier to locate."),
    ],
    "cpp_project_readiness": [
        ("What should you do first when given a long practical-exam specification?", ["Break it into requirements and rules", "Start coding random parts", "Skip the input section", "Write the final report first"], 0, "A requirement checklist gives you a map before implementation begins."),
        ("Why test edge cases in a practical exam?", ["They reveal hidden logic and validation errors", "They are never important", "They replace the program", "They remove the need for input"], 0, "Edge cases are common sources of failed test cases."),
        ("What is a good final step?", ["Run through the requirements and test the complete flow", "Delete validation", "Remove output", "Stop after compilation only"], 0, "A final requirement-by-requirement review catches missing behavior."),
    ],

    # Java fundamentals
    "java_vars": [
        ("Which is a Java primitive type?", ["int", "String", "ArrayList", "Scanner"], 0, "`int` is a primitive type; String and collections are reference types."),
        ("What does `int age = 18;` do?", ["Declares and initializes age", "Prints age", "Reads age", "Deletes age"], 0, "The statement declares an int and stores 18 in it."),
        ("Which name is clearest for a student's GPA?", ["x", "g", "studentGpa", "thing"], 2, "Descriptive names communicate intent."),
    ],
    "java_io": [
        ("Which class commonly reads console input in beginner Java programs?", ["Scanner", "Printer", "ConsoleArray", "InputLoop"], 0, "`Scanner` reads tokens and lines from `System.in`."),
        ("Which method reads a full line?", ["nextLine()", "nextInt()", "readLineOnly()", "line()"], 0, "`nextLine()` reads the rest of the current line, including spaces."),
        ("What common issue appears after `nextInt()` followed by `nextLine()`?", ["The leftover newline can be consumed by nextLine()", "Java deletes the Scanner", "The int becomes a String", "The program cannot compile"], 0, "The newline left in the input buffer is a common beginner issue."),
    ],
    "java_operators": [
        ("Which operator checks equality for primitive values?", ["==", "=", "=>", "equals-only"], 0, "`==` compares primitive values; object equality often uses `.equals()`."),
        ("What does `%` produce for integer arithmetic?", ["Remainder", "Power", "Average", "Always a percentage"], 0, "Modulo returns the remainder."),
        ("Which Math method can calculate a square root?", ["Math.sqrt", "Math.rootOnly", "Math.square", "Math.divide"], 0, "`Math.sqrt()` returns the square root."),
    ],
    "java_conditionals": [
        ("Which construct is used to choose between conditions?", ["if/else", "ArrayList", "Thread", "import"], 0, "`if`, `else if`, and `else` control conditional branches."),
        ("What does `else` run?", ["When earlier conditions are false", "Always", "Only inside loops", "Only after a class"], 0, "`else` is the fallback branch."),
        ("Why test grade boundaries such as 75?", ["Because boundaries determine which branch should run", "Because 75 is required by Java", "Because loops need it", "Because switch only accepts 75"], 0, "Boundary tests verify that conditions match the intended ranges."),
    ],
    "java_loops": [
        ("Which loop is commonly used when the count is known?", ["for", "catch", "class", "import"], 0, "A for loop is concise when initialization, condition, and update are known."),
        ("What causes an infinite loop?", ["The condition never becomes false", "Using int", "Using braces", "Printing output"], 0, "A loop needs a path toward termination."),
        ("How many times does `for(int i=0;i<3;i++)` run?", ["2", "3", "4", "0"], 1, "The loop runs for i = 0, 1, and 2."),
    ],
    "java_arraylists": [
        ("What does ArrayList provide?", ["A resizable collection", "A fixed compiler", "A database", "A loop"], 0, "ArrayList grows and shrinks as elements are added or removed."),
        ("Which method adds an item?", ["add", "pushOnly", "appendOnly", "insertEndOnly"], 0, "`add()` inserts an element into the list."),
        ("Which method returns the number of elements?", ["size", "lengthOnly", "countItemsOnly", "capacity"], 0, "ArrayList uses `size()` for the current number of elements."),
    ],
    "java_methods": [
        ("Why use methods?", ["To organize reusable logic", "To remove all variables", "To prevent testing", "To make every value global"], 0, "Methods divide a program into focused, reusable operations."),
        ("What does a return type describe?", ["The type of value a method returns", "The number of parameters", "The class size", "The loop count"], 0, "The return type tells Java what result the method produces."),
        ("What makes overloaded methods different?", ["Their parameter lists", "Only their return type", "Their comments", "Their class file name"], 0, "Overloads have the same method name but different parameter lists."),
    ],
    "java_classes": [
        ("What is a class?", ["A blueprint for objects", "A loop", "An exception", "A package"], 0, "A class describes fields and behavior for its objects."),
        ("Why are fields often private?", ["To control access to object state", "To make them global", "To remove constructors", "To disable methods"], 0, "Private fields support encapsulation."),
        ("What does a constructor do?", ["Initializes a new object's state", "Deletes an object", "Runs every loop", "Imports a package"], 0, "Constructors run when an object is created and can initialize its fields."),
    ],
    "java_inheritance": [
        ("Which keyword creates class inheritance in Java?", ["extends", "inherits", "superclass", "derive"], 0, "A class uses `extends` to inherit from another class."),
        ("What does an interface provide?", ["A contract a class can implement", "A loop", "A database", "A primitive type"], 0, "Interfaces define behavior contracts."),
        ("Why use inheritance?", ["To reuse and specialize related behavior", "To avoid all methods", "To remove objects", "To replace input"], 0, "Inheritance models an is-a relationship and enables reuse."),
    ],
    "java_exceptions": [
        ("Which block handles an exception?", ["catch", "loop", "switch", "class"], 0, "A catch block handles an exception thrown from its try block."),
        ("Why use finally?", ["For cleanup that should happen after try/catch", "To repeat code", "To declare variables", "To inherit classes"], 0, "Finally is commonly used for cleanup."),
        ("What should you do with invalid input?", ["Handle it deliberately and explain the problem", "Ignore it", "Always crash", "Delete the Scanner"], 0, "Good programs give the user a clear path when input is invalid."),
    ],
    "java_strings": [
        ("Which method returns a String's length?", ["length()", "size()", "count()", "characters()"], 0, "Strings use `length()` to report the number of characters."),
        ("What is StringBuilder useful for?", ["Repeated string modifications", "Reading integers", "Inheritance", "Threads only"], 0, "StringBuilder is useful when building or changing text repeatedly."),
        ("Why are String objects called immutable?", ["A String's contents do not change after creation", "They cannot be printed", "They are always empty", "They are primitives"], 0, "Operations create new String values rather than changing the original String object."),
    ],
    "java_arrays": [
        ("What is the first array index in Java?", ["0", "1", "-1", "Depends on the JVM"], 0, "Java arrays are zero-indexed."),
        ("For `int[] a = new int[5]`, what is the last valid index?", ["5", "4", "3", "6"], 1, "Five elements occupy indexes 0 through 4."),
        ("What can an invalid index cause?", ["ArrayIndexOutOfBoundsException", "Syntax success", "Automatic resizing", "A new class"], 0, "Accessing outside the valid range causes a runtime exception."),
    ],
    "java_overloading": [
        ("What must differ between overloaded methods?", ["Their parameter lists", "Only comments", "Only return types", "Only method visibility"], 0, "Java chooses an overload based on the method name and parameter list."),
        ("Can two methods differ only by return type?", ["No", "Yes always", "Only in loops", "Only in constructors"], 0, "Return type alone is not enough to distinguish overloads."),
        ("Why overload a method?", ["To support related calls with different parameter types/counts", "To remove methods", "To prevent reuse", "To create files"], 0, "Overloading gives a consistent method name for related operations."),
    ],
    "java_encapsulation": [
        ("What is a common encapsulation pattern?", ["private fields with public methods", "all fields public", "no classes", "only static variables"], 0, "Private state plus controlled methods protects object invariants."),
        ("Why use a getter?", ["To read controlled object state", "To create a thread", "To compile faster", "To delete a field"], 0, "A getter exposes a value without making the field directly public."),
        ("What is the benefit of controlled access?", ["The class can enforce rules when state changes", "It removes all logic", "It prevents objects", "It makes every field global"], 0, "Methods can validate or constrain changes to the object's state."),
    ],
    "java_polymorphism": [
        ("What is method overriding?", ["A subclass provides its own implementation of an inherited method", "Creating a second variable", "Importing a package", "Overloading only by return type"], 0, "Overriding changes inherited behavior in a subclass."),
        ("Why use a parent reference?", ["It can point to different subclass objects through a common type", "It removes inheritance", "It prevents methods", "It makes all classes identical"], 0, "A common parent type supports polymorphic code."),
        ("What does polymorphism provide?", ["One interface with different object-specific behavior", "Only one possible behavior", "No objects", "Only primitive values"], 0, "The same call can behave differently depending on the actual object."),
    ],
    "java_abstract": [
        ("What is an abstract class used for?", ["Shared structure plus required subclass behavior", "Only primitive storage", "Reading files only", "Creating infinite loops"], 0, "Abstract classes can define shared members and abstract methods."),
        ("Can you normally instantiate an abstract class directly?", ["No", "Yes always", "Only inside a loop", "Only with Scanner"], 0, "Abstract classes represent incomplete blueprints and require a concrete subclass."),
        ("Why use an abstract method?", ["To require subclasses to provide an implementation", "To remove all methods", "To prevent inheritance", "To print output"], 0, "The abstract method defines a required behavior without its implementation."),
    ],
    "java_interfaces": [
        ("What does an interface define?", ["A contract of behavior", "A database table", "A loop count", "A primitive"], 0, "Interfaces define methods/behavior that implementing classes agree to provide."),
        ("Which keyword implements an interface?", ["implements", "extends-only", "interfaceUse", "inherits"], 0, "A class uses `implements` to fulfill an interface contract."),
        ("Why are interfaces useful?", ["They let unrelated classes share a common contract", "They remove all classes", "They prevent polymorphism", "They replace constructors"], 0, "Interfaces are a key tool for abstraction and polymorphism."),
    ],
    "java_arraylist": [
        ("Which method retrieves an ArrayList element at an index?", ["get", "fetchOnly", "readAt", "item"], 0, "`get(index)` returns the element at that position."),
        ("Which method removes an element?", ["remove", "deleteOnly", "eraseList", "dropAll"], 0, "`remove()` removes an element by index or matching object depending on the overload."),
        ("Why use ArrayList?", ["For a resizable collection of objects", "For inheritance", "For primitive-only memory", "For database connections"], 0, "ArrayList is a flexible collection for reference types."),
    ],
    "java_hashmap": [
        ("What does HashMap store?", ["Key-value pairs", "Only indexes", "Only methods", "Only files"], 0, "A HashMap associates keys with values."),
        ("How do you retrieve a value by key?", ["get(key)", "read(key)", "findValueOnly", "valueAt"], 0, "`get(key)` returns the value associated with the key."),
        ("What should you consider before using a key?", ["Whether the key identifies the value consistently", "Whether the key is a loop", "Whether it is always an int", "Whether it is a file"], 0, "Keys should represent a stable identifier for the associated data."),
    ],
    "java_generics": [
        ("What do generics provide?", ["Type-safe reusable classes and methods", "Automatic database storage", "Threads", "Only inheritance"], 0, "Generics let you express what type a reusable component works with."),
        ("What does `Box<String>` communicate?", ["This Box is intended to hold Strings", "It holds only ints", "It is an interface", "It creates a thread"], 0, "The type argument tells Java what element type the generic is parameterized with."),
        ("Why use generics?", ["To catch many type mistakes at compile time", "To remove types", "To avoid compilation", "To make everything global"], 0, "Generic type information improves compile-time safety."),
    ],
    "java_fileio": [
        ("What should file code do before reading?", ["Open the file/resource successfully", "Create a loop only", "Make every value an int", "Delete the file"], 0, "File operations depend on a successfully opened resource."),
        ("Why handle I/O exceptions?", ["File operations can fail", "Files never fail", "It removes classes", "It changes Java syntax"], 0, "Missing files, permissions, and other I/O problems need handling."),
        ("What is a good resource-management habit?", ["Close resources after use", "Leave every file open", "Ignore failures", "Use random paths"], 0, "Closing resources prevents leaks and keeps programs well behaved."),
    ],
    "java_streams": [
        ("What is a stream useful for?", ["Processing collections through operations like filter/map", "Creating classes only", "Opening files only", "Declaring primitives"], 0, "Streams provide a pipeline for collection processing."),
        ("What does `filter` do?", ["Keeps elements matching a condition", "Sorts automatically", "Deletes the collection", "Creates a database"], 0, "Filter selects elements that satisfy a predicate."),
        ("Why pair streams with lambdas?", ["Lambdas provide compact behavior for stream operations", "Lambdas are required for variables", "They prevent filtering", "They replace classes"], 0, "Stream pipelines often use lambdas to express the operation being applied."),
    ],
    "java_enums": [
        ("What does an enum represent?", ["A fixed set of named constants", "A resizable list", "A database connection", "A loop"], 0, "Enums model a small, known set of states or choices."),
        ("Why use an enum for payment methods?", ["It makes allowed choices explicit", "It allows any random string", "It removes validation", "It creates threads"], 0, "The enum limits the state to defined values."),
        ("What is an advantage of named constants?", ["They make code clearer than unexplained magic values", "They remove all types", "They prevent compilation", "They replace methods"], 0, "Meaningful names make program state easier to understand."),
    ],
    "java_recursion": [
        ("What must recursive code have?", ["A base case", "An infinite loop", "A global scanner", "A HashMap"], 0, "The base case stops recursion."),
        ("What should recursive calls do?", ["Move toward a smaller or simpler problem", "Grow forever", "Skip the base case", "Delete the method"], 0, "Each call should make measurable progress toward termination."),
        ("Why test the smallest input first?", ["It validates the base case", "It guarantees all cases", "It removes recursion", "It compiles without code"], 0, "The base case is the foundation of recursive correctness."),
    ],
    "java_threads": [
        ("What is a thread?", ["A path of execution", "A database row", "A String", "A class constructor"], 0, "A thread represents an independent path of execution within a process."),
        ("Why can shared data be dangerous with threads?", ["Multiple threads may change it at overlapping times", "Threads cannot use variables", "Java deletes data", "Threads only print"], 0, "Concurrent access can create race conditions without coordination."),
        ("What is synchronization for?", ["Coordinating access to shared state", "Creating a loop", "Reading Scanner input", "Declaring enums"], 0, "Synchronization helps protect shared state from unsafe concurrent access."),
    ],
    "java_jdbc": [
        ("What is JDBC used for?", ["Connecting Java applications to databases", "Drawing UI only", "Creating arrays", "Running loops"], 0, "JDBC provides the standard Java API for database connectivity."),
        ("Why use prepared statements for user input?", ["They help parameterize SQL safely", "They remove databases", "They make queries longer only", "They disable validation"], 0, "Prepared statements separate SQL structure from parameter values and help prevent injection."),
        ("What should happen after database work?", ["Close resources appropriately", "Leave every connection open", "Delete the database", "Ignore errors"], 0, "Connections and related resources should be managed carefully."),
    ],
    "java_testing": [
        ("Why test boundary cases?", ["They expose errors at the edges of valid input", "They are never useful", "They remove methods", "They make code compile"], 0, "Boundary cases are where range and validation mistakes often appear."),
        ("What is a useful debugging step?", ["Reproduce the smallest failing case", "Change everything at once", "Ignore the first error", "Delete the test"], 0, "A minimal reproduction makes the cause easier to isolate."),
        ("What makes a test valuable?", ["A known input with an expected result", "A random result", "No expectation", "Only a compile check"], 0, "A test needs an expected behavior so the actual result can be judged."),
    ],
    "java_problem_solving": [
        ("What should you extract from a real-world specification?", ["Inputs, validation, calculations, and outputs", "Only variable names", "Only comments", "Only the final print"], 0, "Decomposing requirements makes implementation manageable."),
        ("Why validate records before processing them?", ["To keep invalid data from entering later calculations", "To remove loops", "To skip output", "To make all data strings"], 0, "Validation protects later logic from invalid assumptions."),
        ("What is a good implementation order?", ["Build and test one requirement at a time", "Write everything at once", "Skip testing until the end", "Ignore edge cases"], 0, "Incremental implementation makes failures easier to locate."),
    ],
    "java_project_readiness": [
        ("What is a strong first step on a large practical task?", ["Turn the specification into a checklist of requirements", "Start typing random code", "Skip input validation", "Write only the final report"], 0, "A checklist prevents important requirements from being forgotten."),
        ("Why test edge cases?", ["They reveal boundary and validation mistakes", "They are irrelevant", "They replace the program", "They remove classes"], 0, "Edge cases often distinguish a robust solution from one that only works on easy input."),
        ("What should a final review check?", ["Every requirement, normal case, and important edge case", "Only whether the file opens", "Only whether it has comments", "Only the class name"], 0, "A complete review checks behavior against the original specification."),
    ],
}


def fallback_questions(topic: dict, language: str) -> list[tuple[str, list[str], int, str]]:
    title = topic["title"]
    description = topic.get("description", "")
    return [
        (
            f"What is the main purpose of **{title}**?",
            [
                f"To apply the concept described by the lesson",
                "To replace every other programming concept",
                "To avoid testing programs",
                "To make all code identical",
            ],
            0,
            f"This lesson focuses on {description.lower().rstrip('.')}.",
        ),
        (
            "What is the best learning strategy for this lesson?",
            ["Understand the idea, then practice it", "Memorize without testing", "Skip examples", "Avoid small exercises"],
            0,
            "Understanding plus deliberate practice is more useful than memorizing syntax alone.",
        ),
        (
            "What should you do when your first solution fails?",
            ["Use a small test case and inspect the first error", "Change everything randomly", "Ignore the error", "Delete the whole project"],
            0,
            "Small, focused debugging steps make the cause easier to find.",
        ),
    ]



QUESTION_OVERRIDES.update({
    "cpp_functions_deeper": [
        ("What makes a function easier to reuse?", ["A clear job and well-chosen parameters", "Global variables for everything", "No return type ever", "An infinite loop"], 0, "A focused function is easier to call, test, and reuse."),
        ("If a function returns the larger of two integers, what should it return?", ["The larger value", "Both values as text", "The loop count", "The variable name"], 0, "The function's result should match its stated responsibility."),
        ("Why keep main focused on program flow?", ["It makes the overall program easier to read", "It prevents functions", "It removes testing", "It makes all data global"], 0, "Moving reusable work into functions keeps the entry point understandable."),
    ],
    "cpp_vectors_2": [
        ("What does `vector<int>` describe?", ["A vector storing integers", "A vector storing only strings", "A fixed class", "A file stream"], 0, "The template argument specifies the element type."),
        ("What should you use to process every element in a vector?", ["A loop or suitable algorithm", "Only a class constructor", "A file stream", "A compiler flag"], 0, "Iteration lets you inspect or process the stored elements."),
        ("Why calculate a vector's sum with a loop?", ["Each element contributes to the total", "Vectors can only store one value", "Loops are required by the compiler", "Sum is automatic"], 0, "A running total combines the elements one by one."),
    ],
    "cpp_searching": [
        ("What does a linear search do?", ["Checks elements one by one for a target", "Always sorts first", "Creates a class", "Reads a file"], 0, "Linear search scans through the collection until it finds the target or reaches the end."),
        ("How do you find a maximum while scanning values?", ["Track the largest value seen so far", "Always choose the last value", "Sort every time", "Use a string"], 0, "A running maximum compares each new value with the best value seen so far."),
        ("What should a search report when the target is absent?", ["A clear not-found result", "A random index", "The last value automatically", "A compiler error"], 0, "The program should distinguish a successful match from no match."),
    ],
    "cpp_nested_loops": [
        ("What is a nested loop?", ["A loop inside another loop", "A function inside a variable", "A class inside a string", "A file inside a vector"], 0, "The inner loop runs as part of each outer-loop iteration."),
        ("Where are nested loops useful?", ["Tables, grids, and repeated comparisons", "Only file closing", "Only constructors", "Only input"], 0, "Two dimensions or pairwise comparisons often naturally use nested loops."),
        ("Why test a small pattern first?", ["It makes the loop order easier to verify", "It prevents compilation", "It removes the inner loop", "It guarantees all outputs"], 0, "Small patterns make indexing and repetition easier to inspect."),
    ],
    "cpp_structs": [
        ("What is a struct useful for?", ["Grouping related data into one record", "Creating infinite loops", "Reading files automatically", "Replacing every class"], 0, "A struct can model a simple record with related fields."),
        ("A Product struct might contain which fields?", ["name and price", "only a loop", "only a function", "only a compiler setting"], 0, "Related properties such as name and price belong naturally in one record."),
        ("Why group fields into a record?", ["It keeps related information together", "It removes all types", "It prevents objects", "It makes input unnecessary"], 0, "A record represents one logical entity instead of scattered variables."),
    ],
    "cpp_dynamic_memory": [
        ("What does `new` generally do in C++?", ["Allocates an object dynamically", "Deletes memory", "Reads input", "Sorts a vector"], 0, "`new` requests dynamically allocated storage and returns an address."),
        ("What is the traditional matching operation for memory from `new`?", ["delete", "remove", "free-only", "erase"], 0, "Memory allocated with `new` is traditionally released with `delete`; modern C++ often prefers RAII tools."),
        ("Why prefer containers or smart pointers when appropriate?", ["They reduce manual memory-management mistakes", "They remove types", "They disable objects", "They prevent compilation"], 0, "RAII-based tools manage lifetime more safely than manual allocation."),
    ],
    "cpp_classes_2": [
        ("What do classes combine?", ["Data and behavior", "Only loops", "Only output", "Only files"], 0, "A class can contain state and member functions that operate on it."),
        ("What creates an object from a class?", ["An object declaration or construction", "A compiler error", "A loop condition", "A comment"], 0, "Objects are instances of classes."),
        ("Why use classes?", ["To organize related state and behavior", "To avoid all functions", "To remove data", "To make programs untestable"], 0, "Classes help structure larger programs around meaningful entities."),
    ],
    "cpp_encapsulation": [
        ("What is encapsulation?", ["Controlling access to an object's state and behavior", "Making every field global", "Removing classes", "Avoiding methods"], 0, "Encapsulation hides implementation details and controls how state changes."),
        ("Why use a constructor?", ["To initialize an object's state", "To run every loop", "To delete a file", "To read input only"], 0, "Constructors establish an object's initial valid state."),
        ("Why keep a balance private in a BankAccount?", ["So methods can enforce rules around changes", "So it cannot ever change", "So it becomes global", "So the class disappears"], 0, "Controlled methods can prevent invalid state changes."),
    ],
    "cpp_inheritance": [
        ("What does inheritance allow?", ["A derived class to reuse and extend base behavior", "A variable to become a loop", "A file to become an object", "A vector to become a class"], 0, "Inheritance models a relationship where a derived type specializes a base type."),
        ("What is a base class?", ["The class whose members can be inherited", "The last object created", "A compiler setting", "A file stream"], 0, "The base class provides the common foundation."),
        ("Why avoid unnecessary inheritance?", ["Simple composition or direct classes may be easier to maintain", "Inheritance never works", "C++ forbids it", "It removes constructors"], 0, "Use inheritance when the relationship and reuse are genuinely appropriate."),
    ],
    "cpp_polymorphism": [
        ("What enables runtime polymorphism in common C++ designs?", ["Virtual functions", "Only macros", "Only loops", "Only vectors"], 0, "Virtual dispatch lets a derived override be selected through a base interface."),
        ("What does `override` communicate?", ["That a derived method is intended to override a base virtual method", "That a method is private", "That a loop repeats", "That a class is abstract automatically"], 0, "The keyword helps the compiler verify the intended override."),
        ("Why use a base pointer/reference in polymorphism?", ["It can work with multiple derived object types through a common interface", "It removes inheritance", "It forces one concrete type", "It prevents virtual dispatch"], 0, "A common interface lets the caller remain independent of the concrete derived type."),
    ],
    "cpp_stl": [
        ("What is the STL?", ["A library of useful containers, algorithms, and utilities", "A compiler", "A database", "A debugger only"], 0, "The C++ Standard Library provides containers, algorithms, and many utilities."),
        ("Which STL container stores key-value pairs?", ["map", "vector", "set-only", "pair-only"], 0, "`map` associates keys with values."),
        ("Why use standard containers?", ["They provide tested building blocks for common data structures", "They remove the need to think", "They prevent loops", "They replace the compiler"], 0, "Using standard tools can make code shorter, clearer, and more reliable."),
    ],
    "cpp_algorithms": [
        ("What does algorithm complexity describe?", ["How resource use grows with input size", "The variable names", "The screen size", "The compiler brand"], 0, "Complexity helps reason about how an algorithm scales."),
        ("What is linear search's typical time complexity?", ["O(n)", "O(1) always", "O(n\u00b2) always", "O(log log n)"], 0, "A linear scan may inspect each of n elements."),
        ("Why consider complexity?", ["A solution that works on small data may become slow on large data", "It changes syntax", "It removes testing", "It prevents input"], 0, "Scaling behavior matters when data size grows."),
    ],
    "cpp_files_2": [
        ("Which C++ header provides file streams?", ["<fstream>", "<vector>", "<thread>", "<map>"], 0, "`<fstream>` contains the standard file stream types."),
        ("What should you do if a file fails to open?", ["Handle the failure before using the stream", "Pretend it opened", "Delete the program", "Continue reading random data"], 0, "Always verify the resource is usable."),
        ("Why use file I/O in applications?", ["To persist information between runs", "To remove all data", "To replace functions", "To disable input"], 0, "Files can preserve information after the program exits."),
    ],
    "cpp_exceptions": [
        ("Which block handles a thrown exception?", ["catch", "for", "switch", "class"], 0, "A catch block handles a matching exception from a try block."),
        ("When is exception handling useful?", ["When an operation can fail in an exceptional way", "For every variable declaration", "Only for loops", "Only for printing"], 0, "Exceptions are appropriate for exceptional failure paths in APIs that use them."),
        ("What is a poor error-handling habit?", ["Catching everything and hiding the cause", "Explaining the failure", "Testing invalid input", "Cleaning up resources"], 0, "Hiding errors makes debugging and reliability worse."),
    ],
    "java_methods_2": [
        ("What do method parameters provide?", ["Inputs to the method", "Only output formatting", "A class hierarchy", "A thread"], 0, "Parameters let callers provide the data the method needs."),
        ("What should a method returning an int provide?", ["An int result on every required path", "Only a String", "Only a loop", "No result ever"], 0, "The declared return type determines the expected result."),
        ("Why make a method for 'larger of two integers'?", ["It isolates a reusable decision", "It prevents reuse", "It removes parameters", "It makes the program global"], 0, "A focused method can be called wherever that operation is needed."),
    ],
    "java_classes_2": [
        ("What does a constructor initialize?", ["A newly created object's state", "The JVM", "A package", "A loop counter globally"], 0, "Constructors initialize instances when they are created."),
        ("How is a constructor named?", ["With the same name as the class", "With return type void", "With the word constructor only", "With the package name"], 0, "Java constructors use the class name and have no return type."),
        ("Why initialize fields in a constructor?", ["To establish a useful initial state", "To prevent objects", "To remove methods", "To disable inheritance"], 0, "A well-initialized object is safer to use."),
    ],
    "java_inheritance_2": [
        ("Which keyword creates a subclass?", ["extends", "inherits", "child", "super"], 0, "`extends` declares class inheritance."),
        ("What can a child class do?", ["Reuse and specialize inherited behavior", "Only delete parent methods", "Only store primitives", "Only read files"], 0, "A subclass can add behavior and override inherited methods."),
        ("What is a benefit of inheritance?", ["Sharing common behavior across related types", "Avoiding all classes", "Removing polymorphism", "Preventing reuse"], 0, "Inheritance can reduce duplication when the relationship is appropriate."),
    ],
    "java_exceptions_2": [
        ("Which keyword can explicitly throw an exception?", ["throw", "throwsOnly", "catchOnly", "raise"], 0, "`throw` actually throws a specific exception object."),
        ("What is `throws` used for?", ["Declaring that a method may propagate specified checked exceptions", "Catching an exception", "Creating a thread", "Declaring an enum"], 0, "`throws` appears in a method signature to declare propagated checked exceptions."),
        ("Why give users a friendly error message?", ["It explains what went wrong and what they can do next", "It hides all bugs", "It removes validation", "It changes the type system"], 0, "Clear feedback makes invalid input easier to recover from."),
    ],
})

def _mastery_question(question, category: str):
    """Normalize a curriculum question and attach a mastery skill category."""
    text, options, answer, explanation = question
    return {
        "question": text,
        "options": list(options),
        "answer": int(answer),
        "explanation": explanation,
        "category": category,
    }


def _code_reading_question(topic: dict, language: str):
    """Build a small code-reading question from the lesson's own worked example.

    This is deliberately generated from the lesson record rather than from a
    shared question bank. It tests whether the student can connect syntax to
    behavior, not just recognize terminology.
    """
    code = clean_code(topic.get("example1", ""))
    candidates = []
    for raw in code.splitlines():
        line = raw.strip()
        if not line or line in {"{", "}"} or line.startswith("//"):
            continue
        explanation = line_explanation(line, language)
        if explanation == "performs part of the program's logic":
            continue
        candidates.append((line, explanation))

    if candidates:
        line, correct = random.choice(candidates)
        distractors = [
            "declares a completely unrelated class or object",
            "starts a new source file or package",
            "automatically fixes every runtime and logic error",
        ]
        return {
            "question": f"In this lesson's worked example, what is the main role of `{line[:95]}`?",
            "options": [correct, *distractors],
            "answer": 0,
            "explanation": f"That line {correct.lower()}. Focus on what the statement actually does, not just what it is called.",
            "category": "Code reading",
        }

    # Some advanced lessons use a compact syntax specimen rather than a full
    # executable example. In that case, test the student's ability to reason
    # about the lesson's own syntax breakdown instead of dropping the category.
    breakdown = list(topic.get("syntax_breakdown", []))
    if breakdown:
        correct = breakdown[0]
        distractors = [x for x in breakdown[1:] if x != correct][:3]
        while len(distractors) < 3:
            distractors.append("An unrelated implementation detail that the lesson does not require")
        return {
            "question": f"When reading the syntax for **{topic['title']}**, which point should you focus on first?",
            "options": [correct, *distractors],
            "answer": 0,
            "explanation": f"The lesson's syntax breakdown starts here: {correct}",
            "category": "Code reading",
        }
    return None


def _debug_question(topic: dict):
    """Turn a lesson-specific common mistake into a diagnostic question."""
    mistakes = list(topic.get("common_mistakes", []))
    tips = list(topic.get("beginner_tips", []))
    if not mistakes:
        return None
    correct = random.choice(mistakes)
    distractors = []
    for item in tips:
        if item != correct and item not in distractors:
            distractors.append(item)
        if len(distractors) == 3:
            break
    while len(distractors) < 3:
        distractors.append("Testing the program with a normal case before changing anything")
    return {
        "question": "Which situation is a lesson-specific mistake you should actively check for?",
        "options": [correct, *distractors[:3]],
        "answer": 0,
        "explanation": f"Watch for this because it is listed in the lesson's own common-mistakes guidance: {correct}",
        "category": "Debugging",
    }


def _application_question(topic: dict):
    """Test transfer by asking which next action actually applies the lesson."""
    practice = topic.get("practice_problem", "").strip()
    extension = topic.get("extension", "").strip()
    if not practice:
        return None
    distractors = [
        "Ignore the lesson concept and solve the problem by changing unrelated parts of the program.",
        "Copy the worked example unchanged without adapting it to the new requirement.",
        "Skip testing and assume the first version is correct.",
    ]
    return {
        "question": f"Which action best applies what you learned in **{topic['title']}** to the practice problem?",
        "options": [
            f"Implement the practice requirement and test the relevant edge cases: {practice[:210]}",
            *distractors,
        ],
        "answer": 0,
        "explanation": f"The practice problem is the lesson's transfer task. {extension[:350]}",
        "category": "Application",
    }


def lesson_questions(topic: dict, language: str):
    """Return a stronger five-part mastery check owned by this lesson.

    The first two questions remain the lesson author's own questions. The
    remaining questions deliberately test different skills using this exact
    lesson's example, mistakes, and practice problem:

    1. Core concept
    2. Syntax and usage
    3. Code reading
    4. Debugging
    5. Application / transfer

    If a lesson record cannot supply a generated question, an unused original
    question fills the slot so every valid curriculum record remains playable.
    """
    original = list(topic["mastery_quiz"])
    questions = []
    categories = ["Core concept", "Syntax & usage"]
    # Pick two distinct author-written questions on each attempt. The generated
    # questions below also vary their lesson-specific code/mistake examples, so
    # retries test the same topic without replaying an identical quiz every time.
    chosen_originals = random.sample(original, k=min(2, len(original)))
    for index, category in enumerate(categories):
        if index < len(chosen_originals):
            questions.append(_mastery_question(chosen_originals[index], category))

    generated = [
        _code_reading_question(topic, language),
        _debug_question(topic),
        _application_question(topic),
    ]
    for item in generated:
        if item:
            questions.append(item)

    # Preserve the five-question contract even if a future lesson record is
    # unusually sparse. Prefer unused author-written questions as the fallback.
    used_text = {q["question"] for q in questions}
    for raw in original[2:]:
        if len(questions) >= 5:
            break
        if raw[0] not in used_text:
            questions.append(_mastery_question(raw, "Lesson knowledge"))
            used_text.add(raw[0])

    if len(questions) < 5:
        raise ValueError(f"Lesson {topic['id']} has fewer than five usable mastery questions")
    return questions[:5]


# -----------------------------
# Database-backed mastery
# -----------------------------

async def get_mastery(user_id: int, language: str, topic_id: str):
    return await db.fetchone(
        "SELECT best_score, last_score, attempts, passed, xp_awarded, weak_categories, review_due_at, demonstration_completed FROM lesson_mastery WHERE user_id=? AND language=? AND topic_id=?",
        (user_id, language, topic_id),
    )


async def record_mastery(user_id: int, language: str, topic_id: str, score: int, passed: bool, weak_categories=None):
    if type(score) is not int:
        raise TypeError("score must be an integer")
    if not 0 <= score <= 5:
        raise ValueError("score must be between 0 and 5")
    if type(passed) is not bool:
        raise TypeError("passed must be a boolean")
    if passed != (score >= 4):
        raise ValueError("passed must match the mastery passing threshold")

    weak = ", ".join(dict.fromkeys(weak_categories or []))
    # Spaced retrieval: failed attempts return quickly; stronger passes wait longer.
    delay_days = 1 if not passed else (3 if score == 4 else 7)
    due = manila_timestamp(manila_now() + timedelta(days=delay_days)).strftime("%Y-%m-%d %H:%M:%S")

    def operation(conn):
        ensure_user_in_transaction(conn, user_id, None)
        old = conn.execute(
            "SELECT best_score, attempts, xp_awarded, passed FROM lesson_mastery WHERE user_id=? AND language=? AND topic_id=?",
            (user_id, language, topic_id),
        ).fetchone()
        best = max(score, int(old["best_score"]) if old else 0)
        attempts = (int(old["attempts"]) if old else 0) + 1
        conn.execute(
            """INSERT INTO lesson_mastery(user_id,language,topic_id,best_score,last_score,attempts,passed,xp_awarded,weak_categories,review_due_at,updated_at)
               VALUES(?,?,?,?,?,?,?,?,?,?,CURRENT_TIMESTAMP)
               ON CONFLICT(user_id,language,topic_id) DO UPDATE SET
                 best_score=CASE WHEN lesson_mastery.best_score>excluded.best_score THEN lesson_mastery.best_score ELSE excluded.best_score END,
                 last_score=excluded.last_score,
                 attempts=lesson_mastery.attempts+1,
                 passed=CASE WHEN lesson_mastery.passed=1 OR excluded.passed=1 THEN 1 ELSE 0 END,
                 weak_categories=excluded.weak_categories,
                 review_due_at=excluded.review_due_at,
                 updated_at=CURRENT_TIMESTAMP""",
            (user_id, language, topic_id, best, score, attempts, int(passed), int(old["xp_awarded"]) if old else 0, weak, due),
        )
        return conn.execute(
            "SELECT best_score, last_score, attempts, passed, xp_awarded, weak_categories, review_due_at, demonstration_completed FROM lesson_mastery WHERE user_id=? AND language=? AND topic_id=?",
            (user_id, language, topic_id),
        ).fetchone()

    return await db.run_transaction(operation)



class CodeReviewResultView(discord.ui.View):
    def __init__(self, language: str, topic: dict):
        super().__init__(timeout=600)
        self.language = language
        self.topic = topic

    @discord.ui.button(label="\U0001f50e Review Again", style=discord.ButtonStyle.secondary)
    async def review_again(self, interaction: discord.Interaction, button):
        await interaction.response.send_modal(ReviewCodeModal(self.language, self.topic))

    @discord.ui.button(label="\U0001f41b Debug This Code", style=discord.ButtonStyle.primary)
    async def debug_this(self, interaction: discord.Interaction, button):
        await interaction.response.send_modal(DebugCodeModal(self.language, self.topic))


class ReviewCodeModal(discord.ui.Modal):
    def __init__(self, language: str, topic: dict):
        super().__init__(title=f"Review My Code \u2014 {topic['title'][:25]}")
        self.language = language
        self.topic = topic
        self.code = discord.ui.TextInput(
            label="Paste your code",
            style=discord.TextStyle.paragraph,
            placeholder="Paste code only \u2014 never passwords, tokens, or private data.",
            required=True,
            max_length=4000,
        )
        self.add_item(self.code)

    async def on_submit(self, interaction: discord.Interaction):
        cleaned = clean_code(self.code.value)
        if not cleaned:
            await interaction.response.send_message("\u274c Please enter some code.", ephemeral=True)
            return
        cog = interaction.client.get_cog("CodeReviewCog")
        if cog is None:
            await interaction.response.send_message("\u26a0\ufe0f The AI code-review service is currently unavailable.", ephemeral=True)
            return
        await interaction.response.defer(ephemeral=True)
        text = await cog.review_student_code(
            self.language,
            self.topic["title"],
            self.topic.get("description", ""),
            cleaned,
            user_id=interaction.user.id,
        )
        embed = discord.Embed(
            title=f"\U0001f50e Code Review \u2014 {('C++' if self.language == 'cpp' else 'Java')}",
            description=text[:4000],
            color=discord.Color.blurple(),
        )
        embed.set_footer(text="AI feedback is guidance, not an official grade. Do not submit passwords, API keys, or private data.")
        await interaction.followup.send(embed=embed, view=CodeReviewResultView(self.language, self.topic), ephemeral=True, allowed_mentions=discord.AllowedMentions.none())


class DebugCodeModal(discord.ui.Modal):
    def __init__(self, language: str, topic: dict):
        super().__init__(title=f"Debug Coach \u2014 {topic['title'][:25]}")
        self.language = language
        self.topic = topic
        self.code = discord.ui.TextInput(
            label="Your code",
            style=discord.TextStyle.paragraph,
            placeholder="Paste code only \u2014 never passwords, tokens, or private data.",
            required=True,
            max_length=4000,
        )
        self.error = discord.ui.TextInput(
            label="Error message (optional)",
            style=discord.TextStyle.paragraph,
            placeholder="Paste the compiler/runtime error, if you have one...",
            required=False,
            max_length=1500,
        )
        self.add_item(self.code)
        self.add_item(self.error)

    async def on_submit(self, interaction: discord.Interaction):
        cleaned = clean_code(self.code.value)
        if not cleaned:
            await interaction.response.send_message("\u274c Please enter your code.", ephemeral=True)
            return
        cog = interaction.client.get_cog("CodeReviewCog")
        if cog is None:
            await interaction.response.send_message("\u26a0\ufe0f The Debugging Coach is currently unavailable.", ephemeral=True)
            return
        await interaction.response.defer(ephemeral=True)
        text = await cog.debug_student_code(
            self.language,
            self.topic["title"],
            cleaned,
            self.error.value.strip(),
            user_id=interaction.user.id,
        )
        embed = discord.Embed(title="\U0001f41b Debugging Coach", description=text[:4000], color=discord.Color.orange())
        embed.set_footer(text="Try the suggested step yourself before asking for a stronger hint.")
        await interaction.followup.send(embed=embed, ephemeral=True, allowed_mentions=discord.AllowedMentions.none())


class MiniChallengeView(discord.ui.View):
    def __init__(self, language: str, topic: dict):
        super().__init__(timeout=600)
        self.language = language
        self.topic = topic

    @discord.ui.button(label="\U0001f4bb Submit Challenge Code", style=discord.ButtonStyle.success)
    async def submit(self, interaction: discord.Interaction, button):
        await interaction.response.send_modal(MiniChallengeCodeModal(self.language, self.topic))


class MiniChallengeCodeModal(discord.ui.Modal):
    def __init__(self, language: str, topic: dict):
        super().__init__(title=f"Mini Challenge \u2014 {topic['title'][:24]}")
        self.language = language
        self.topic = topic
        self.code = discord.ui.TextInput(
            label="Your solution",
            style=discord.TextStyle.paragraph,
            placeholder="Write your solution \u2014 no passwords, tokens, or private data.",
            required=True,
            max_length=4000,
        )
        self.add_item(self.code)

    async def on_submit(self, interaction: discord.Interaction):
        cleaned = clean_code(self.code.value)
        if not cleaned:
            await interaction.response.send_message("\u274c Please enter your solution.", ephemeral=True)
            return
        cog = interaction.client.get_cog("CodeReviewCog")
        if cog is None:
            await interaction.response.send_message("\u26a0\ufe0f The Mini Challenge coach is currently unavailable.", ephemeral=True)
            return
        await interaction.response.defer(ephemeral=True)
        text = await cog.evaluate_mini_challenge(
            self.language,
            self.topic["title"],
            self.topic.get("exercise", "Complete the lesson exercise."),
            cleaned,
            user_id=interaction.user.id,
        )
        embed = discord.Embed(title="\U0001f3af Mini Challenge Feedback", description=text[:4000], color=discord.Color.green())
        embed.set_footer(text="Coaching feedback only \u2014 not an official grade. Do not submit private data.")
        await interaction.followup.send(embed=embed, ephemeral=True, allowed_mentions=discord.AllowedMentions.none())

# -----------------------------
# Lesson UI
# -----------------------------

def mastery_line(mastery) -> str:
    if not mastery:
        return "\U0001f9e0 **Mastery check:** Not attempted yet"
    best = int(mastery["best_score"])
    attempts = int(mastery["attempts"])
    return f"\U0001f9e0 **Mastery check:** {'\u2705 Passed' if mastery['passed'] else '\U0001f7e1 Try again'} \u2022 Best **{best}/5** \u2022 Attempts **{attempts}**"


def guided_next_step(section: str, status: str, mastery=None) -> str:
    if section == "overview":
        return "➡️ **Next:** Click **📖 Learn** to understand the concept and why it matters."
    if section == "learn":
        return "➡️ **Next:** Click **💻 Example** to trace the worked code, then use the guided practice in **🧪 Practice**."
    if section == "example":
        return "➡️ **Next:** Click **🧪 Practice**. Do the guided task first, then attempt the independent task."
    if section == "practice":
        return "➡️ **Next:** Click **🧠 Mastery Check** after completing the independent practice and reviewing your test cases."
    if section == "check":
        if mastery and mastery["passed"] and status == "completed":
            return "➡️ **Next:** Click **➡️ Next Lesson** to continue, or **🔄 Review** later when this topic comes due."
        return "➡️ **Next:** Click **🧠 Mastery Check** and pass **4/5**. If you miss questions, review the named skill areas before retrying."
    if mastery and mastery["passed"] and status != "completed":
        return "➡️ **Next:** Click **✅ Complete Lesson**, then **➡️ Next Lesson**."
    return "➡️ **Next:** Review **📖 Learn**, redo **🧪 Practice**, then click **🧠 Mastery Check** and pass 4/5."


def lesson_embed(language: str, topic: dict, section: str, status: str, mastery=None) -> discord.Embed:
    lang = "C++" if language == "cpp" else "Java"
    number, total = topic_number(language, topic["id"])
    status_text = "✅ Completed" if status == "completed" else ("🟡 Review" if status == "review" else "🟢 In progress")
    colors = {
        "overview": discord.Color.blurple(), "learn": discord.Color.blurple(),
        "example": discord.Color.teal(), "practice": discord.Color.green(),
        "check": discord.Color.gold(), "mastery": discord.Color.purple(),
    }
    embed = discord.Embed(
        title=f"{('🟦' if language == 'cpp' else '☕')} {lang} • Lesson {number}/{total} • {topic['title']}",
        description=f"**{topic['introduction']}**\n\n**Difficulty:** {topic['difficulty']} • **Stage:** {topic['stage']}\n**Lesson ID:** `{topic['id']}`",
        color=colors.get(section, discord.Color.blurple()),
    )
    embed.set_footer(text=f"{status_text} • Lesson {number}/{total} • Learn → Practice → Mastery → Apply")
    embed.add_field(name="🧭 Step-by-step", value=guided_next_step(section, status, mastery), inline=False)

    if section == "overview":
        embed.add_field(name="🎯 Learning objectives", value=lesson_objective(topic, lang), inline=False)
        embed.add_field(name="💡 Why this matters", value=topic.get("why_it_matters", topic["description"]), inline=False)
        embed.add_field(name="📌 Core idea", value=topic["description"], inline=False)
        embed.add_field(name="📚 Important terminology", value=" • ".join(f"`{x}`" for x in topic["terminology"]), inline=False)
        embed.add_field(name="🏆 Your mastery", value=mastery_line(mastery), inline=False)
    elif section == "learn":
        embed.add_field(name="📖 Explanation", value=topic["explanation"], inline=False)
        embed.add_field(name="🔑 Key ideas", value="\n".join(f"• {x}" for x in topic["beginner_tips"]), inline=False)
        embed.add_field(name="⚠️ Common mistakes", value="\n".join(f"• {x}" for x in topic["common_mistakes"]), inline=False)
        embed.add_field(name="🧠 Self-check", value="\n".join(f"• {x}" for x in topic.get("learning_checks", [])), inline=False)
        embed.add_field(name="➡️ Next step", value="Finish the explanation, then click **💻 Example**.", inline=False)
    elif section == "example":
        code = clean_code(topic["example1"])
        if len(code) > 2200: code = code[:2200] + "\n// ... shortened for Discord"
        embed.add_field(name="💻 Example 1 — Worked code", value=f"```{code_language(language)}\n{code}\n```", inline=False)
        embed.add_field(name="🔎 Syntax breakdown", value="\n".join(f"**{i}.** {x}" for i,x in enumerate(topic["syntax_breakdown"],1))[:3900], inline=False)
        embed.add_field(name="🧩 Example explanation", value=topic["example1_explanation"], inline=False)
        code2=clean_code(topic["example2"])
        embed.add_field(name="💡 Example 2 — Change the idea", value=f"```{code_language(language)}\n{code2[:2200]}\n```", inline=False)
        embed.add_field(name="🔁 Transfer task", value=topic["example2_explanation"], inline=False)
    elif section == "practice":
        embed.add_field(name="🧪 Mini exercise", value=topic["exercise"], inline=False)
        embed.add_field(name="🛠️ Practice problem", value=topic["practice_problem"], inline=False)
        embed.add_field(name="📤 Expected output", value=topic["expected_output"], inline=False)
        embed.add_field(name="💡 Hint", value=topic["hint"], inline=False)
        embed.add_field(name="🌱 Beginner tips", value="\n".join(f"• {x}" for x in topic["beginner_tips"]), inline=False)
        embed.add_field(name="🧭 Guided practice", value="\n".join(topic.get("guided_practice", [])), inline=False)
        embed.add_field(name="🧑‍💻 Independent practice", value=topic.get("independent_practice", "Complete the independent task."), inline=False)
        embed.add_field(name="🐛 Debug task", value=topic.get("debug_task", "Diagnose a topic-specific mistake."), inline=False)
        tests = topic.get("test_cases", [])
        test_text = "\n".join(f"• **{t['name']}:** {t['input']} → {t['expected']}" for t in tests[:3])
        embed.add_field(name="🧪 Test contract", value=test_text[:3900], inline=False)
    elif section == "check":
        embed.add_field(name="🧠 Lesson-specific mastery", value="This mastery check tests five different skills using this lesson: concept, syntax, code reading, debugging, and application.", inline=False)
        embed.add_field(name="📊 Current result", value=mastery_line(mastery), inline=False)
        embed.add_field(name="📈 Passing rule", value="Answer at least **4 of 5** questions correctly. The check covers five different skill types.", inline=False)
        embed.add_field(name="🛠️ Demonstration", value="After studying the questions, use **🧪 Mini Challenge** to demonstrate the lesson skill with your own code. For lessons where automated tests are available, the runner should be used before treating the skill as demonstrated.", inline=False)
        embed.add_field(name="🔁 Remediation", value=topic.get("review_plan", {}).get("failed_mastery", "Review missed skills, redo practice, and retry."), inline=False)
    else:
        embed.add_field(name="📝 Summary", value=topic["summary"], inline=False)
        embed.add_field(name="🏁 Completion rule", value="Pass the lesson mastery check, then complete the lesson to unlock the next topic.", inline=False)
        embed.add_field(name="🚀 Apply it", value=topic["extension"], inline=False)
        embed.add_field(name="➡️ Next lesson", value=topic["next_lesson"], inline=False)
    return embed


class LessonQuizView(discord.ui.View):
    """Five-part mastery check that tests more than recognition.

    Each attempt covers core knowledge, syntax/usage, code reading, debugging,
    and application. Answer choices are shuffled per attempt so the student
    cannot memorize the position of the correct answer.
    """

    def __init__(self, language: str, topic: dict):
        super().__init__(timeout=600)
        self.language = language
        self.topic = topic
        self.questions = lesson_questions(topic, language)
        self._shuffle_options()
        self.index = 0
        self.score = 0
        self.results = []
        self._render()

    def _shuffle_options(self):
        rng = random.SystemRandom()
        for question in self.questions:
            correct_text = question["options"][question["answer"]]
            pairs = list(enumerate(question["options"]))
            rng.shuffle(pairs)
            question["options"] = [text for _, text in pairs]
            question["answer"] = question["options"].index(correct_text)

    def _render(self):
        for child in list(self.children):
            self.remove_item(child)

        question = self.questions[self.index]
        options = question["options"]
        select = discord.ui.Select(
            placeholder="Choose the best answer…",
            min_values=1,
            max_values=1,
            row=0,
            options=[
                discord.SelectOption(
                    # Discord truncates long select labels in the client. Keep
                    # the menu readable and show each complete option in the embed.
                    label=f"Choice {'ABCD'[idx]}",
                    value=str(idx),
                    description="Read the full choice in the message above",
                )
                for idx, option in enumerate(options)
            ],
        )

        async def on_select(interaction: discord.Interaction):
            await self._handle_answer(interaction, int(select.values[0]))

        select.callback = on_select
        self.add_item(select)

    def _progress_text(self):
        return " • ".join(
            f"{q['category']}: {'✓' if result is True else '—'}"
            for q, result in self.results
        )

    async def _handle_answer(self, interaction: discord.Interaction, selected: int):
        await interaction.response.defer()
        question = self.questions[self.index]
        options = question["options"]
        answer = question["answer"]

        for child in self.children:
            child.disabled = True

        correct = selected == answer
        if correct:
            self.score += 1
            result = f"✅ **Correct!** {question['explanation']}"
        else:
            result = (
                f"❌ **Not quite.** The correct answer is **{options[answer]}**. "
                f"{question['explanation']}"
            )
        self.results.append((question, correct))
        self.index += 1

        if self.index < len(self.questions):
            self._render()
            next_question = self.questions[self.index]
            embed = discord.Embed(
                title=f"🧠 Mastery Check • {self.topic['title']}",
                description=(
                    f"{result}\n\n"
                    f"**Question {self.index + 1}/5** • `{next_question['category']}`\n"
                    f"{next_question['question']}"
                ),
                color=discord.Color.gold(),
            )
            for option_index, option_text in enumerate(next_question["options"]):
                embed.add_field(
                    name=f"Choice {'ABCD'[option_index]}",
                    value=option_text[:1024],
                    inline=False,
                )
            embed.add_field(
                name="📊 Progress",
                value=f"**{self.score}/{self.index}** correct so far",
                inline=True,
            )
            embed.add_field(
                name="🎯 Passing rule",
                value="**4/5** correct",
                inline=True,
            )
            await interaction.edit_original_response(embed=embed, view=self)
            return

        passed = self.score >= 4
        mastery = await record_mastery(
            interaction.user.id,
            self.language,
            self.topic["id"],
            self.score,
            passed,
            [q["category"] for q, ok in self.results if not ok],
        )

        category_lines = []
        for question, correct_answer in self.results:
            mark = "✅" if correct_answer else "❌"
            category_lines.append(f"{mark} **{question['category']}**")
        breakdown = "\n".join(category_lines)

        if passed:
            today = manila_today()

            def reward_operation(conn):
                awards = []
                mastery_claim = conn.execute(
                    "UPDATE lesson_mastery SET xp_awarded=1 WHERE user_id=? AND language=? AND topic_id=? AND xp_awarded=0",
                    (interaction.user.id, self.language, self.topic["id"]),
                )
                if mastery_claim.rowcount == 1:
                    awards.append(_add_xp_in_transaction(
                        conn, interaction.user.id, interaction.user.display_name, 15,
                        f"Passed {self.language.upper()} lesson mastery check", today,
                    ))

                completion_xp = _complete_lesson_in_transaction(
                    conn, interaction.user.id, interaction.user.display_name,
                    self.language, self.topic["id"], today,
                )
                if completion_xp is not None:
                    awards.append(completion_xp)
                return awards

            xp_results = await db.run_transaction(reward_operation)
            for xp_result in xp_results:
                await _publish_xp_result(interaction.user.id, interaction.guild, xp_result)
            await sync_progress(interaction.user.id, self.language)
            await award_badge(interaction.user.id, "first_steps", interaction.guild)
            title = "🎉 Mastery Passed — Lesson Complete!"
            desc = (
                f"**{self.score}/5** correct — you passed.\n\n"
                "You demonstrated knowledge, code-reading, debugging, and application skills.\n\n"
                "➡️ **Next:** Click **➡️ Next Lesson** to continue."
            )
            color = discord.Color.green()
        else:
            missed = [q["category"] for q, ok in self.results if not ok]
            title = "🔁 Mastery Not Passed — Review the Weak Areas"
            desc = (
                f"**{self.score}/5** correct. You need **4/5** to pass.\n\n"
                f"📌 **Review:** {', '.join(missed) if missed else 'the lesson'}\n\n"
                "➡️ **Next:** Click **📖 Learn** to review, then **🧪 Practice**, "
                "then **🧠 Mastery Check** again."
            )
            color = discord.Color.orange()

        embed = discord.Embed(title=title, description=desc, color=color)
        embed.add_field(name="📋 Skill breakdown", value=breakdown, inline=False)
        embed.add_field(name="💬 Last question feedback", value=result, inline=False)
        embed.set_footer(
            text=f"Best score: {mastery['best_score']}/5 • Attempts: {mastery['attempts']} • Review due: {mastery['review_due_at'] or 'later'}"
        )

        status = await get_status(interaction.user.id, self.language, self.topic["id"])
        lesson_view = LessonView(self.language, self.topic["id"], status)
        lesson_view.section = "check"
        await interaction.edit_original_response(embed=embed, view=lesson_view)

class LessonView(discord.ui.View):
    def __init__(self, language: str, topic_id: str, status: str = "unlocked"):
        super().__init__(timeout=1800)
        self.language = language
        self.topic_id = topic_id
        self.status = status
        self.section = "overview"
        self._set_buttons()

    def _set_buttons(self):
        for child in self.children:
            child.disabled = False
        # Completion is gated by the mastery check.
        mastery_button = getattr(self, "mastery_button", None)
        complete = getattr(self, "complete_button", None)
        if mastery_button:
            mastery_button.label = "\U0001f9e0 Mastery Check"
        if complete:
            complete.disabled = self.status != "completed"
            complete.label = "\u2705 Completed" if self.status == "completed" else ("\U0001f4d6 Review Only" if self.status == "review" else "\U0001f512 Pass Check First")
        curriculum = curriculum_for(self.language)
        index = next((i for i, t in enumerate(curriculum) if t["id"] == self.topic_id), -1)
        previous_button = getattr(self, "previous_lesson_button", None)
        if previous_button:
            previous_button.disabled = index <= 0
        next_button = getattr(self, "next_lesson_button", None)
        if next_button:
            next_button.disabled = self.status != "completed" or index < 0 or index >= len(curriculum) - 1

    async def refresh(self, interaction: discord.Interaction):
        curriculum = curriculum_for(self.language)
        topic = next((t for t in curriculum if t["id"] == self.topic_id), None)
        if not topic:
            await interaction.response.send_message("\u274c Lesson not found.", ephemeral=True)
            return
        self.status = await get_status(interaction.user.id, self.language, self.topic_id)
        if self.status == "locked":
            await interaction.response.send_message("\U0001f512 Complete the previous lesson first.", ephemeral=True)
            return
        mastery = await get_mastery(interaction.user.id, self.language, self.topic_id)
        # Completion is allowed only after the mastery check has passed.
        if self.status == "unlocked" and mastery and mastery["passed"]:
            self.complete_button.disabled = False
            self.complete_button.label = "\u2705 Complete Lesson"
        else:
            self.complete_button.disabled = self.status != "completed" and self.status != "unlocked"
            self.complete_button.label = "\u2705 Completed" if self.status == "completed" else ("\U0001f4d6 Review Only" if self.status == "review" else "\U0001f512 Pass Check First")
        await interaction.response.edit_message(embed=lesson_embed(self.language, topic, self.section, self.status, mastery), view=self)

    @discord.ui.button(label="\U0001f3af Overview", style=discord.ButtonStyle.primary, row=0)
    async def overview(self, interaction, button):
        self.section = "overview"
        await self.refresh(interaction)

    @discord.ui.button(label="\U0001f4d6 Learn", style=discord.ButtonStyle.primary, row=0)
    async def learn(self, interaction, button):
        self.section = "learn"
        await self.refresh(interaction)

    @discord.ui.button(label="\U0001f4bb Example", style=discord.ButtonStyle.secondary, row=0)
    async def example(self, interaction, button):
        self.section = "example"
        await self.refresh(interaction)

    @discord.ui.button(label="\U0001f9ea Practice", style=discord.ButtonStyle.success, row=0)
    async def practice(self, interaction, button):
        self.section = "practice"
        await self.refresh(interaction)

    @discord.ui.button(label="\U0001f9e0 Mastery Check", style=discord.ButtonStyle.primary, row=1)
    async def mastery_button(self, interaction, button):
        # Acknowledge the button immediately so Discord never shows
        # "This interaction failed" while the mastery view is being built.
        await interaction.response.defer()
        topic = next((t for t in curriculum_for(self.language) if t["id"] == self.topic_id), None)
        if not topic:
            await interaction.edit_original_response(content="\u274c Lesson not found.", embed=None, view=None)
            return
        questions = lesson_questions(topic, self.language)
        first_question = questions[0]
        embed = discord.Embed(
            title=f"🧠 Mastery Check • {topic['title']}",
            description=(
                f"**Question 1/5** • `{first_question['category']}`\n"
                f"{first_question['question']}\n\n"
                "Choose the matching answer from the dropdown below. "
                "Full answer choices are listed here. You need **4/5** to pass."
            ),
            color=discord.Color.gold(),
        )
        for option_index, option_text in enumerate(first_question["options"]):
            embed.add_field(
                name=f"Choice {'ABCD'[option_index]}",
                value=option_text[:1024],
                inline=False,
            )
        await interaction.edit_original_response(content=None, embed=embed, view=LessonQuizView(self.language, topic))

    @discord.ui.button(label="\U0001f504 Check Status", style=discord.ButtonStyle.secondary, row=1)
    async def status_button(self, interaction, button):
        self.section = "check"
        await self.refresh(interaction)

    @discord.ui.button(label="\U0001f512 Pass Check First", style=discord.ButtonStyle.success, row=2)
    async def complete_button(self, interaction, button):
        await interaction.response.defer()
        await sync_progress(interaction.user.id, self.language)
        today = manila_today()

        def operation(conn):
            mastery = conn.execute(
                "SELECT best_score,passed FROM lesson_mastery WHERE user_id=? AND language=? AND topic_id=?",
                (interaction.user.id,self.language,self.topic_id),
            ).fetchone()
            if not mastery or not mastery["passed"]:
                return "not_mastered", None, None
            status_row = conn.execute(
                "SELECT status FROM user_progress WHERE user_id=? AND language=? AND topic_id=?",
                (interaction.user.id,self.language,self.topic_id),
            ).fetchone()
            if not status_row or status_row["status"] in ("locked", "review"):
                return "locked", None, mastery
            xp_result = _complete_lesson_in_transaction(
                conn, interaction.user.id, interaction.user.display_name,
                self.language, self.topic_id, today,
            )
            if xp_result is None:
                return "already_completed", None, mastery
            return "completed", xp_result, mastery

        outcome, xp_result, mastery = await db.run_transaction(operation)
        if outcome != "completed":
            message = {
                "not_mastered": "Pass the **Mastery Check** with at least 4/5 first.",
                "locked": "This lesson is locked or review-only. Complete the earlier lesson first.",
                "already_completed": "This lesson is already complete. No extra XP was awarded.",
            }[outcome]
            await interaction.followup.send(message,ephemeral=True)
            return

        _, leveled, level, streak = await _publish_xp_result(interaction.user.id, interaction.guild, xp_result)
        await award_badge(interaction.user.id, "first_steps", interaction.guild)
        await sync_progress(interaction.user.id, self.language)
        curriculum = curriculum_for(self.language)
        index = next(i for i, t in enumerate(curriculum) if t["id"] == self.topic_id)
        self.status = "completed"
        self.section = "check"
        self._set_buttons()
        if index == len(curriculum) - 1:
            next_text = "\U0001f3c6 **Track complete!** You can now claim your certificate."
        else:
            next_text = f"\u27a1\ufe0f **Next lesson:** {curriculum[index + 1]['title']}"
        embed = discord.Embed(
            title="\U0001f389 Lesson Complete!",
            description=f"You completed **{curriculum[index]['title']}**.\n\n\u2b50 **+20 XP** for completion\n\U0001f9e0 **Mastery:** {mastery['best_score']}/5\n\U0001f525 Streak: **{streak} day(s)**\n\n{next_text}",
            color=discord.Color.green(),
        )
        if leveled:
            embed.add_field(name="\U0001f38a Level Up", value=f"You reached **Level {level}**!", inline=False)
        embed.add_field(name="\U0001f4a1 Keep the momentum", value="Open the next lesson when you're ready. You do not need to rush; consistency matters more than speed.", inline=False)
        embed.set_footer(text="Learn \u2192 Practice \u2192 Master \u2192 Apply")
        await interaction.edit_original_response(embed=embed, view=self)

    @discord.ui.button(label="\U0001f3af Mini Challenge", style=discord.ButtonStyle.success, row=2)
    async def mini_challenge(self, interaction, button):
        topic = next((t for t in curriculum_for(self.language) if t["id"] == self.topic_id), None)
        if not topic:
            await interaction.response.send_message("\u274c Lesson not found.", ephemeral=True)
            return
        embed = discord.Embed(
            title=f"\U0001f3af Mini Challenge \u2022 {topic['title']}",
            description=topic.get("exercise", "Apply the lesson concept in a small program."),
            color=discord.Color.green(),
        )
        embed.add_field(name="\U0001f4cc Rules", value="Solve it yourself first. You may use the lesson notes, but do not copy the worked example unchanged.", inline=False)
        embed.set_footer(text="AI feedback is coaching only and does not affect your official score.")
        await interaction.response.send_message(embed=embed, view=MiniChallengeView(self.language, topic), ephemeral=True)

    @discord.ui.button(label="\U0001f41b Debugging Coach", style=discord.ButtonStyle.primary, row=2)
    async def debugging_coach(self, interaction, button):
        topic = next((t for t in curriculum_for(self.language) if t["id"] == self.topic_id), None)
        if not topic:
            await interaction.response.send_message("\u274c Lesson not found.", ephemeral=True)
            return
        await interaction.response.send_modal(DebugCodeModal(self.language, topic))

    @discord.ui.button(label="\U0001f50e Review My Code", style=discord.ButtonStyle.secondary, row=2)
    async def review_code(self, interaction, button):
        topic = next((t for t in curriculum_for(self.language) if t["id"] == self.topic_id), None)
        if not topic:
            await interaction.response.send_message("\u274c Lesson not found.", ephemeral=True)
            return
        await interaction.response.send_modal(ReviewCodeModal(self.language, topic))

    @discord.ui.button(label="\u2b05\ufe0f Previous Lesson", style=discord.ButtonStyle.secondary, row=3, disabled=True)
    async def previous_lesson_button(self, interaction, button):
        await interaction.response.defer(ephemeral=True, thinking=True)
        curriculum = curriculum_for(self.language)
        index = next((i for i, t in enumerate(curriculum) if t["id"] == self.topic_id), -1)
        if index <= 0:
            await interaction.edit_original_response(content="This is the first lesson in the track.", embed=None, view=None)
            return
        previous_topic = curriculum[index - 1]
        statuses = await sync_progress(interaction.user.id, self.language)
        if statuses.get(previous_topic["id"]) == "locked":
            await interaction.edit_original_response(content="\u274c The previous lesson is unavailable.", embed=None, view=None)
            return
        await open_lesson(interaction, self.language, previous_topic["id"])

    @discord.ui.button(label="\u27a1\ufe0f Next Lesson", style=discord.ButtonStyle.primary, row=3, disabled=True)
    async def next_lesson_button(self, interaction, button):
        await interaction.response.defer(ephemeral=True, thinking=True)
        curriculum = curriculum_for(self.language)
        index = next((i for i, t in enumerate(curriculum) if t["id"] == self.topic_id), -1)
        if index < 0 or index + 1 >= len(curriculum):
            await interaction.edit_original_response(content="\U0001f3c6 You reached the end of this track. Use `/certificate` when eligible.", embed=None, view=None)
            return
        next_topic = curriculum[index + 1]
        statuses = await sync_progress(interaction.user.id, self.language)
        if statuses.get(next_topic["id"]) == "locked":
            await interaction.edit_original_response(content="\U0001f512 Complete this lesson first.", embed=None, view=None)
            return
        await open_lesson(interaction, self.language, next_topic["id"])


async def open_lesson(interaction: discord.Interaction, language: str, topic_id: str):
    # Always acknowledge before database/progress work so Discord's 3-second
    # initial-response deadline is not exceeded. Callers may have deferred already.
    if not interaction.response.is_done():
        await interaction.response.defer(ephemeral=True, thinking=True)

    curriculum = curriculum_for(language)
    topic = next((t for t in curriculum if t["id"] == topic_id), None)
    if not topic:
        await interaction.edit_original_response(content="\u274c Lesson not found.", embed=None, view=None)
        return
    statuses = await sync_progress(interaction.user.id, language)
    status = statuses.get(topic_id, "locked")
    if status == "locked":
        await interaction.edit_original_response(
            content="\U0001f512 This lesson is locked. Complete the previous lesson first.",
            embed=None,
            view=None,
        )
        return
    mastery = await get_mastery(interaction.user.id, language, topic_id)
    await interaction.edit_original_response(
        content=None,
        embed=lesson_embed(language, topic, "overview", status, mastery),
        view=LessonView(language, topic_id, status),
    )
