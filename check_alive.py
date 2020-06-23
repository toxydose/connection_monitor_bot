from subprocess import run, PIPE
import time
from bot import *

message = '_'
command = 'nc ' + IP + ' ' + PORT + ' -w 1'
output = run(command, shell=True, stdout=PIPE)
message = output.stdout.decode('utf-8')
status = False

print(message)
if 'SSH' in message:
    status = True

if status == False:
    time.sleep(3)
    output = run(command, shell=True, stdout=PIPE)
    message = output.stdout.decode('utf-8')
    if 'SSH' in message:
        print()
    else:
        bot.send_message(chat_id=CHAT_ID, text=(REMOTE_HOSTNAME + ' is unreachable ' + message))
