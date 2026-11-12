import asyncio
import logging
from bot.config import Config
from bot.bot import ClassCodeBot
from bot.database import db

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

async def main():
    Config.validate()
    await db.check_schema()
    bot = ClassCodeBot()
    async with bot:
        await bot.start(Config.DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
