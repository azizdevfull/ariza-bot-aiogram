from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext

async def start_command_answer(message: Message, bot: Bot):
    await message.answer("Assalomu Alaykum, botdan foydalanishni bilmasangiz /help buyrug'ini yuboring")

async def help_command_answer(message: Message, bot: Bot):
    matn = """Botdan Foydalanish:
    /new - yangi ariza yuborish
    /stop - joriy yuborilayotkan arizani bekor qilish!
    """
    await message.answer(matn)
