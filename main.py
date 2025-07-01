import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

# BOT TOKEN KAAGA HALKAN KU DAR
API_TOKEN = '7132920778:AAEOZTFz4y7NcHWi-w6Xx4k1-v9g8U4ZdYQ'

# Log setting
logging.basicConfig(level=logging.INFO)

# Bot & Dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Dictionary si loo xafido tirada videos ka ee user walba
user_video_counts = {}

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def handle_video(message: Message):
    user_id = message.from_user.id

    # Haddii uusan user-ka horay u jirin, bilaabi count 1
    if user_id not in user_video_counts:
        user_video_counts[user_id] = 1
    else:
        user_video_counts[user_id] += 1

    count = user_video_counts[user_id]import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

# BOT TOKEN KAAGA HALKAN KU DAR
API_TOKEN = '7132920778:AAEOZTFz4y7NcHWi-w6Xx4k1-v9g8U4ZdYQ'

# Log setting
logging.basicConfig(level=logging.INFO)

# Bot & Dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Dictionary si loo xafido tirada videos ka ee user walba
user_video_counts = {}

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def handle_video(message: Message):
    user_id = message.from_user.id

    # Haddii uusan user-ka horay u jirin, bilaabi count 1
    if user_id not in user_video_counts:
        user_video_counts[user_id] = 1
    else:
        user_video_counts[user_id] += 1

    count = user_video_counts[user_id]
