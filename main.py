import telebot
import random
from config import secret_tocken

bot = telebot.TeleBot(secret_tocken)


@bot.message_handler(commands=['hello'])
def index(message):
    bot.send_message(message.chat.id, 'Привет!', parse_mode='html')


@bot.message_handler(commands=['start', 'roll'])
def index(message):
    stats = []
    list_roll_all = []
    all_list = ''
    for el in range(6):
        a = sorted([int(random.randint(1, 6)) for num in range(4)])
        list_roll_all.append(a)
        mod = a[1] + a[2] + a[3]
        stats.append(mod)

    for elem in range(len(list_roll_all)):
        if stats[elem] // 10 % 10 > 0:
            all_list += str(stats[elem]) + "    " + str(list_roll_all[elem]) + "\n"
        else:
            all_list += str(stats[elem]) + "      " + str(list_roll_all[elem]) + "\n"
    print(all_list)
    bot.send_message(message.chat.id, all_list)
    bot.send_message(message.chat.id, str(stats))


bot.polling(non_stop=True)