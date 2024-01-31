from aiogram import Bot, Dispatcher, types
from asyncio import run
from aiogram.types import BotCommand
from aiogram.filters import Command
from functions import start_command_answer, help_command_answer, new_command_answer, stop_command_answer, newApplication_name_answer, newApplication_age_answer, newApplication_phone_answer,newApplication_job_answer,newApplication_goal_answer, newApplication_verify_answer
from states import newApplication
dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message('admin_id', "Bot Ishga tushdi! ✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message('admin_id', "Bot ishdan to'xtadi! ❌")


async def start():

    dp.startup.register(startup_answer)
    
    dp.message.register(start_command_answer,Command("start") )
    dp.message.register(help_command_answer,Command("help") )
    dp.message.register(new_command_answer,Command("new") )
    dp.message.register(stop_command_answer,Command("stop") )
    dp.message.register(newApplication_name_answer,newApplication.name )
    dp.message.register(newApplication_age_answer,newApplication.age )
    dp.message.register(newApplication_phone_answer,newApplication.phone )
    dp.message.register(newApplication_job_answer,newApplication.job )
    dp.message.register(newApplication_goal_answer,newApplication.goal )
    dp.message.register(newApplication_verify_answer,newApplication.verify )
    dp.shutdown.register(shutdown_answer)
    bot = Bot("bot_token")
    await bot.set_my_commands([
        BotCommand(command="/new", description="Yangi ariza yuborish!"),
        BotCommand(command="/stop", description="Arizani Bekor qilish!"),
        BotCommand(command="/help", description="Botdan foydalanish uchun yordam!")
    ])


    await dp.start_polling(bot)
run(start())