from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from states import newApplication
async def start_command_answer(message: Message, bot: Bot):
    await message.answer("Assalomu Alaykum, botdan foydalanishni bilmasangiz /help buyrug'ini yuboring")

async def help_command_answer(message: Message, bot: Bot):
    matn = """Botdan Foydalanish:
    /new - yangi ariza yuborish
    /stop - joriy yuborilayotkan arizani bekor qilish!
    """
    await message.answer(matn)

async def new_command_answer(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Ism familya yuboring!")
    await state.set_state(newApplication.name)

async def stop_command_answer(message: Message, bot: Bot, state: FSMContext):
    this_state = await state.get_state()
    if(this_state == "None"): await message.answer("Bekor qilish uchun ariza mavjud emas!")
    else:
        await state.clear()
        await message.answer("Joriy ariza bekor qilindi!")

async def newApplication_name_answer(message: Message, bot: Bot, state: FSMContext):
    if len(message.text.split()) == 2:
        name = message.text.strip()  # Remove leading/trailing whitespaces
        if isinstance(name, str):
            await state.update_data(name=name)
            await message.answer(f"Ism-familya qabul qilindi. \n\n{name}")
            await message.answer("Yoshingizni yuboring!")
            await state.set_state(newApplication.age)
        else:
            await message.answer("Notog'ri ism-familyada raqam bo'lishi mumkun emas")
    else:
        await message.answer("Menga ism familyani to'liq yuboring!")

async def newApplication_age_answer(message: Message, bot: Bot, state: FSMContext):
    if message.text.isdigit():
        if int(message.text) < 150 and int(message.text) > 7:
            await state.update_data(age=message.text)
            await message.answer(f"Yoshingiz qabul qilindi\n\n{message.text}")
            await message.answer("Telefon raqamingizni kiriting!")
            await state.set_state(newApplication.phone)
        elif int(message.text) >= 150: await message.answer("150 dan kichik bolgan yosh kiritilsin")
        else: await message.answer("7 yoshdan kattalar ariza bera oladi")
    else: await message.answer("Notog'ri yosh!")
            

async def newApplication_phone_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer(F"Telefon raqamingiz qabul qilindi\n\n{message.text}")
    await message.answer("Kasbingiz nima?")
    await state.set_state(newApplication.job)

async def newApplication_job_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(job=message.text)
    await message.answer(F"Kasbingiz qabul qilindi\n\n{message.text}")
    await message.answer("Maqsadingiz nima?")
    await state.set_state(newApplication.goal)

async def newApplication_goal_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(goal=message.text)
    await message.answer(F"Maqsadingiz qabul qilindi\n\n{message.text}")
    
    data = await state.get_data()
    
    ariza = (f"Ariza beruvchi: { data.get('name')}\n"
             f"Username: @{message.from_user.username}\n"
             f"Yoshi: {data.get('age')}\n"
             f"Telefon raqam: {data.get('phone')}\n"
             f"Kasbi: {data.get('job')}\n"
             f"Maqsadi: {data.get('goal')}\n"
             )

    await message.answer(f"Arizani yuboraberaymi?\n\n{ariza}\n\n Ha yoki /stop deb javob bering.")
    await state.set_state(newApplication.verify)

async def newApplication_verify_answer(message: Message, bot: Bot, state: FSMContext):
    if message.text.lower() == "ha":
        data = await state.get_data()
    
        ariza = (f"Ariza beruvchi: { data.get('name')}\n"
                f"Yoshi: {data.get('age')}\n"
                f"Username: @{message.from_user.username}\n"
                f"Telefon raqam: {data.get('phone')}\n"
                f"Kasbi: {data.get('job')}\n"
                f"Maqsadi: {data.get('goal')}\n"
                )
        await bot.send_message('admin_id', f"Yangi Ariza:\n\n{ariza}")
        await message.answer("Arizangiz qabul qilindi. ✅")
        await state.clear()
    else: await message.answer("Yo menga ha deng yoki /stop buyrug'ini yuboring!")