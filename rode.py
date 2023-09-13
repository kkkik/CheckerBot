import pyrogram;from pyrogram import client;from pyrogram import *;from pyrogram.types import *;import requests,re;from time import sleep;from pyrogram.errors import FloodWait ,BadRequest
info = open("info.txt",'r').read();tok = info.split('\n')[0];idown = info.split('\n')[1]
r = open("user.txt").read()
mk = r.replace("@", "")
o = mk.replace(" ", "")
qq = 0
req = requests.get(f"https://t.me/{o}").text
if "tgme_username_link" not in req:
	print("No")
	v = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- The user is used😡')
	exit("The user is used")
while True:
	for session in open("account.txt","r").read().split("\n"):
		if session != "":
			try:
				if session != " ":
					app = Client("ACC",api_id=24367955,api_hash="df9e7f5217331d03353a8d42e11419fc",session_string=session)
					app.connect()
					try:
						ch = app.create_channel(title="𝐓𝐇𝐄 𝐁𝐄𝐒𝐓 ☠️")
						ch = ch.id
						app.set_chat_username(ch, o)
						app.update_profile(first_name="- 𝐓𝐇𝐄 𝐁𝐄𝐒𝐓 ☠️<\>", bio="ᴄʜ ↬ @apthon | ᴅᴇᴠ ↬ @X_USU  ☠️ ")
						qq+=1
						op = requests.post(f'''https://api.telegram.org/bot{tok}/sendvideo?chat_id={idown}&video=https://telegra.ph/file/3a3fc7aa1b03a4a48c11e.mp4&caption=> Sorry Bot I'm Top 1
new   FLOOD
  UserName: @{o}
  Clicks: {qq}
  Type:  Channel
  BY : @X_USU  🐊''')
						v = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=[ {session} ]')
						app.send_message(ch,f'''> Sorry but I'm the best   ↬ @X_USU ☠️''')
						os.system('screen -S rode -X kill')
  
					except FloodWait as e:
						qq+=1
						ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- Checker [ {qq} ] 
- NumBer : {app.get_me().phone_number}
- Error : {e}''')
						pass
					except BadRequest as e:
						qq+=1
						ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- Checker [ {qq} ]
- User is don't Save ↣ @{o}
- Error ↣ flood''')
					try:
						sleep(int(open("sleep.txt").read()))
					except:
						sleep(2)
			except:
				pass				