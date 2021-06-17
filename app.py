async def startup(dp):
    pass


async def shutdown(dp):
    pass

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown, skip_updates=True)
