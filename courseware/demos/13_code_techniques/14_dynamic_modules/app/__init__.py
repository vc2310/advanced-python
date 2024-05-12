import logging
import importlib
import os
from typing import Any

from .core.bot import Bot

print("loading __init__")


class BotFilter(logging.Filter):
    def __init__(self, bot: Bot) -> None:
        self.__bot = bot

    def filter(self, record: Any) -> bool:
        record.bot_name = self.__bot.name
        return True


BOT_NAME = os.environ.get("BOT_NAME", "rigel")

bot_module = importlib.import_module(f"dynamic_modules.bots.{BOT_NAME}")

BotClass = getattr(bot_module, f"{BOT_NAME.capitalize()}Bot")

logger = logging.getLogger(f"{BOT_NAME}_bot")
logger.addFilter(BotFilter(BotClass))
logger.setLevel(logging.DEBUG)

log_handler = logging.FileHandler("bot.log", encoding="utf-8")
log_formatter = logging.Formatter("%(asctime)s:%(bot_name)s:%(message)s")
log_handler.setFormatter(log_formatter)

logger.addHandler(log_handler)
