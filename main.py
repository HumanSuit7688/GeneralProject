import config
import asyncio
from aiogram import Bot, Dispatcher, types
from Fonetic.Handlers.fonetic import register_handlers_fonetic


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


async def main():
    register_handlers_fonetic(dp)
    await dp.skip_updates()
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())