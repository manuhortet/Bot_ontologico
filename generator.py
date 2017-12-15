from keys import *
from random import randint
from markovbot import MarkovBot
import os

tweetbot = MarkovBot()

# Log in to Twitter
# tweetbot.twitter_login(consumer_key, consumer_secret, access_token, access_token_secret)
# Construct the path to the book
book = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'LaNausea-Sartre.txt')
# Make your bot read the book!
tweetbot.read(book)

tweet_len = randint(5, 15)

tweet = tweetbot.generate_text(tweet_len, seedword=[])

tweet = "El sentido de la vida es " + tweet[0].lower() + tweet[1::]



# print(tweet)

# writting to our generated_sentences.txt file
# sentences_list = open("generated_sentences.txt", "a")
# sentences_list.write(tweet + "\n")
# sentences_list.close()



