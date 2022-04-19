import telebot
from Config import TOKEN, Currencies
from Extentions import CryptoConvector, APIException
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'To get started, enter the bot command in the following format:\n<currency name> \
<in which currency to exchange> \
<amount of exchanged currency>\nSee a list of all available currencies: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Available currencies:'
    for key in Currencies.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Too many parameters.')

        quote, base, amount = values
        total_base = CryptoConvector.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'User error.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Failed to process command\n{e}')
    else:
        text = f'Price {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)