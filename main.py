#Sunset Yellow Telegram Bot
#This code was mostly from https://www.youtube.com/watch?v=NwBWW8cNCP4&t=196s
#I'm trying edit, have fun and maybe improve on the YouTube video's Telegram chatbot finally making it my own
import telebot
import os
# import yfinance as yf
import random
# import requests
# import time
#Keep Alive is from https://www.youtube.com/watch?v=0BT1rGMAFwQ
from keep_alive import keep_alive

my_secret = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(my_secret)
#how to print random string
#https://www.codegrepper.com/code-examples/python/print+random+string+from+list+python
#import random
#SWW

#foo = ['a', 'b', 'c', 'd', 'e']
#print(random.choice(foo))
#https://www.therandomvibez.com/best-cheer-up-quotes/
sad = [
  'Oh no! Take a deep breath and calm down first. It is fine if you are feeling sad but if you feel like it is a problem, please remember that you are the bigger person!',
  'Life is better when you’re laughing.',
  'Stars can’t shine without darkness.',
  'Cheer up, tomorrow is another chance.', 'Stay Determined.',
  'Tomorrow is another day.',
  'You can do this. 00:00 is a new day. Stay determined till then. Look at how strong you are! Come on bud! You are at the home stretch!',
  'Here, listen to this and cheer up! https://www.youtube.com/watch?v=pw-2e3T03Co&t=3231s&ab_channel=pengweng',
  'Oh no! Take a deep breath and calm down first. It is fine if you are feeling sad but if you feel like it is a problem, please remember that you are the bigger person',
  'You matter and your opinions are valid✨'
]
#sad = ['', '', '', '', '']
#random.choice(sad)

#Tarot cards: https://labyrinthos.co/blogs/tarot-card-meanings-list
tarot = [
  'The World Upright: fulfillment, harmony, completion',
  'The World Reversed: incompletion, no closure',
  'Judgement Upright: reflection, reckoning, awakening',
  'Judgement Reversed: lack of self awareness, doubt, self loathing',
  'The Sun Upright: joy, success, celebration, positivity',
  'The Sun Reversed: negativity, depression, sadness',
  'The Moon Upright: unconscious, illusions, intuition',
  'The Moon Reversed: confusion, fear, misinterpretation',
  'The Star Upright: hope, faith, rejuvenation',
  'The Star Reversed: faithlessness, discouragement, insecurity',
  'The Tower Upright: sudden upheaval, broken pride, disaster',
  'The Tower Reversed: disaster avoided, delayed disaster, fear of suffering',
  'The Devil Upright: addiction, materialism, playfulness',
  'The Devil Reversed: freedom, release, restoring control',
  'Temperance Upright: middle path, patience, finding meaning',
  'Temperance Reversed: extremes, excess, lack of balance',
  'Death Upright: end of cycle, beginnings, change, metamorphosis',
  'Death Reversed: fear of change, holding on, stagnation, decay',
  'The Hanged Man Upright: sacrifice, release, martyrdom',
  'The Hanged Man Reversed: stalling, needless sacrifice, fear of sacrifice',
  'Justice Upright: cause and effect, clarity, truth',
  'Justice Reversed: dishonesty, unaccountability, unfairness',
  'The Wheel of Fortune Upright: change, cycles, inevitable fate',
  'The Wheel of Fortune Reversed: no control, clinging to control, bad luck',
  'The Hermit Reversed: loneliness, isolation, lost your way',
  'The Hermit Upright: contemplation, search for truth, inner guidance',
  'Strength Upright: inner strength, bravery, compassion, focus',
  'Strength Reversed: self doubt, weakness, insecurity',
  'The Chariot Upright: direction, control, willpower',
  'The Chariot Reversed: lack of control, lack of direction, aggression',
  'The Lovers Upright: partnerships, duality, union',
  'The Lovers Reversed: loss of balance, one-sidedness, disharmony',
  'The Hierophant Upright: tradition, conformity, morality, ethics',
  'The Hierophant Reversed: rebellion, subversiveness, new approaches',
  'The Emperor Upright: authority, structure, control, fatherhood',
  'The Emperor Reversed: tyranny, rigidity, coldness',
  'The Empress Upright: motherhood, fertility, nature',
  'The Empress Reversed: dependence, smothering, emptiness, nosiness',
  'The High Priestess Upright: intuitive, unconscious, inner voice',
  'The High Priestess Reversed: lack of center, lost inner voice, repressed feelings',
  'The Magician Upright: willpower, desire, creation, manifestation',
  'The Magician Reversed: trickery, illusions, out of touch',
  'The Fool Upright: innocence, new beginnings, free spirit',
  'The Fool Reversed: recklessness, taken advantage of, inconsideration'
]
tarotwands = [
  'Seven of Wands Upright: perseverance, defensive, maintaining control',
  'Seven of Wands Reversed: give up, destroyed confidence, overwhelmed',
  'Four of Wands Upright: community, home, celebration',
  'Four of Wands Reversed: lack of support, transience, home conflicts',
  'Ace of Wands Upright: creation, willpower, inspiration, desire',
  'Ace of Wands Reversed: lack of energy, lack of passion, boredom',
  'Ten of Wands Upright: accomplishment, responsibility, burden',
  'Ten of Wands Reversed: inability to delegate, overstressed, burnt out',
  'Nine of Wands Upright: resilience, grit, last stand',
  'Nine of Wands Reversed: exhaustion, fatigue, questioning motivations',
  'Eight of Wands Upright: rapid action, movement, quick decisions',
  'Eight of Wands Reversed: panic, waiting, slowdown',
  'Six of Wands Upright: victory, success, public reward',
  'Six of Wands Reversed: excess pride, lack of recognition, punishment',
  'Five of Wands Upright: competition, rivalry, conflict',
  'Five of Wands Reversed: avoiding conflict, respecting differences',
  'Three of Wands Upright: looking ahead, expansion, rapid growth',
  'Three of Wands Reversed: obstacles, delays, frustration',
  'Two of Wands Upright: planning, making decisions, leaving home',
  'Two of Wands Reversed: fear of change, playing safe, bad planning',
  'Page of Wands Upright: exploration, excitement, freedom',
  'Page of Wands Reversed: lack of direction, procrastination, creating conflict',
  'Queen of Wands Upright: courage, determination, joy',
  'Queen of Wands Reversed: selfishness, jealousy, insecurities',
  'King of Wands Upright: big picture, leader, overcoming challenges',
  'King of Wands Reversed: impulsive, overbearing, unachievable expectations',
  'Knight of Wands Upright: action, adventure, fearlessness',
  'Knight of Wands Reversed: anger, impulsiveness, recklessness'
]

tarotcups = [
  'King of Cups Upright: compassion, control, balance',
  'King of Cups Reversed: coldness, moodiness, bad advice',
  'Queen of Cups Upright: compassion, calm, comfort',
  'Queen of Cups Reversed: martyrdom, insecurity, dependence',
  'Knight of Cups Upright: following the heart, idealist, romantic',
  'Knight of Cups Reversed: moodiness, disappointment',
  'Page of Cups Upright: happy surprise, dreamer, sensitivity',
  'Page of Cups Reversed: emotional immaturity, insecurity, disappointment',
  'Ten of Cups Upright: inner happiness, fulfillment, dreams coming true',
  'Ten of Cups Reversed: shattered dreams, broken family, domestic disharmony',
  'Nine of Cups Upright: satisfaction, emotional stability, luxury',
  'Nine of Cups Reversed: lack of inner joy, smugness, dissatisfaction',
  'Eight of Cups Upright: walking away, disillusionment, leaving behind',
  'Eight of Cups Reversed: avoidance, fear of change, fear of loss',
  'Seven of Cups Upright: searching for purpose, choices, daydreaming',
  'Seven of Cups Reversed: lack of purpose, diversion, confusion',
  'Six of Cups Upright: familiarity, happy memories, healing',
  'Six of Cups Reversed: moving forward, leaving home, independence',
  'Five of Cups Upright: loss, grief, self-pity',
  'Five of Cups Reversed: acceptance, moving on, finding peace',
  'Four of Cups Upright: apathy, contemplation, disconnectedness',
  'Four of Cups Reversed: sudden awareness, choosing happiness, acceptance',
  'Three of Cups Upright: friendship, community, happiness',
  'Three of Cups Reversed: overindulgence, gossip, isolation',
  'Two of Cups Upright: unity, partnership, connection',
  'Two of Cups Reversed: imbalance, broken communication, tension',
  'Ace of Cups Upright: new feelings, spirituality, intuition',
  'Ace of Cups Reversed: emotional loss, blocked creativity, emptiness'
]

tarotswords = [
  'King of Swords Upright: head over heart, discipline, truth',
  'King of Swords Reversed: manipulative, cruel, weakness',
  'Knight of Swords Upright: action, impulsiveness, defending beliefs',
  'Knight of Swords Reversed: no direction, disregard for consequences, unpredictability',
  'Queen of Swords Upright: complexity, perceptiveness, clear mindedness',
  'Queen of Swords Reversed: cold hearted, cruel, bitterness',
  'Page of Swords Upright: curiosity, restlessness, mental energy',
  'Page of Swords Reversed: deception, manipulation, all talk',
  'Ten of Swords Upright: failure, collapse, defeat',
  'Ten of Swords Reversed: can not get worse, only upwards, inevitable end',
  'Nine of Swords Upright: anxiety, hopelessness, trauma',
  'Nine of Swords Reversed: hope, reaching out, despair',
  'Eight of Swords Upright: imprisonment, entrapment, self-victimization',
  'Eight of Swords Reversed: self acceptance, new perspective, freedom',
  'Seven of Swords Upright: deception, trickery, tactics and strategy',
  'Seven of Swords Reversed: coming clean, rethinking approach, deception',
  'Six of Swords Upright: transition, leaving behind, moving on',
  'Six of Swords Reversed: emotional baggage, unresolved issues, resisting transition',
  'Five of Swords Upright: unbridled ambition, win at all costs, sneakiness',
  'Five of Swords Reversed: lingering resentment, desire to reconcile, forgiveness',
  'Three of Swords Upright: heartbreak, suffering, grief',
  'Three of Swords Reversed: recovery, forgiveness, moving on',
  'Four of Swords Upright: rest, restoration, contemplation',
  'Four of Swords Reversed: restlessness, burnout, stress',
  'Two of Swords Upright: difficult choices, indecision, stalemate',
  'Two of Swords Reversed: lesser of two evils, no right choice, confusion',
  'Ace of Swords Upright: breakthrough, clarity, sharp mind',
  'Ace of Swords Reversed: confusion, brutality, chaos'
]
tarotpentacle = [
  'King of Pentacles Upright: abundance, prosperity, security',
  'King of Pentacles Reversed: greed, indulgence, sensuality',
  'Queen of Pentacles Upright: practicality, creature comforts, financial security',
  'Queen of Pentacles Reversed: self-centeredness, jealousy, smothering',
  'Knight of Pentacles Upright: efficiency, hard work, responsibility',
  'Knight of Pentacles Reversed: laziness, obsessiveness, work without reward',
  'Page of Pentacles Upright: ambition, desire, diligence',
  'Page of Pentacles Reversed: lack of commitment, greediness, laziness',
  'Ten of Pentacles Upright: legacy, culmination, inheritance',
  'Ten of Pentacles Reversed: fleeting success, lack of stability, lack of resources',
  'Nine of Pentacles Upright: fruits of labor, rewards, luxury',
  'Nine of Pentacles Reversed: reckless spending, living beyond means, false success',
  'Eight of Pentacles Upright: apprenticeship, passion, high standards',
  'Eight of Pentacles Reversed: lack of passion, uninspired, no motivation',
  'Seven of Pentacles Upright: hard work, perseverance, diligence',
  'Seven of Pentacles Reversed: work without results, distractions, lack of rewards',
  'Six of Pentacles Upright: charity, generosity, sharing',
  'Six of Pentacles Reversed: strings attached, stinginess, power and domination',
  'Five of Pentacles Upright: need, poverty, insecurity',
  'Five of Pentacles Reversed: recovery, charity, improvement',
  'Four of Pentacles Upright: conservation, frugality, security',
  'Four of Pentacles Reversed: greediness, stinginess, possessiveness',
  'Three of Pentacles Upright: teamwork, collaboration, building',
  'Three of Pentacles Reversed: lack of teamwork, disorganized, group conflict',
  'Two of Pentacles Upright: balancing decisions, priorities, adapting to change',
  'Two of Pentacles Reversed: loss of balance, disorganized, overwhelmed',
  'Ace of Pentacles Upright: opportunity, prosperity, new venture',
  'Ace of Pentacles Reversed: lost opportunity, missed chance, bad investment'
]


@bot.message_handler(commands=['tarot', 'Tarot'])
def Tarot(message):
  bot.reply_to(
    message, "journey- \n\nPast: " + random.choice(tarot) + "\n\nPresent: " +
    random.choice(tarot) + "\n\nFuture: " + random.choice(tarot) +
    "\n \npassion, inspiration and willpower- \n" + random.choice(tarotwands) +
    "\n \nemotions, the unconscious, creativity, and intuition- \n" +
    random.choice(tarotcups) +
    "\n \nintelligence, logic, truth, ambition, conflict and communication- \n"
    + random.choice(tarotswords) +
    "\n \nsecurity, stability, nature, health, and prosperity- \n" +
    random.choice(tarotpentacle))


#Help - Ctrl F from here
@bot.message_handler(commands=['Help', 'help', 'Start', 'start'])
def help(message):
  bot.reply_to(
    message,
    "Welcome to Sunset Yellow. This is just a fun bot\n \nGreetings: /Hiya /hiya /Hi /Hey /hey /yo /Heya /Yahallo /yahallo /heya /Yellow /yellow  /hello /Hello /hi\n  \nA bunch of fun stuff: /Bored /bored \n \nRandom games I made here: /Play\n \nTarot cards: /tarot \nAll tarot stuff are from: https://labyrinthos.co/blogs/tarot-card-meanings-list \n \nIf you're feeling sad/depressed/suicidal: /Sad  /sad /depressed /Depressed /Depression /depression /feelingSuicidal\n  "
  )


sayHi = [
  'Hey! Hows it going?', 'Heya~ Whatz cooking good looking~', 'YOOO~',
  'Konichiwa~', 'Wazzap~', 'Hola~ Soy Yellow!', 'Hello! Whatchu doin?'
]


#Example of how a command looks
@bot.message_handler(
  commands=['Hiya', 'hiya', 'Hey', 'hey', 'hi', 'Hi', 'Hello', 'hello'])
def Hiya(message):
  bot.reply_to(message, random.choice(sayHi))


sayYellow = [
  'Heya~ Whatz cooking good looking~', 'Hola~ Soy Yellow!', 'Yellow!',
  'Hello, sunshine!', 'I come in peace!', 'Ahoy, matey!',
  'Top of the mornin’ to ya!', 'Wazzup homeslice?', 'Aloha!', 'Que pasa!',
  'Bonjour!', 'Ciaossu!',
  'Salutations pretty person. What do you require of me?', 'Annyeong~'
]


@bot.message_handler(commands=[
  'yo', 'Yo', 'Heya', 'Yahallo', 'yahallo', 'heya', 'Yellow', 'yellow',
  'Aloha', 'aloha', 'bonjour', 'Bonjour', 'annyeong', 'Annyeong'
])
def yo(message):
  bot.reply_to(message, random.choice(sayYellow))


sayHello = [
  'Hey! Hows it going?', 'Hello! Whatchu doin?', 'Hello! What is up?',
  'Sometimes I think greetings are boring',
  'Greetings are meaningless...People say they are fine after basic greetings but most of the time they are just lying through gritted teeth...So then, what is the point in all this?',
  'Salutations!'
]


@bot.message_handler(commands=['hello', 'Hello', 'hi', 'Hi'])
def hello(message):
  bot.send_message(message.chat.id, random.choice(sayHello))


@bot.message_handler(commands=['Sad', 'sad'])
def Sad(message):
  bot.reply_to(message, random.choice(sad))


#random.choice(sad)


@bot.message_handler(
  commands=['Depression', 'depression', 'depressed', 'Depressed'])
def depression(message):
  bot.reply_to(
    message,
    random.choice(sad) + "\n \n" + random.choice(sad) +
    "\n \nSamaritans of Singapore: 1800-221 4444\n Singapore Website: https://www.sos.org.sg/ \n \nSocial Awareness Education & Mental Health Resources \n Website: https://ttsresources.carrd.co/ \n \n International Suicide Helplines: https://www.opencounseling.com/suicide-hotlines \n \n"
  )


@bot.message_handler(commands=['feelingSuicidal', 'feelingsuicidal'])
def feelingSuicidal(message):
  bot.reply_to(
    message,
    random.choice(sad) +
    "\n \nHold on. Please don't let go yet. \n \nSamaritans of Singapore: 1800-221 4444\n Singapore Website: https://www.sos.org.sg/ \n \nSocial Awareness Education & Mental Health Resources \n Website: https://ttsresources.carrd.co/ \n \n International Suicide Helplines: https://www.opencounseling.com/suicide-hotlines \n \n"
  )


@bot.message_handler(
  commands=['play', 'LetsPlay', 'Play', 'letsplay', 'letsPlay', 'Letsplay'])
def playletsplay(message):
  bot.reply_to(message, "Magical 8-ball chance game: /8ball \n \n")


#sad = ['', '', '', '', '']
#random.choice(sad)
#https://futureofworking.com/20-funny-magic-8-ball-sayings/
chanceBall = [
  'Divine intervention time: NO!', 'Suprisingly, I do not know...',
  'Something tells me this is too big of a decision to simply let me decide! Trust yourself!',
  'Hm...umm...really sorry to break it to you...but LOL IT IS A BIG FAT NOPE',
  'YES! The souls deem it so!', 'Hmmm...maybe', 'LOL NO',
  'This will yield great outcomes! Go for it!!!',
  'It is an unfortunate nope. Perhaps, it is time for you to re evluate your life choices.',
  'Sorry...It is a no. Do not worry. Everythiing will be okay. If you wanted this to be a yes, you do not have to hear it from me. You can validate yourself. If you struggle to, then just to let you know: You are special. You are worth it. You are awesome. If you believe it to be a yes, I know you can make it. From me to you: I believe in you',
  'Yes! I wish you the best btw!', 'As I see it, yes', 'Ask again later',
  'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
  'Don’t count on it', 'It is certain', 'It is decidedly so', 'Most likely',
  'My reply is no', 'My sources say no.', 'Outlook good',
  'Outlook not so good', 'Reply hazy try again', 'Signs point to yes',
  'Very doubtful', 'Without a doubt', 'Yes', 'No', 'Yes, definitely.',
  'You may rely on it', 'The Whole World is screaming Yes!', 'YAS QUEEN!',
  'Kamakura, Kamakura Yaas Queen!',
  'Yes, but do not trust the clock, go at your own pace!', 'Hell Yeah!',
  'Not Yet', 'The Universe smiles upon this.'
]


@bot.message_handler(
  commands=['8ball', 'Magical8ball', '8Ball', '8-ball', '8-Ball'])
def ballof8(message):
  bot.reply_to(message, random.choice(chanceBall))


@bot.message_handler(commands=['Bored', 'bored', 'boring'])
def bored(message):
  bot.reply_to(
    message,
    "Quick! Think of something you love! \n \nPerhaps I can help you! \n \nWhat do you like? \n \n/Cartoons \n \n/Anime\n \n/Movies\n \n/Music\n \n/Books\n \n/Studying"
  )


#Do this
@bot.message_handler(commands=['Studying', 'studying', 'Study', 'study'])
def study(message):
  bot.reply_to(
    message,
    "Learn another Language: /learnLanguages \n \n Technology Stuff: /learnTechnology"
  )


@bot.message_handler(commands=['learnLanguages'])
def learnLanguages(message):
  bot.reply_to(message,
               "Learn another Language: https://www.duolingo.com/learn")


@bot.message_handler(commands=['learnTechnology'])
def learnTechnology(message):
  bot.reply_to(
    message,
    "1000+ Free Developer and IT Certifications: https://www.classcentral.com/report/free-developer-it-certifications/ \n \nAutomation: https://automate.io/ \n \nHackerRank: https://www.hackerrank.com/dashboard \n \nLeetcode: https://leetcode.com/study-plan/ \n\nCodeCamp: https://www.codecademy.com/learn?utm_content=blognavbar&utm_medium=ccblog&utm_source=ccblog \n\nSimplilearn: https://www.youtube.com/@SimplilearnOfficial/videos"
  )


#Do this
@bot.message_handler(commands=['Books', 'books', 'Book', 'book'])
def Books(message):
  bot.reply_to(message, "What Book is pulling you in right now?! \n \n")


#Do this
@bot.message_handler(commands=['Music', 'music'])
def Music(message):
  bot.reply_to(message, "Spotify \n\n")


#Do this
@bot.message_handler(commands=['Movies', 'movies', 'movie', 'Movie'])
def Movies(message):
  bot.reply_to(message, "Find movies to watch: https://www.imdb.com/")


#Do this
@bot.message_handler(commands=['Games', 'games', 'Game', 'game'])
def Games(message):
  bot.reply_to(message, "8-ball chance game: /8ball")


#Do this
@bot.message_handler(commands=['Anime', 'anime'])
def anime(message):
  bot.reply_to(message, "Find anime to watch: https://myanimelist.net/ \n\n ")


#Do this
@bot.message_handler(commands=['Cartoons', 'Cartoon', 'cartoon', 'cartoons'])
def cartoon(message):
  bot.reply_to(
    message,
    "What cartoon is pulling you in right now?! \n Amphibia: /Amphibia \n \nThe Owl House: /toh \n \n Gravity Falls: /gravityfalls \n \nHelluva Boss(for 18+ only): /helluvaboss \n \n Hazbin Hotel(for 18+ only): /hazbinhotel"
  )


@bot.message_handler(commands=['helluvaboss'])
def helluvaboss(message):
  bot.reply_to(
    message,
    "Helluva Boss Episodes: https://www.youtube.com/watch?v=OlahNrlcgS4&list=PL-uopgYBi65HwiiDR9Y23lomAkGr9mm-S \n \n \n \n"
  )


@bot.message_handler(commands=['hazbinhotel'])
def hazbinhotel(message):
  bot.reply_to(
    message,
    "Hazbin Hotel Episodes: https://www.youtube.com/watch?v=Zlmswo0S0e0&list=PL-uopgYBi65FM-dSZtZRaYZXreGwAIfV8&ab_channel=Vivziepop  \n \n  "
  )


@bot.message_handler(commands=['Anime'])
def Anime(message):
  bot.reply_to(
    message,
    "All anime: https://myanimelist.net/ \n \n Anime by genre and etc: https://myanimelist.net/anime.php "
  )


@bot.message_handler(commands=['Amphibia'])
def Amphibia(message):
  bot.reply_to(
    message,
    "Amphibia Edits: https://www.youtube.com/watch?v=qpBp9j9r9Io&list=PLVPSyfRaOtXfnaPlfB3r5ESX6JEn-JyJh \n \n Just Marcy edits to make you cry: https://www.youtube.com/watch?v=5w1mgY6GovU&list=PL7Sg-r1IjzQBWlS1mpf04lQ5ZdQ0v_MY3 \n \n Amphibia Animatics: https://www.youtube.com/watch?v=fRVjyc7so20&list=PLsvQpgyawT-jkPbVx0loQ48DjkfEHyNcp \n \n"
  )


@bot.message_handler(commands=['toh'])
def toh(message):
  bot.reply_to(
    message,
    "The Owl House Edits: https://www.youtube.com/watch?v=p2dI-zXJLcg&list=PLEICknKOGouZfA__qAjQvq1boFK58gcCA \n \n The Owl House animatics: https://www.youtube.com/watch?v=lPdvkZ82PyU&list=PLtX2GC6XkoKC8DnWZh_9FzTZupHfv7M5b \n \n"
  )


@bot.message_handler(commands=['gravityfalls'])
def gravityfalls(message):
  bot.reply_to(
    message,
    "Gravity Falls AMV/PMV/CMV: youtube.com/watch?v=6d-JGjgKYM0&list=PLE_zi5OoXQeIggc-yVskX6qQBSc4uytdt \n \n Gravity falls amv: https://www.youtube.com/watch?v=wL4-AslLA9I&list=PL8oix_w8H_agmcVwjMz8ZHT8DG1NlNfIq \n \n Gravity Falls Ost: https://www.youtube.com/watch?v=JZaJ_dP2mIk&list=PLOKYpoOuhMVRDp1VxX31IP8J9Wl2TDO8F \n \n"
  )


#Organize

# #Stock thingy from the YouTube video, idk what it does but Imma just keep it
# @bot.message_handler(commands=['wsb'])
# def get_stocks(message):
#     response = ""
#     stocks = ['gme', 'amc', 'nok']
#     stock_data = []
#     for stock in stocks:
#         data = yf.download(tickers=stock, period='2d', interval='1d')
#         data = data.reset_index()
#         response += f"-----{stock}-----\n"
#         stock_data.append([stock])
#         columns = ['stock']
#         for index, row in data.iterrows():
#             stock_position = len(stock_data) - 1
#             price = round(row['Close'], 2)
#             format_date = row['Date'].strftime('%m/%d')
#             response += f"{format_date}: {price}\n"
#             stock_data[stock_position].append(price)
#             columns.append(format_date)
#         print()

#     response = f"{columns[0] : <10}{columns[1] : ^10}{columns[2] : >10}\n"
#     for row in stock_data:
#         response += f"{row[0] : <10}{row[1] : ^10}{row[2] : >10}\n"
#     response += "\nStock Data"
#     print(response)
#     bot.send_message(message.chat.id, response)

# def stock_request(message):
#     request = message.text.split()
#     if len(request) < 2 or request[0].lower() not in "price":
#         return False
#     else:
#         return True

# @bot.message_handler(func=stock_request)
# def send_price(message):
#     request = message.text.split()[1]
#     data = yf.download(tickers=request, period='5m', interval='1m')
#     if data.size > 0:
#         data = data.reset_index()
#         data["format_date"] = data['Datetime'].dt.strftime('%m/%d %I:%M %p')
#         data.set_index('format_date', inplace=True)
#         print(data.to_string())
#         bot.send_message(message.chat.id,
#                          data['Close'].to_string(header=False))
#     else:
#         bot.send_message(message.chat.id, "No data!?")

# @bot.message_handler(commands=['wordcounter'])
# def wordcounter(message):
#   line_count = 0
#   word_count = 0
#   request = message.text.split()[1]
#   if request != None:
#     # Iterate over the opened file
#     # To the number of lines and words in it
#     for line in request:
#         # Increment the line counter variable
#         line_count = line_count + 1
#         # Find the number of words in each line
#         words = len(line.split())
#         # Add the number of words in each line
#         # To the word counter variable
#         word_count = word_count + words

#     bot.reply_to(message, "\nTotal number of lines in the given file: {line_count}\nTotal number of words in the given file: {word_count})")

keep_alive()
bot.polling()
