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

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#you can add more tags.. in hash_tag list
hash_tags = ['#example1','#example2','#example3']

for query in hash_tags:
    for tweet in tweepy.Cursor(api.search, q=query).items(5):
        try:
            print('\nTweet by @' + tweet.user.screen_name)
            print('Attempting to retweet')

            tweet.retweet()
            print('Retweet published successfully.')
            time.sleep(10)
        except tweepy.TweepError as error:
            print('\nError. Unable to tweet:')
            print(error.reason)
            
        except StopIteration:
            break
