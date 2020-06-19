# Connection Monitor Telegram Bot
### This bot allows to send logs to the specified telegram chat
 
This is simple extendable bot framework to monitor accessibility of the host, VPN status, sending logs

Functionality of this bot can be extended by adding additional scripts or by importing bot to your code and send all the necessary information (for example important logs) directly to your Telegram chat

This bot is not running continuously, it only starts when it is triggered by any event, and sends one single message so you can create one single bot and place required scripts to a separate hosts to monitor different processes.

Any script can be activated by adding it to crontab to repeat it as often as you need.

#### requirements:
- python3

- `sudo python3 -m pip install python-telegram-bot`

#### usage:

 - rename `config.py.sample` to `config.py` and fill all required parameters
 - add the required script to cron `crontab -e`
 For example to check if the VPN is still running for every minute add in crontab the next string:
  `* * * * * python3 ~/connection_monitor_bot/checkvpn.py`

#### checkvpn.py

Checks if the host where script is deployed still connected to VPN. Will not work if VPN does not change your real IP.
If the specified in config.py IP corresponds to the current host IP address script considers that VPN is off and sends an alert.

#### check_alive.py

Checks if the remote host is up based on the requests to SSH interface.


#### logging

You can use this bot to send important logs of your Python3 application
- import bot into your script:

`
from bot import * `

- add this string in every place in your code when you needs to be alerted

`bot.send_message(chat_id=CHAT_ID, text=message)`

`message` variable can be defined before, or specified directly within the logging line
