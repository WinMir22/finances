import html
from aiogram import F, types
from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command
from filters.basefilters import IsAdmin
from functions import add_user, get_users_money 

dp = Dispatcher()


async def start_command(message: types.Message):
    kb = [
        [
            types.InlineKeyboardButton(
                text="Начать пользование ботом", callback_data="start"
            )
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer(
        f"Привет, <b>{html.escape(message.from_user.full_name)}</b>!\nЯ бот учета финансов. Я помогу тебе разобраться в твоих финансовых делах 😊.",
        reply_markup=keyboard,
    )
    await add_user(
        message.from_user.id,
        message.from_user.full_name,
        message.from_user.username,
        0,
    )


async def profile(call: types.CallbackQuery):
    kb = [
        [
            types.InlineKeyboardButton(text="Доход", callback_data="givemoney"),
            types.InlineKeyboardButton(text="Расход", callback_data="getmoney"),
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    money = await get_users_money(user_id=call.message.from_user.id)
    await call.message.answer(text=f'Выберите вариант из списка ниже. Ваш баланс: {money}', reply_markup=keyboard)


async def admin_command(message: types.Message):
    kb = [
        [
            types.InlineKeyboardButton(text="Статистика", callback_data="statistic"),
            types.InlineKeyboardButton(text="Рассылка", callback_data="sendtoall"),
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer("Добро пожаловать в админ панель!", reply_markup=keyboard)


async def statistic_callback(callback: types.CallbackQuery):
    kb = [[types.InlineKeyboardButton(text="В меню", callback_data="menu")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    user_count = await get_user_count()
    await callback.message.edit_text(
        f"Статистика\n\nКоличество пользователей: {user_count}", reply_markup=keyboard
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


def register_user_messages(dp: Dispatcher):
    dp.message.register(start_command, CommandStart())
    dp.callback_query.register(profile, F.data == 'start')
    dp.message.register(admin_command, Command("admin"), IsAdmin())
    dp.callback_query.register(statistic_callback, F.data == "statistic", IsAdmin())
    dp.callback_query.register(start_command2, F.data == "menu")
