from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
import logging
import signal
import ayar
import json
import time
import os
os.system('cls')
PATCH = os.getcwd()

   
bot = Bot(token=ayar.API_TOKEN)
dp = Dispatcher(bot)
end_id = input("Введите номер последнего сообщения который вы хотите удалить:")
while end_id == "":
	end_id = input("Это поле обязательно:")
else:
	print ("nempty")

@dp.message_handler(commands=['del'], commands_prefix='*')
async def acmd(message: types.Message):
     
     
    # end_id = 210750
    while message.message_id > end_id:
        try:
            await bot.delete_message(message.chat.id,message.message_id)
            message.message_id -=1
            print(f"({message.message_id}) Удален")
        except Exception as irr:
               
            print (f"Нет сообщения под номером: {message.message_id}")
            message.message_id -=1
            asyncio.sleep(0.1)

@dp.message_handler(commands=['stop'], commands_prefix='*')
async def acmd(message: types.Message):
	stop()
	exit()
       
        










if __name__ == '__main__':
    try:
        executor.start_polling(dp,skip_updates=True)
    except Exception as irr:
        logging.error("Connection error:"+str(irr))
