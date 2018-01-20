
import tweepy
import time

consumer_key = '8ROBF6oXfqKojxSGSPQn9bjBC'
consumer_secret = 'TG8IZiVVsWkAvAW0IuWi7UvQVP4Spkmdh4NawVxpReJQzUfrcM'
access_token = '3241977882-vC0oeIcjrBIU7oRjWLxy3hU35ntsuU7XNBPXWQN'
access_token_secret = 'Xkyzls3T0rD2T5l67o3hMfyQkGWFRzgZYH9Wnkp92m7iO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

hash_tags = ['#IIT_indore','#not_so_prestigious','#bhookhLagiHai ']

for query in hash_tags:
    for tweet in tweepy.Cursor(api.search, q=query).items(5):
        try:
            print('\nTweet by @' + tweet.user.screen_name)
            print('Attempting to retweet')

            tweet.retweet()
            print('Retweet published successfully.')
            time.sleep(10)
        except tweepy.TweepError as error:
            print('\nError. Retweet not successful. Reason: ')
            print(error.reason)
        except StopIteration:
            break
