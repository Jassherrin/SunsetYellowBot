#This code was mostly from https://www.youtube.com/watch?v=NwBWW8cNCP4&t=196s
#I'm trying edit, have fun and maybe improve on the YouTube video's Telegram chatbot finally making it my own
import os
import telebot
import yfinance as yf
#Keep Alive is from https://www.youtube.com/watch?v=0BT1rGMAFwQ
from keep_alive import keep_alive
my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)


@bot.message_handler(commands=['Help', 'help', 'Start', 'start'])
def help(message):
    bot.reply_to(
        message,
        "Greetings: /Hiya /hiya /Hi /Hey /hey /yo /Heya /Yahallo /yahallo /heya /Yellow /yellow  /hello /Hello /hi\n \nIf you're feeling sad/depressed/suicidal: /Sad  /sad /depressed /Depressed /Depression /depression /feelingSuicidal\n   \nA bunch of fun stuff /Bored /bored \n \nRandom stock trade thingy from the og that I improved this bot from [IDK what this is but it's kinda cool so I kept in LOL] : /wsb"
    )


#Example of how a command looks
@bot.message_handler(commands=['Hiya', 'hiya', 'Hi', 'Hey', 'hey'])
def Hiya(message):
    bot.reply_to(message, "Hey! Hows it going?")


@bot.message_handler(
    commands=['yo', 'Heya', 'Yahallo', 'yahallo', 'heya', 'Yellow', 'yellow'])
def yo(message):
    bot.reply_to(message, "Yellow!")


@bot.message_handler(commands=['hello', 'Hello', 'hi'])
def hello(message):
    bot.send_message(message.chat.id, "Hello! What's up")


@bot.message_handler(
    commands=['Sad', 'sad'])
def sad(message):
    bot.reply_to(
        message,
        "Oh no! Take a deep breath and calm down first. It's fine if you are feeling sad but if you feel like it is a problem, please remember that you are the bigger person"
    )

@bot.message_handler(
    commands=['depressed', 'Depressed'])
def depressed(message):
    bot.reply_to(
        message,
        "Oh no! Take a deep breath and calm down first. It's fine if you are feeling sad but if you feel like it is a problem, please remember that you are the bigger person"
    )

@bot.message_handler(
    commands=['Depression','depression'])
def depression(message):
    bot.reply_to(
        message,
        "Oh no! Take a deep breath and calm down first. It's fine if you are feeling sad but if you feel like it is a problem, please remember that you are the bigger person"
    )
    
@bot.message_handler(
    commands=['feelingSuicidal'])
def feelingSuicidal(message):
    bot.reply_to(
        message,
        "Hold on. Please don't let go yet. \n \nSamaritans of Singapore: 1800-221 4444\n Singapore Website: https://www.sos.org.sg/ \n \nSocial Awareness Education & Mental Health Resources \n Website: https://ttsresources.carrd.co/ \n \n International Suicide Helplines: https://www.opencounseling.com/suicide-hotlines \n \n")


@bot.message_handler(commands=['Bored', 'bored', 'boring'])
def bored(message):
    bot.reply_to(message, "Quick! Think of something you love! \n \nPerhaps I can help you! \n \nWhat do you like? \n \n/Cartoons \n \n /AdultCartoons\n \n/Anime\n \n/Games\n \n/Movies\n \n/Music\n \n/Books\n \n/Studying")

@bot.message_handler(commands=['Cartoons', 'Cartoon', 'cartoon','cartoons'])
def cartoon(message):
    bot.reply_to(message, "What cartoon is pulling you in right now! \n Amphibia: /Amphibia \n \nThe Owl House: /toh \n \n Gravity Falls: /gravityfalls")

@bot.message_handler(commands=['AdultCartoons', 'adultCartoon', 'adultcartoon','adultcartoons'])
def adultcartoon(message):
    bot.reply_to(message, "What adult cartoon is pulling you in right now! \n Rick And Morty: /RickAndMorty \n \nHelluva Boss: /helluvaboss \n \n Hazbin Hotel: /hazbinhotel")

@bot.message_handler(commands=['RickAndMorty'])
def RickAndMorty(message):
    bot.reply_to(message, "Rick And Morty Edits: https://www.youtube.com/watch?v=qpBp9j9r9Io&list=PLVPSyfRaOtXfnaPlfB3r5ESX6JEn-JyJh \n \n Just Marcy edits to make you cry: https://www.youtube.com/watch?v=5w1mgY6GovU&list=PL7Sg-r1IjzQBWlS1mpf04lQ5ZdQ0v_MY3 \n \n Amphibia Animatics: https://www.youtube.com/watch?v=fRVjyc7so20&list=PLsvQpgyawT-jkPbVx0loQ48DjkfEHyNcp \n \n")

@bot.message_handler(commands=['helluvaboss'])
def helluvaboss(message):
    bot.reply_to(message, "Helluva Boss Episodes: https://www.youtube.com/watch?v=OlahNrlcgS4&list=PL-uopgYBi65HwiiDR9Y23lomAkGr9mm-S \n \n Rick And Morty Edits: https://www.youtube.com/watch?v=qpBp9j9r9Io&list=PLVPSyfRaOtXfnaPlfB3r5ESX6JEn-JyJh \n \n Just Marcy edits to make you cry: https://www.youtube.com/watch?v=5w1mgY6GovU&list=PL7Sg-r1IjzQBWlS1mpf04lQ5ZdQ0v_MY3 \n \n Amphibia Animatics: https://www.youtube.com/watch?v=fRVjyc7so20&list=PLsvQpgyawT-jkPbVx0loQ48DjkfEHyNcp \n \n")

@bot.message_handler(commands=['hazbinhotel'])
def hazbinhotel(message):
    bot.reply_to(message, "Rick And Morty Edits: https://www.youtube.com/watch?v=qpBp9j9r9Io&list=PLVPSyfRaOtXfnaPlfB3r5ESX6JEn-JyJh \n \n Just Marcy edits to make you cry: https://www.youtube.com/watch?v=5w1mgY6GovU&list=PL7Sg-r1IjzQBWlS1mpf04lQ5ZdQ0v_MY3 \n \n Amphibia Animatics: https://www.youtube.com/watch?v=fRVjyc7so20&list=PLsvQpgyawT-jkPbVx0loQ48DjkfEHyNcp \n \n")

@bot.message_handler(commands=['Anime'])
def Anime(message):
    bot.reply_to(message, "Quick! Think of something you love! \n Perhaps I can help you! \n What do you like? \n /Cartoons")

@bot.message_handler(commands=['Games'])
def Games(message):
    bot.reply_to(message, "Quick! Think of something you love! \n Perhaps I can help you! \n What do you like? \n /Cartoons")


@bot.message_handler(commands=['Amphibia'])
def Amphibia(message):
    bot.reply_to(message, "Amphibia Edits: https://www.youtube.com/watch?v=qpBp9j9r9Io&list=PLVPSyfRaOtXfnaPlfB3r5ESX6JEn-JyJh \n \n Just Marcy edits to make you cry: https://www.youtube.com/watch?v=5w1mgY6GovU&list=PL7Sg-r1IjzQBWlS1mpf04lQ5ZdQ0v_MY3 \n \n Amphibia Animatics: https://www.youtube.com/watch?v=fRVjyc7so20&list=PLsvQpgyawT-jkPbVx0loQ48DjkfEHyNcp \n \n")


@bot.message_handler(commands=['toh'])
def toh(message):
    bot.reply_to(message, "The Owl House Edits: https://www.youtube.com/watch?v=p2dI-zXJLcg&list=PLEICknKOGouZfA__qAjQvq1boFK58gcCA \n \n The Owl House animatics: https://www.youtube.com/watch?v=lPdvkZ82PyU&list=PLtX2GC6XkoKC8DnWZh_9FzTZupHfv7M5b \n \n")


@bot.message_handler(commands=['gravityfalls'])
def gravityfalls(message):
    bot.reply_to(message, "Gravity Falls AMV/PMV/CMV: youtube.com/watch?v=6d-JGjgKYM0&list=PLE_zi5OoXQeIggc-yVskX6qQBSc4uytdt \n \n Gravity falls amv: https://www.youtube.com/watch?v=wL4-AslLA9I&list=PL8oix_w8H_agmcVwjMz8ZHT8DG1NlNfIq \n \n Gravity Falls Ost: https://www.youtube.com/watch?v=JZaJ_dP2mIk&list=PLOKYpoOuhMVRDp1VxX31IP8J9Wl2TDO8F \n \n")

#Stock thingy from the YouTube video, idk what it does but Imma just keep it
@bot.message_handler(commands=['wsb'])
def get_stocks(message):
    response = ""
    stocks = ['gme', 'amc', 'nok']
    stock_data = []
    for stock in stocks:
        data = yf.download(tickers=stock, period='2d', interval='1d')
        data = data.reset_index()
        response += f"-----{stock}-----\n"
        stock_data.append([stock])
        columns = ['stock']
        for index, row in data.iterrows():
            stock_position = len(stock_data) - 1
            price = round(row['Close'], 2)
            format_date = row['Date'].strftime('%m/%d')
            response += f"{format_date}: {price}\n"
            stock_data[stock_position].append(price)
            columns.append(format_date)
        print()

    response = f"{columns[0] : <10}{columns[1] : ^10}{columns[2] : >10}\n"
    for row in stock_data:
        response += f"{row[0] : <10}{row[1] : ^10}{row[2] : >10}\n"
    response += "\nStock Data"
    print(response)
    bot.send_message(message.chat.id, response)


def stock_request(message):
    request = message.text.split()
    if len(request) < 2 or request[0].lower() not in "price":
        return False
    else:
        return True


@bot.message_handler(func=stock_request)
def send_price(message):
    request = message.text.split()[1]
    data = yf.download(tickers=request, period='5m', interval='1m')
    if data.size > 0:
        data = data.reset_index()
        data["format_date"] = data['Datetime'].dt.strftime('%m/%d %I:%M %p')
        data.set_index('format_date', inplace=True)
        print(data.to_string())
        bot.send_message(message.chat.id,
                         data['Close'].to_string(header=False))
    else:
        bot.send_message(message.chat.id, "No data!?")

keep_alive()
bot.polling()
