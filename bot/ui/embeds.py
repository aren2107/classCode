import discord

class ColorPalette:
    PRIMARY = discord.Color.from_rgb(88, 101, 242)   # Blurple
    SUCCESS = discord.Color.from_rgb(87, 242, 135)   # Green
    WARNING = discord.Color.from_rgb(254, 231, 92)   # Gold
    DANGER = discord.Color.from_rgb(237, 66, 69)     # Red
    DARK = discord.Color.from_rgb(43, 45, 49)        # Dark Slate

class UIEmbeds:
    @staticmethod
    def standard(title: str, description: str, color: discord.Color = ColorPalette.PRIMARY) -> discord.Embed:
        embed = discord.Embed(title=title, description=description, color=color)
        embed.set_footer(text="ClassCode Platform \u2022 Gemini AI & Code Runner Integrated")
        return embed

    @staticmethod
    def profile(username: str, level: int, title_str: str, xp: int, next_xp: int, cpp_pct: int, java_pct: int, badges: list[str]) -> discord.Embed:
        embed = discord.Embed(title=f"\U0001f464 CLASSCODE PROFILE \u2014 {username}", color=ColorPalette.PRIMARY)
        embed.description = f"**Level {level}** \u2022 `{title_str}`"
        
        bar_len = 10
        filled = int((xp / max(next_xp, 1)) * bar_len)
        bar = "\u2588" * min(filled, bar_len) + "\u2591" * max(0, bar_len - filled)
        embed.add_field(name="\u2b50 XP Progress", value=f"`{bar}` ({xp} / {next_xp} XP)", inline=False)

        cpp_filled = int((cpp_pct / 100) * bar_len)
        cpp_bar = "\u2588" * cpp_filled + "\u2591" * (bar_len - cpp_filled)
        embed.add_field(name="\U0001f7e6 C++ Mastery", value=f"`{cpp_bar}` {cpp_pct}%", inline=True)

        java_filled = int((java_pct / 100) * bar_len)
        java_bar = "\u2588" * java_filled + "\u2591" * (bar_len - java_filled)
        embed.add_field(name="\u2615 Java Mastery", value=f"`{java_bar}` {java_pct}%", inline=True)

        badge_str = " ".join([f"`[{b}]`" for b in badges]) if badges else "None unlocked yet."
        embed.add_field(name="\U0001f3c5 Unlocked Badges", value=badge_str, inline=False)
        embed.set_footer(text="Keep completing quizzes and challenges to level up!")
        return embed
