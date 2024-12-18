import asyncio
import configparser
from handlers.handler import register_user_messages
from aiogram import Bot, Dispatcher
import logging
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
dp = Dispatcher()


logger = logging.getLogger(__name__)

config = configparser.ConfigParser()

config.read("config.ini")


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    bot = Bot(token=config.get("Token", "token"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    register_user_messages(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
