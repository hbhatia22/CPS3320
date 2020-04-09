import json
import pandas as pd
import tweepy
from tweepy import OAuthHandler


# keys and tokens for OAuth
access_token = '726110104450375681-UvSnhAIk5MgvCHwKXivyxMGvSjKdJEP'
access_token_secret = 'r7sdpc1f5I3aLH7IydCNgGbJNaMudT2vPZTmxCSxd6L7j'
consumer_key = '8GiZTIYk1QpVsZVtA1iK7suD7'
consumer_secret = 'UbWa0PwsDFnqE00KVKZg5havC4lhisKotjmSE8a9jLCzldeXBj'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

search_word = '#COVID19'
date_since = '2020-4-1'

#search tweets with hashtag covid19
tweets = tweepy.Cursor(api.search,
    q=search_word,
    lang='en',
    since=date_since).items(15)

#print(tweets)

for tw in tweets:
    print(tw.text)

print('\n\nEnd of tweets \n\n\n\n\n')
# remove retweets from our search results to avoid duplicate tweets
filter_search_words = search_word + ' -filter:retweets'

new_tweets = tweepy.Cursor(api.search,
        q=filter_search_words,
        lang='en',
        since=date_since).items(15)

for tw in new_tweets:
    print(tw.text)

print('\n\nEnd of tweets \n\n\n\n\n')

# get the information about who is sending these tweet
# and from where are these being sent

#users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in new_tweets]
#print(users_locs)

# storing user_locations in pandas dataframe
# tweet_text = pd.DataFrame(data=users_locs,columns=['user','location'])

# print(tweet_text)