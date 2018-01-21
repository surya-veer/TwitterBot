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

    # Only iterate through the first 5 statuses
    interate_limit = 5  

    ##time setup in seconds
    retweet_time = 10
    loop_retweet_time = 30*60  #30 min

    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def retweet(self):
        for query in hash_tags:
            for tweet in tweepy.Cursor(self.api.search, q=query).items(interate_limit):
                try:
                    print('\nTweet by @' + tweet.user.screen_name)
                    print('Attempting to retweet')

                    tweet.retweet()
                    print('Retweet published successfully.')
                    time.sleep(10)
                except tweepy.TweepError as error:
                    print('\nError. Unable to tweet:')
                    print(error.reason)

    #update_status
    def tweet(self,status):
        self.api.update_status(status=status,lat='28.6466773',long='76.813073')  #@28.6466773,76.813073 for delhi 

    ##loop retweet
    def loop_retweet(self):
        while True:
            self.retweet()
            print("\n\n Waiting for tweets.....")
            time.sleep(self.loop_retweet_time)


twitter_bot = TwitterBot()
twitter_bot.retweet()
# twitter_bot.loop_retweet()   #uncomment if you want infinte loop of retweet
# twitter_bot.tweet(status = "I am Happy Today!!")    #uncomment if you want to make a tweet or update your status