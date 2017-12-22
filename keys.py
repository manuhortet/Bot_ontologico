import tweepy

# Creating variables for the different needed keys.

# Consumer Key (API Key) && Consumer Secret (API Secret)
consumer_key = ""
consumer_secret = ""
# Access Token && Access Token Secret
access_token = ""
access_token_secret = ""

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
