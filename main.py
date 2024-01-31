from aiogram import Bot, Dispatcher, types
from asyncio import run
from aiogram.types import BotCommand
from aiogram.filters import Command
from functions import start_command_answer, help_command_answer
dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(1184193890, "Bot Ishga tushdi! ✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message(1184193890, "Bot ishdan to'xtadi! ❌")


async def start():

    dp.startup.register(startup_answer)
    
    dp.message.register(start_command_answer,Command("start") )
    dp.message.register(help_command_answer,Command("help") )
    
    dp.shutdown.register(shutdown_answer)
    bot = Bot("6803882554:AAH91YHRcmFQQnZmhzy0ZWpRXscZiJBNeV4")
    await dp.start_polling(bot)
    await bot.set_my_commands([
        BotCommand(command="/new", description="Yangi ariza yuborish!"),
        BotCommand(command="/stop", description="Arizani Bekor qilish!"),
        BotCommand(command="/help", description="Botdan foydalanish uchun yordam!")
    ])

run(start())
