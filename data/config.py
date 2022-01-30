import os

DATABASE_URL = os.environ.get('DATABASE_URL')
REDIS_URL = os.environ.get('REDIS_URL')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
ADMINS = [admin.strip() for admin in os.environ.get('ADMINS').split(',')]
