import aiohttp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import API_URL

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    user = message.from_user

    data = {
        "telegram_id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(f"{API_URL}/botusers/create/", json=data) as resp:
                if resp.status == 201:
                    await message.answer(f"Salom, {user.full_name}! Botga xush kelibsiz!")
                elif resp.status == 400:
                    await message.answer(f"Salom, {user.full_name}! Botga xush kelibsiz!")
                else:
                    await message.answer("❌ Serverda xatolik yuz berdi.")
        except Exception as e:
            await message.answer("❌ Backend bilan bog'lanib bo'lmadi.")

