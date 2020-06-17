# Connection Monitor Telegram Bot
##### This bot allows to send logs to the specified telegram chat
 
This is simple extendable bot framework to monitor accessibility of the host, VPN status, sending logs

Functionality of this bot can be extended by adding additional scripts or by importing bot to your code and send all the necessary information (for example important logs) directly to your Telegram chat

This bot is not running continuously, it only starts when it is triggered by any event, and sends one single message so you can create one single bot and place required scripts to a separate hosts to monitor different processes.

Any script can be activated by adding it to crontab to repeat it as often as you need.
