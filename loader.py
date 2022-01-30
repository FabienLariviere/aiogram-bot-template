from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aioredis import Redis

from data import config

bot = Bot(token=config.BOT_TOKEN)

if config.REDIS_URL:
    redis = Redis.from_url(config.REDIS_URL)
    fsm_storage = RedisStorage2(redis.connection.host, redis.connection.port, db=0, password=redis.connection.password)
else:
    fsm_storage = MemoryStorage()

dp = Dispatcher(bot, storage=fsm_storage)
