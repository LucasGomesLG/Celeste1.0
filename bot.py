import discord
import random
class MyClient(discord.Client):
    async def on_ready(self):
         activity = discord.Activity(type=discord.ActivityType.watching, name="Robos")
         await client.change_presence(status=discord.Status.online, activity=activity)
         print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        #frases do programa choque de cultura
        conselhos = ['conselho1','conselho2','conselho3','conselho4,conselho5,]
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '/conselho':
            await message.channel.send (f'{message.author.name}, {random.choice(conselhos)}')
        
  
    async def on_member_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} Acabou de chegar, seja bem vindo'
            await guild.system_channel.send(mensagem)


intents = discord.Intents.default()
intents.members = True

client = MyClient('meu token')
