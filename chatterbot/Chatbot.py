from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Jarvis')

trainer = ListTrainer(bot)

for files in os.listdir("/chatterbot/"):
    data = open("/chatterbot/"+files, 'r').readlines()
    trainer.train(data)

while True:
    try:
        message = str(input('You: '))
        bot_input = bot.get_response(message)
        print('Jarvis:',bot_input)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
