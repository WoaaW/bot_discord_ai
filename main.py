from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message    
from response import get_response
from openai import OpenAI

load_dotenv()
TOKEN : Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

ai = OpenAI(api_key=os.getenv('GPT_TOKEN'))

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enable probably)')
        return
    
    if (is_private := user_message[0] == "?") or user_message[0] =="!":
        user_message = user_message[1:]
    else:
        return
    
    try:
        response: str = get_response(user_message, ai)
        if response == "None":
            return
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running !')


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return 
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}]{username}:"{user_message}"')
    await send_message(message=message, user_message=user_message)


def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()