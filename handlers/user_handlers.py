import html
from aiogram import F, types
from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command
from filters.basefilters import IsAdmin
from functions import add_user, get_users_money
from handlers.admin_handlers import admin_command, start_command2, statistic_callback, send_callback
from keyboards import start_command_keyboard, profile_keyboard

dp = Dispatcher()


async def start_command(message: types.Message):
    await message.answer(
        f"Привет, <b>{html.escape(message.from_user.full_name)}</b>!\nЯ бот учета финансов. Я помогу тебе разобраться в твоих финансовых делах 😊.",
        reply_markup=start_command_keyboard,
    )
    await add_user(
        message.from_user.id,
        message.from_user.full_name,
        message.from_user.username,
        money=0,
    )


async def profile(call: types.CallbackQuery):
    money = await get_users_money(user_id=int(call.from_user.id))
    await call.message.answer(
        text=f"Выберите вариант из списка ниже. Ваш баланс: {money}",
        reply_markup=profile_keyboard,
    )


def register_user_messages(dp: Dispatcher):
    dp.message.register(start_command, CommandStart())
    dp.callback_query.register(profile, F.data == "start")
    dp.message.register(admin_command, Command("admin"), IsAdmin())
    dp.callback_query.register(statistic_callback, F.data == "statistic", IsAdmin())
    dp.callback_query.register(send_callback, F.data == 'sendtoall', IsAdmin())
    dp.callback_query.register(start_command2, F.data == "menu")
