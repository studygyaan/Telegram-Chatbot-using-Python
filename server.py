from bot import telegram_bot

mybot = telegram_bot("config.txt")

update_id = None

def make_reply(msg):
	if msg is not None:
		return msg

while True:
	print("...")
	updates = mybot.get_updates(offset=update_id)
	updates = updates["result"]
	if updates:
		for item in updates:
			update_id = item["update_id"]
			try:
				message = item["message"]["text"]
			except:
				message = None
			from_ = item["message"]["from"]["id"]
			reply = make_reply(message)
			mybot.send_message(reply, from_)