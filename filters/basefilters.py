from aiogram.types import TelegramObject
from aiogram.filters import BaseFilter


admin_ids = [6020786260]


class IsAdmin(BaseFilter):
    async def __call__(self, obj: TelegramObject) -> bool:
        return obj.from_user.id in admin_ids
