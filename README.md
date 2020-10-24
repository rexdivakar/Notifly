# Telegram-Notify
![GitHub issues](https://img.shields.io/github/issues-raw/rexdivakar/telegram-notifly?logo=github&style=for-the-badge)
![Discord](https://img.shields.io/discord/760088481224851476?label=DISCORD&logo=discord&logoColor=green&style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/notifly?logo=github&style=for-the-badge)
![PyPI - Downloads](https://img.shields.io/pypi/dm/notifly?color=green&style=for-the-badge&logo=github)

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/rexdivakar/telegram-notifly/Python%20application?&style=flat-square)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/rexdivakar/telegram-notifly/Upload%20Python%20Package?label=Upload%20Python%20Package&style=flat-square)


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
To see how the tool works, create a [telegram bot][2].
1. ***Creating the [telegram bot][0]***
   1. Open Telegram messenger, sign in to your account or create a new one.
   1. Enter _@Botfather_ in the search tab and choose this bot.<br>*Note, official Telegram bots have a blue checkmark beside their name*.<br>
   ![image1][img1]
   1. Click _Start_ to activate BotFather bot.<br>
   ![image2][img2]
   1. Choose or type _/newbot_ and send it.<br>
   ![image3][img3]
   1. Choose a name for the bot, the bot can be found by its username in searches. The username must be unique and end with the word _bot_.<br>
1. ***Getting the bot API token***
   * **Newly created bot**<br>
   ![image4][img4]
   * **Already existing bot**<br>
   ![image5][img5]
   ![image6][img6]
   ![image7][img7]
1. ***Run sample code***
```python
from telegram import notifly

token = input("Enter bot token : ")
bot=notifly.BotHandler(token)
text = input("Enter text message : ")
print(bot.send_message(text))
opt_image = input("Do you want to send image ?")
if(opt_image=='y' or opt_image=='Y'):
    img_path = input("Enter full image path : ")
    bot.send_image(img_path)
```
![image8][img8]
![image9][img9]
## Contributing
1. Fork the Project
1. Create your Feature Branch 
```
git checkout -b feature/mybranch
```
1. Commit your Changes 
```
git commit -m 'Add something'
```
1. Push to the Branch 
```
git push origin feature/mybranch
```
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
[img1]:others/1.png
[img2]:others/2.png
[img3]:others/3.png
[img4]:others/4.png
[img5]:others/5.png
[img6]:others/6.png
[img7]:others/7.png
[img8]:others/8.png
[img9]:others/9.png
