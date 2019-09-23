import tweepy
from tweepy import OAuthHandler
from datetime import datetime, timedelta

def get_tweets(prod_name):
	consumer_key = input("Enter your API key: ")
	consumer_secret_key = input("Enter your API secret key: ")
	access_token = input("Enter your access token: ")
	access_secret_token = input("Enter your secret access token: ")	

	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret) 
	api = tweepy.API(auth)

	hashtag = '#' + prod_name + '-filter:nativeretweets'
	lastweek = datetime.today().now() - timedelta(days=7)
	lastweek_date = lastweek.strftime('%Y-%m-%d')
	results = tweepy.Cursor(api.search, q = hashtag, tweet_mode = 'extended', lang = 'en', since = lastweek_date).items(50)
	return results



if __name__ == '__main__':
	prod_name = input("Enter hashtag to search: ")
	get_tweets(prod_name)

	
	
	