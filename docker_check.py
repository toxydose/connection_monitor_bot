from bot import *
from subprocess import run, PIPE

message = 'No running Dockers on ' + HOSTNAME
command = 'docker ps'
output = run(command, shell=True, stdout=PIPE)
response = str(output)
if DOCKER_KEYWORD in response:
	pass
else:
	bot.send_message(chat_id=CHAT_ID, text=message)
