import discord
import time
import random
import requests
from translate import Translator

token = 'YOUR_TOKEN_HERE'
client = discord.Client()
id = client.get_guild('YOUR ID HERE')
#SOULD BE A INTEGER
time_string = time.strftime('%H:%M')
print("bot is ready")
base_url = "https://api.openweathermap.org/data/2.5/weather?appid=YOUR-ID-FROM-OPENWHEATHER-API&units=metric"
complete_url = base_url + "&q=" + 'CITY YOU WANT'
response = requests.get(complete_url)

x = response.json()
if x["cod"] != "404":
    y = x["main"]
    temp = y["temp"]

@client.event
async def on_message(message):
    id = client.get_guild('YOUR-ID-HERE')#SHOULD BE A INTEGER
    global temp
    if message.content == 'Bot':
        await message.channel.send(random.choice(['Yes', "I'm here"]))
    elif message.content == "hello":
        await message.channel.send(random.choice(['Hi', "Hello", "How are you", "How are you doing today"]))
    elif message.content == "help":
        await message.channel.send("""
        help to display this message\n\n hello for a greeting message\n\n users for a # of members\n\n time to display time\n\n bye for goodbyes\n\n Weather_i for weather

        """)
    elif message.content == "users":
        await message.channel.send(f"""# of Members: {id.member_count}""")
    elif message.content == 'time':
        await message.channel.send('the time is {}'.format(time_string))
    elif message.content == "bye":
        await message.channel.send(random.choice(['see you later', 'have a great day', 'Goodbye']))
    elif message.content == 'Weather_m':
        temp = str(temp)
        await message.channel.send(temp + ' celsius')
    elif message.content == 'Weather_i':
        temp = int(temp)/5*9+32
        temp = str(temp)
        await message.channel.send(temp + ' Fahrenheit')
    elif 'Translate' in message.content:
        count = 0
        while count == 0:
            tra = message.content
            translator = Translator(from_lang='en', to_lang='spanish')
            translated = translator.translate(tra)
            await message.channel.send(translated)
            count += 1



# We can use id.member_count







client.run(token)



