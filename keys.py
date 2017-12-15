import tweepy

# Create variables for each key, secret, token
consumer_key = '662LS2gAlBpV04Un07uu4szoe'
consumer_secret = 'JizABplMKiwm7JfB3zRD0IM5Go6u8iyYM3Ch2AbGWz2TuoNAyI'
access_token = '941441521450213378-oAIFLCJ79n7LkKR3frj4B4Hru85bpF4'
access_token_secret = 'HvlTfKoq4snoJJ69mBwPiliM03HjF0D4T1HjB0GOFm6Va'

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)