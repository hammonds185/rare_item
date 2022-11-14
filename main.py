import tweepy
import config
print(config.BEARER_TOKEN)
auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.user.screen_name +  "tweeted" + status.text)

def streamtweets():
    MyStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener =MyStreamListener)
    myStream.filter(track=['gymnastics'])

streamtweets()
