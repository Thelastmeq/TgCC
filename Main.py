import logging
import os
import requests
import time
import string
import random
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup

env = bool(os.environ.get('env', True))
Token = os.environ.get("Token", True)
Black_list = os.environ.get("Black_list", None)
prefix = "!."


#This is For Config

logging.basicConfig(level=logging.INFO)


#Installing Bot

bot = Bot(token=Token , parse_mode=types.ParseMode.HTML)
disspatcher = Dispatcher(bot)

#Proxies ! 

r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=20&country=all&ssl=all&anonymity=all&simplified=true').text
res = r.partition('\n')[0]

Proxy = {"http":f"http://{res}"}
sessions = requests.session()



#Random Generator ! 

Number = 10
rnd = .join(random.choices(string.ascii_lowercase + string.digits, k=Number))

#----------------------Handlers--------------------------------#

@Dispatcher.message_handler(commands=['start','help'],commands_preifx=prefix)

async def helpcmd(message:types.Message):
	await message.answer_chat_action("Working...")
	await message.reply("How To Use CyberCardsTM cc Checker Bot:\n\nCMD -> .chk cc/month/yy/cvv\n")



@Dispatcher.message_handler(commands=["bin" or "Bin"], command_prefix=prefix)

async def binchk(message:types.Message):
	await message.answer_chat_action("Working...")
	asyncio.sleep(1)

	Bin = message.text[len(".bin"):11]

	if len(Bin):
		return await message.reply("Dont Fuck ME !... Send Bin")

		if not Bin:
			return await message.reply("U Stupid Dont Know How To Fuck Ma Ass... Check Ma Help Bruh !")
		r = requests.get(f"https://bins.ws/search?bins={Bin}&bank=&country=").text
		sxy = BeautifulSoup(r,features="html.parser")
		bro = soup.find("div", {"class":"page"})
		Res = f"""
⋙═══════ ⋆★⋆ ═══════ ⋘
<b>BIN INFO</b>
<code>{k.get_text()[62:]}</code>
Checked By: <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
<b>Owner:</b> @YourDecisions
⋙═══════ ⋆★⋆ ═══════ ⋘
"""
		await message.reply(Res)








if __name__ == '__main__':
    executor.start_polling(Dispatcher, skip_updates=True)


