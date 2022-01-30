from data import config, models
from loader import redis, fsm_storage


async def startup(dp):
    pass


async def shutdown(dp):
    if config.REDIS_URL:
        redis.close()
    if config.DATABASE_URL:
        models.db.database_connect.close()
    fsm_storage.close()

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown, skip_updates=True)
