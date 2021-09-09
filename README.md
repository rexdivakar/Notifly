# Notifly  
### [Code Usage](https://rexdivakar.github.io/Notifly/)
![PyPI](https://img.shields.io/pypi/v/notifly?logo=github&style=for-the-badge)
![PyPI - Downloads](https://img.shields.io/pypi/dm/notifly?color=green&style=for-the-badge&logo=github)
![Discord](https://img.shields.io/discord/760088481224851476?label=DISCORD&logo=discord&logoColor=green&style=for-the-badge)


<p align="center">	<p align="center">
<img src="https://raw.githubusercontent.com/rexdivakar/Notifly/main/.others/bot.png" width="200" alt="Logo">

## Table of Contents
* [About the package](#about-the-package)
  * [Built With](#built-with)
* [Prerequisites for install](#prerequisites)
* [Install the package](#install-the-package)
* [Working of the tool](#working-of-the-tool)
    * [Telegram](#telegram)
    * [Discord](#discord)
    * [Slack](#slack)
* [Contributing](#contributing)

## About the package
Simple Bots to push notifications during an event trigger. <br>

[!["Telegram"](https://img.shields.io/badge/%20Telegram-%20.svg?longCache=true&logo=telegram&colorB=blue)](https://telegram.org/) 
wrapper to send messages, images, files over the bot using API. <br>
[!["Discord"](https://img.shields.io/badge/%20Discord-%20.svg?longCache=true&logo=discord&colorB=lightblue)](https://discord.com/) 
wrapper to send message, images, files to the channel using Webhooks. <br>
[!["Slack"](https://img.shields.io/badge/%20slack-gray.svg?longCache=true&logo=slack&colorB=brightgreen)](https://slack.com) 
wrapper to send message, images, files to the channel using API.

### Built With
* [Python 3][1]

## Prerequisites
* Python<br>
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
* Directly download packages:
```
pip3 install requests==2.24.0
pip3 install matplotlib==3.2.2
pip3 install slackclient==2.9.3
```

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

## Working of the tool
### Telegram
To see how the tool works,
1. Create the [telegram bot][2].
2. Getting the bot API token
   1. Search and go to ```_@Botfather_``` .
   1. Message ```/mybots``` .
   1. Select the bot.
   1. Select the _API token_ displayed in message.
   1. Copy and use in sample code.
   ```python
   from notifly import telegram        #import the package    
   x = telegram.Notifier('bot API token')        #create object of class Notifier
   x.send_message('message')       #send message
   x.send_image("image address")        #send image(.jpg or .png format)
   x.send_file("file address")     #send document
   x.session_dump()        #creates folder named 'downloads' in local folder, downloads/saves message,chat details for current session in 'sessio_dump.json' file
    ```
3. Run sample code.
### Discord
To see how the tool works,
1. Create server.
2. Create and copy server [webhook][5] and use in sample code.
   ```python
   from notifly import discord
   x = discord.Notifier(r'webhook')       #create object of class Notifier
   x.send_message('message')      #send message
   x.send_file("file address")        #send file
   x.send_file("image address")       #send image
   ```
3. Run sample code.
### Slack
To see how the tool works,
1. Create app. Follow these steps,
    1. Go [here][6].
    2. Go to ```Create an App``` .
    3. Enter _App Name_ and select workspace. Click ```Create App```.
    4. Under **Add features and functionality** select ```Incoming Webhooks``` and **Activate Incoming Webhooks**.
    5. Scroll down, select ```Add New Webhook to Workspace``` and select a channel from the drop down.This channel name is used as an argument in the sample code. Click ```Allow```.
    6. Select **OAuth & Permissions** from left-sidebar.
    7. Under **Scopes** > **Bot Token Scopes**  click ```Add an OAuth Scope``` and add the following scopes,
       <br>```chat:write``` &nbsp; ```chat:write.public``` &nbsp; ```files:write``` &nbsp; ```users:write```
    8. Scroll up, under **OAuth Tokens for Your Team** copy the *Bot User OAuth Access Token* to use in sample code.
    9. Click ```Reinstall to Workspace```, select channel and click ```Allow```.
2. Write sample code.
   ```python
   from notifly import slack
   x= slack.Notifier('token', channel='channel-name')      #create object of class Notiflier
   x.send_message('message')      #send message
   x.send_file("image or file address")      #send image/file
   ```
3. Run sample code.

### Tensorflow Integration
Plug and play feature for your tensorflow callbacks
```python
# create your notifier using above methods
from notifly import discord
notifier = discord.Notifier(r'webhook') 
class MyNotifierCallback:

    @notifier.notify_on_epoch_begin(epoch_interval=1, graph_interval=1, hardware_stats_interval=1)
    def on_epoch_begin(self, epoch, logs=None):
        pass

    @notifier.notify_on_epoch_end(epoch_interval=1, graph_interval=1, hardware_stats_interval=1)
    def on_epoch_end(self, epoch, logs=None):
        pass

    @notifier.notify_on_train_begin()
    def on_train_begin(self, logs=None):
        pass

    @notifier.notify_on_train_end()
    def on_train_end(self, logs=None):
        pass

model.fit(callbacks=[MyNotifierCallback()])
```
## Learn more about Notifly ✨
Read the [wiki pages](https://github.com/rexdivakar/Notifly/wiki) which has all the above steps in great detail with some examples as well 🤩🎉.

## Contributing
1. Fork the Project
1. Create your Feature Branch 
   >git checkout -b feature/mybranch
1. Commit your Changes 
    >git commit -m 'Add something'
1. Push to the Branch
    >git push origin feature/mybranch
1. Open a Pull Request<br><br>
Follow the given commands or use the amazing ***GitHub GUI***<br>
**Happy Contributing**

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
[1]:https://www.python.org/
[2]:https://telegram.org/blog/bot-revolution
[4]:https://www.python.org/downloads/
[5]:https://discordjs.guide/popular-topics/webhooks.html#fetching-all-webhooks-of-a-guild
[6]:https://api.slack.com/
