import logging
from pathlib import Path

import environ

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.files import JSONStorage
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram_dialog import StartMode, DialogManager, DialogRegistry

from courier import MainSG, dialog
logging.basicConfig(level=logging.INFO)

env = environ.Env()
env.read_env(Path(__file__).resolve().parent.parent / ".env")


#storage = JSONStorage('db.json')
storage = MemoryStorage()
bot = Bot(token=env.str("BOT_TOKEN"))
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)

registry.register(dialog)

@dp.message_handler(commands=["start"])
async def start(m: Message, dialog_manager: DialogManager):
    await m.reply("Привет, я помогаяю курьерам с доставкой."
                        "Нажми кнопку получить заказ, чтобы начать работу")
    await dialog_manager.start(MainSG.root, mode=StartMode.RESET_STACK)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)