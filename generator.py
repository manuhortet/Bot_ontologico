from keys import *
from markovbot import MarkovBot
import os

tweetbot = MarkovBot()

# Log in to Twitter
# tweetbot.twitter_login(consumer_key, consumer_secret, access_token, access_token_secret)
# Construct the path to the book
book = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'LaNausea-Sartre.txt')
# Make your bot read the book!
tweetbot.read(book)

tweet = tweetbot.generate_text(10, seedword=['vida', 'sentido'])

tweet = "El sentido de la vida es " + tweet[0].lower() + tweet[1::]

api.update_status(status=tweet)
print(tweet)
