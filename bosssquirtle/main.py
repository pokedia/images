import discord
from discord.ext import commands
import asyncio

# Load tokens from file
with open('tokens.txt', 'r') as f:
    tokens = [line.strip() for line in f if line.strip()]

OWNER_ID = 1273958641879486540  # Replace with your Discord User ID
COMMAND_PREFIX = '!'

# Function to start selfbot with a token
async def start_selfbot(token):
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=COMMAND_PREFIX, self_bot=True, intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} has logged in!')

    @bot.command()
    async def ping(ctx):
        if ctx.author.id == OWNER_ID:
            print(f'Ping command received from {ctx.author} in {ctx.channel}')
        else:
            print(f'Ignored command from unauthorized user {ctx.author}')

    try:
        await bot.start(token)
    except Exception as e:
        print(f'Error logging in with token {token}: {e}')

# Main function to start all selfbots
async def main():
    tasks = []
    for token in tokens:
        tasks.append(start_selfbot(token))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
