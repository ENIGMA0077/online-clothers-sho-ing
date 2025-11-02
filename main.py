from aiogram import Bot, Dispatcher, F
import os
import logging

import asyncio

from handlers import start_router, user_router, admin_router


TOKEN = '7594715231:AAEfN2Y7OX_MpTyVUWW4DBLlyIq62c6oJWc'

dp = Dispatcher()
# TOKEN = os.getenv('TOKEN')    


async def main():
    bot = Bot(TOKEN)
    
    dp.include_router(start_router)
    dp.include_router(user_router)
    dp.include_router(admin_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

