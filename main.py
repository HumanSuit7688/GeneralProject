import config
import asyncio
from aiogram import Bot, Dispatcher, types
from Fonetic.Handlers.fonetic import register_handlers_fonetic
from background import keep_alive


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


async def main():
    register_handlers_fonetic(dp)
    await dp.skip_updates()
    await dp.start_polling()


if __name__ == '__main__':
    keep_alive()
    asyncio.run(main())