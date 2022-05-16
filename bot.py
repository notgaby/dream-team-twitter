from tracemalloc import start
import tweepy
import datetime as DT
import time
from config import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token


#Info to connect our API to our code
client = tweepy.Client(consumer_key = consumer_key,
                    consumer_secret = consumer_secret,
                    access_token = access_token,
                    access_token_secret = access_token_secret,
                    bearer_token= bearer_token)


#Creating a simple tweet
#response = client.create_tweet(text='Houston, we have a bot!!!!')


print ("Program Start : %s" % time.ctime()) #time the program starts
startDate = DT.datetime.now() 
check = startDate.replace(minute=30)

if(startDate < check): #if the time is below 30 minutes for the current hour
    startDate = startDate.replace(minute=30,second=0,microsecond=0)
else: #if the time is 30 minutes past the current hour
    startDate = startDate.replace(hour=DT.datetime.now().hour+1,minute=0,second=0,microsecond=0)

print(f'Next tweet will be at : {startDate}')
while True:
    if(DT.datetime.now() >= startDate): #wait until start of the hour
        response = client.create_tweet(text="The current date and time is: %s" % time.ctime()) #tweet
        dt = DT.datetime.now() + DT.timedelta(minutes=30) #sets the time for the next tweet
        dt = dt.replace(second=0,microsecond=0)
        print(f'Next tweet will be at : {dt}')
        while DT.datetime.now() < dt: #wait until it's time for next tweet
            time.sleep(1)
        

