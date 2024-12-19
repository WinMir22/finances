import asyncio
from aiogram import Bot, types
from functions import get_user_count
from keyboards import admin_keyboard, admin_menu_keyboard
from aiogram.fsm.context import FSMContext
from states import AdminState
from functions import get_all_users_id


async def admin_command(message: types.Message):

    await message.answer(
        "Добро пожаловать в админ панель!", reply_markup=admin_keyboard
    )


async def statistic_callback(callback: types.CallbackQuery):
    user_count = await get_user_count()
    await callback.message.edit_text(
        f"Статистика\n\nКоличество пользователей: {user_count}",
        reply_markup=admin_menu_keyboard,
    )


async def send_callback(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(AdminState.newsletter)
    await call.message.edit_text(
        "Вы не поверите, но я поменял ваш state:)\nВведите сообщение для отправки.",
        reply_markup=admin_menu_keyboard,
    )


async def admin_newsletter_step_2(
    message: types.Message, state: FSMContext, bot: Bot
) -> None:
    msg = message.text
    users = await get_all_users_id()
    await state.clear()
    i = 0
    for user in users:
        try:
            await bot.send_message(user, msg)
            i += 1
            await asyncio.sleep(0.3)
        except:
            pass
    user_count = len(users)
    await message.answer(
        f"Рассылка завершена\n\nВсего пользователей: {user_count}\nУдалось отправить: {i}\nНе удалось отправить:{user_count-i}")


async def start_command2(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        "Добро пожаловать в админ панель!", reply_markup=admin_keyboard
    )
