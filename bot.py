import random
import telebot

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)

def load_responses(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()
        responses = content.split('",\n"')
        responses[0] = responses[0][1:]
        responses[-1] = responses[-1][:-1]
        return responses

responses = load_responses('Lines.txt')

@bot.message_handler(func=lambda message: message.text.isdigit())
def send_random_responses(message):
    num_responses = int(message.text)
    if num_responses > 30:
        bot.reply_to(message, f"Извините, У меня есть ограничение на количество символов. Попробуйте число меньше 30.")
        return
    random_responses = random.sample(responses, num_responses)
    bot.reply_to(message, "\n".join(random_responses))

@bot.message_handler(func=lambda message: True)
def send_help(message):
    bot.reply_to(message, "Отправьте число, чтобы получить столько случайных строк из анекдотов про сталкеров.")

bot.polling(none_stop=True)
