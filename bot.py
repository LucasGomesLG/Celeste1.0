import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '/conselho':
            await message.channel.send(f'{message.author.name}  Não dá pra discutir na internet.{os.linesep}Por mais brilhante que seja sua ideia, a outra pessoa pode rebater com a figurinha do Vampeta pelado{os.linesep}que é um argumento muito mais forte.') 
    async def on_member_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} Acabou de chegar, seja bem vindo'
            await guild.system_channel.send(mensagem)

intents = discord.Intents.default()
intents.members = True

client = MyClient()
client.run('MTExNjE3NDI3MzA3NDE2Nzg1OA.Gvf1Uq.5ixI-jSKEx1AeAW9nz4WkrPvYfdXQBRXAplxAE')