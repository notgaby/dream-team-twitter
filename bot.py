import tweepy
from config import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token

#Info to connect our API to our code
client = tweepy.Client(consumer_key = consumer_key,
                    consumer_secret = consumer_secret,
                    access_token = access_token,
                    access_token_secret = access_token_secret,
                    bearer_token= bearer_token)


#Creating a simple tweet
response = client.create_tweet(text='bing bong3 hi')

print("hi5")
