import time
import tweepy
import config
#print(config.BEARER_TOKEN)
auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
client = tweepy.Client(bearer_token=config.BEARER_TOKEN, 
                       consumer_key= config.API_KEY, 
                       consumer_secret=config.API_SECRET, 
                       access_token=config.ACCESS_TOKEN, 
                       access_token_secret=config.ACCESS_TOKEN_SECRET)


streaming_client = tweepy.StreamingClient(config.BEARER_TOKEN)
#streaming_client.add_rules(tweepy.StreamRule("phone"))
print(streaming_client.get_rules())
#streaming_client.filter()