import time
import tweepy
import config
#print(config.BEARER_TOKEN)
auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

class MyStreamListener(tweepy.StreamingClient):
    def on_connect(self):
        print("Connected")
    def on_tweet(self, tweet):
        # Displaying tweet in console
        # if tweet.referenced_tweets == None:
        #     print(tweet.text)
        #     # Delay between tweets
        #     time.sleep(0.5)
        print("someone tweeted")
        print(tweet.text)
            # Delay between tweets
        time.sleep(0.5)

def streamtweets(stream):
   print(stream.get_rules())
   stream.filter()

def clear_rules(stream):
    rule_list = stream.get_rules()
    rule_ids = []
    print(rule_list[3]["result_count"])
    if rule_list[3]["result_count"] != 0:
        for r in rule_list[0]:
            rule_ids.append(r.id)
        stream.delete_rules(rule_ids)
        print(rule_ids)
    
def set_rules(stream):
    stream.add_rules(tweepy.StreamRule('#blackpanther'))

#main
#create stream
stream = MyStreamListener(bearer_token=config.BEARER_TOKEN)
#streamtweets()
clear_rules(stream)
#print(stream.get_rules())
set_rules(stream)
stream.filter()

