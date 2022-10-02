import os
import discord
from chatbot import Chatbot
from dotenv import load_dotenv

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
prefix = "hey bozo"
cb = Chatbot()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix) and len(message.content[8:].lstrip()) > 0:
        cb.extend_prompt(message.author.name.capitalize(), message.content[8:].lstrip())
        cb.print_prompt()
        await message.channel.send(cb.generate_response())

client.run(os.getenv('DISCORD_TOKEN'))