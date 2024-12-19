from aiogram import types
from functions import get_user_count
from keyboards import admin_keyboard, admin_menu_keyboard

async def admin_command(message: types.Message):

    await message.answer("Добро пожаловать в админ панель!", reply_markup=admin_keyboard)


async def statistic_callback(callback: types.CallbackQuery):
    user_count = await get_user_count()
    await callback.message.edit_text(
        f"Статистика\n\nКоличество пользователей: {user_count}", reply_markup=admin_menu_keyboard
    )


async def start_command2(callback: types.CallbackQuery):
    kb = [
        [
            types.InlineKeyboardButton(text="Статистика", callback_data="statistic"),
            types.InlineKeyboardButton(text="Рассылка", callback_data="sendtoall"),
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        "Добро пожаловать в админ панель!", reply_markup=keyboard
    )
