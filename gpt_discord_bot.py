import os
import openai
import discord
from discord.ext import commands

# Set up the OpenAI API client
openai.api_key = "YOUR_OPEN_API_KEY"

# Define the required intents
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

# Set up the Discord bot
bot = commands.Bot(command_prefix='/', intents=intents)
bot_token = "YOUR_DISCORD_BOT_TOKEN"

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='gpt')
async def gpt(ctx, *, prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{prompt}\n\n",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.8,
    )

    reply = response.choices[0].text.strip()
    await ctx.send(reply)

# Run the bot
bot.run(bot_token)
