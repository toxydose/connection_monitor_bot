from subprocess import run, PIPE
from bot import *

message = ''
output = run('dig +short myip.opendns.com @resolver1.opendns.com', shell=True, stdout=PIPE)
ip = output.stdout.decode('utf-8')

if 'IP' in ip:
    message = 'real ip is disclosed'
    bot.send_message(chat_id=CHAT_ID, text=(ip + message))

else:
    if len(ip) < 17 or len(ip) > 8:
        pass

    else:
        message = 'Unknown error while checking IP'
        bot.send_message(chat_id=CHAT_ID, text=message)
