# Telegram-Notify

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
![Python application](https://github.com/rexdivakar/Telegram-Notifly/workflows/Python%20application/badge.svg)
![Upload Python Package](https://github.com/rexdivakar/Telegram-Notifly/workflows/Upload%20Python%20Package/badge.svg)


<p align="center">
<img src="others\bot.png" width="200" alt="Logo">

## Table of Contents
* [About the package](#about-the-package)
  * [Built With](#built-with)
* [Install the package](#install-the-package)
  * [Working of the tool](#working-of-the-tool)
  * [Prerequisites](#prerequisites)
* [Contributing](#contributing)

## About the package
Telegram Bot to push notifications during an event trigger.

## Built With
* [Python][1]

## Install the package
Run the following terminal commands to install the package on the given distros.
* Termux :
```
pkg install python3 
```
```
pip3 install notifly
```
* Ubuntu/Debian
```
sudo apt install python3-pip
```
```
pip3 install notifly
```
* Arch
```
sudo pacman -S python3-pip
```
```
pip3 install notifly
```
***This may take a while depending on the network speed.***
### Prerequisites
* Python3<br>
It is preinstalled in Ubuntu 20.04. To check the version use command :
```
python3 --version
```
If it is not preinstalled for some reason, proceed [here][4] and download as per requirement.

Run the following command in terminal to download the required packags for running the tool locally : 
* Using requirements file :
```
pip3 install -r requirements.txt
```
* Directly download :
```
pip3 install requests==2.20.0
```
### Working of the tool
To see how the tool works, create a [telegram bot][2] and run the _sample code_.
1. Creating the [telegram bot][0]
   1. Open Telegram messenger, sign in to your account or create a new one.
   1. Enter _@Botfather_ in the search tab and choose this bot.<br>*Note, official Telegram bots have a blue checkmark beside their name*
   1. Click _Start_ to activate BotFather bot.
   1. Choose or type _/newbot_ and send it.
   1. Choose a name for the bot, the bot can be found by its username in searches. The username must be unique and end with the word _bot_.
   1. After choosing a suitable name for the bot, the bot is created. We receive a message with a link to the bot _t.me/<bot_username>_, recommendations to set up a profile picture, description, and a list of commands to manage your new bot.
1. Run sample code
```python
from telegram import notifly

bot=notifly.BotHandler('1317654102:AAHhNLXy_vqJWDEf0Hu7svfw-DkVFmQuUG0')
text = input("Enter text message : ")
print(bot.send_message(text))
opt_image = input("Do you want to send image ?")
if(opt_image=='y' or opt_image=='Y'):
    img_path = input("Enter full image path : ")
    bot.send_image(img_path)
```
Enter the _bot token_ here.
```
bot=notifly.BotHandler('bot_token')
```
## Contributing
1. Fork the Project
1. Create your Feature Branch (git checkout -b feature/mybranch)
1. Commit your Changes (git commit -m 'Add something')
1. Push to the Branch (git push origin feature/mybranch)
1. Open a Pull Request

*Follow the given commands or use the amazing GitHub GUI*
<br>**Happy Contributing** :smiley:

[contributors-shield]: https://img.shields.io/github/contributors/rexdivakar/Telegram-Notifly.svg?style=flat-square
[contributors-url]: https://github.com/rexdivakar/Telegram-Notifly/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/rexdivakar/Telegram-Notifly.svg?style=flat-square
[forks-url]: https://github.com/rexdivakar/Telegram-Notifly/network/members
[stars-shield]: https://img.shields.io/github/stars/rexdivakar/Telegram-Notifly.svg?style=flat-square
[stars-url]: https://github.com/rexdivakar/Telegram-Notifly/stargazers
[issues-shield]: https://img.shields.io/github/issues/rexdivakar/Telegram-Notifly.svg?style=flat-square
[issues-url]: https://github.com/rexdivakar/Telegram-Notifly/issues
[license-shield]: https://img.shields.io/github/license/rexdivakar/Telegram-Notifly.svg?style=flat-square
[license-url]: https://github.com/rexdivakar/Telegram-Notifly/blob/master/LICENSE.txt
[0]:https://core.telegram.org/bots
[1]:https://www.python.org/
[2]:https://telegram.org/blog/bot-revolution
[4]:https://www.python.org/downloads/
