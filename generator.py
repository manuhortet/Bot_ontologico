from random import randint
from markovbot import MarkovBot
import os

bot = MarkovBot()

# Creating a list with the books our book will learn from
books = [os.path.join(os.path.dirname(os.path.abspath(__file__)), 'LaNausea-Sartre.txt'),
         os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Critica_de_la_razon_dialectica.txt')]

# Make your bot read the books!
for book in books:
    bot.read(book)

for x in range(0, 3):
    # len of the new tweets that will be generated, in words (we are not counting "El sentido de la vida es")
    tweet_len = randint(5, 10)
    # generating tweet, based on its len and seedwords!
    tweet = bot.generate_text(tweet_len, seedword=[])
    # adding the beginning of the sentence and solving possible capital letter problem.
    tweet = "El sentido de la vida es " + tweet[0].lower() + tweet[1::]

    # writting to our generated_sentences.txt file
    sentences_list = open("generated_sentences.txt", "a")
    sentences_list.write(tweet + "\n")
    sentences_list.close()



