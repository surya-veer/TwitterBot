# TwitterBot
This is the simplest twitter bot for retweet.

## Dependencies
 **```tweepy```**<br>
 install via pip<br>
 ```sudo pip install tweepy```
 
## How to use
1. First create App on twitter.<br>
    Visit: http://apps.twitter.com <br>
    **You need a twiter account for this.**
   
2. Generate **consumer_key, consumer_secret, access_token, access_token_secret**.<br>
How to generate Auth token : https://github.com/surya-veer/TwitterBot/blob/master/HOW_TO_GENETARE_TOKEN.md 
<br>
3. Download ```retweet.py``` form my repository.
4. Now exit ```retweet.py``` and enter your **consumer_key, consumer_secret, access_token, access_token_secret** in this script.
5. Finally run **retweet.py** 

## How to edit ```retweet.py```
You can increase ```hash_tag``` in **hast_tag** for retweets.<br>
 Example: <br>
 hash_tag = ['exmaple']<br>
 edit: <br>
 hash_tag = ['example','example2']<br>
 Now ```for``` loop will automatically itrate ```hash_tag```

 You can set retweet time by changing ```retweet_time``` in ```TweetBot``` class
 
 If you want to run this script for a long time then you can uncomment ```tweet.loop_retweet()``` at the end of script. You can aslo specify the time of loop by changing ```loop_retweet_time``` in  ```TweetBot``` class.
 



### Please commit for any changes or bugs :)




  
 

