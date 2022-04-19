Introduction:
This repository contains simple telegram bot 'CashLover' for exchange currencies.

Requirements for the bot.
1) The bot returns the price for a certain amount of currency (euro, dollar or ruble).
2) When writing a bot, you must use the 'pytelegrambotapi' library.
3) A person must send a message to the bot in the form <name of the currency the price of which he wants to know>
 <name of the currency in which you want to find out the price of the first currency> <amount of the first currency>.
4)When you enter the command /start or /help, the user will receive instructions on how to use the bot.
5)When entering the /values command, information about all available currencies should be displayed in a readable form.
6)To take the exchange rate, you must use the API and send requests to it using the 'Requests' library.
7) To parse the received responses, use the JSON library.
8) If the user makes a mistake (for example, an incorrect or non-existent currency is entered, or a number is entered incorrectly),
 throw a self-written APIException with the error explanation text.
9) The text of any error indicating the type of error should be sent to the user in messages.
10) To send requests to the API, describe a class with a static get_price () method that takes three arguments: the name of the currency,
 the price of which you need to find out - base, the name of the currency, the price of which you need to find out - quote, the amount of the transferred currency - amount and returns the required amount in the currency.
11) Store the telegramm-bot token in a special config (you can use a .py file).
12) Hide all classes in the extensions.py file.


