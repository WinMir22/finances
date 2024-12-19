from aiogram import types


start_command_kb = [
    [
        types.InlineKeyboardButton(
            text="Начать пользование ботом", callback_data="start"
        )
    ]
]
start_command_keyboard = types.InlineKeyboardMarkup(inline_keyboard=start_command_kb)


profile_kb = [
    [
        types.InlineKeyboardButton(text="Доход", callback_data="givemoney"),
        types.InlineKeyboardButton(text="Расход", callback_data="getmoney"),
    ]
]
profile_keyboard = types.InlineKeyboardMarkup(inline_keyboard=profile_kb)


admin_kb = [
    [
        types.InlineKeyboardButton(text="Статистика", callback_data="statistic"),
        types.InlineKeyboardButton(text="Рассылка", callback_data="sendtoall"),
    ]
]
admin_keyboard = types.InlineKeyboardMarkup(inline_keyboard=admin_kb)


admin_menu_kb = [[types.InlineKeyboardButton(text="В меню", callback_data="menu")]]
admin_menu_keyboard = types.InlineKeyboardMarkup(inline_keyboard=admin_menu_kb)
