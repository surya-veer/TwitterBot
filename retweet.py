#####################################################
#############  By: Suryaveer @IIT indore  ###########
#############  Handle @ayrusreev          ###########
#####################################################

import tweepy
import time

consumer_key = '********'
consumer_secret = '***********'
access_token = '************'
access_token_secret = '**********'


# you can add more tags.. in hash_tag list
hash_tags = ['#example1','#example2','#example3']

class TwitterBot():
    """Class for Twitter Bot"""

    ##time setup in seconds
    retweet_time = 10
    loop_retweet_time = 30  #30 min

    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def retweet(self):
        for query in hash_tags:
            for tweet in tweepy.Cursor(self.api.search, q=query).items(5):
                try:
                    print('\nTweet by @' + tweet.user.screen_name)
                    print('Attempting to retweet')

                    tweet.retweet()
                    print('Retweet published successfully.')
                    time.sleep(10)
                except tweepy.TweepError as error:
                    print('\nError. Unable to tweet:')
                    print(error.reason)

    ##loop retweet
    def loop_retweet(self):
        while True:
            self.retweet()
            print("\n\n Waiting for tweets.....")
            time.sleep(self.loop_retweet_time)


twitter_bot = TwitterBot()
twitter_bot.retweet()
# twitter_bot.loop_retweet()   #uncomment if you want infinte loop of retweet