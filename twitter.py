import tweepy
from tweepy import OAuthHandler
from datetime import datetime, timedelta
from nltk.tokenize import WordPunctTokenizer

consumer_key = ''
consumer_secret_key = ''
access_token = ''
access_secret_token = ''	


def get_tweets(prod_name):
	
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret) 
	api = tweepy.API(auth)

	hashtag = '#' + prod_name + '-filter:nativeretweets'
	lastweek = datetime.today().now() - timedelta(days=7)
	lastweek_date = lastweek.strftime('%Y-%m-%d')
	results = tweepy.Cursor(api.search, q = hashtag, tweet_mode = 'extended', lang = 'en', since = lastweek_date)
	
	for tweet in results:
		encoded_tweet = tweet.text.encode('utf-8')
		rem_user = re.sub(r'@[A-Za-z0-9]+','',encoded_tweet.decode('utf-8'))
		rem_num  = re.sub('[^a-zA-Z]', ' ', rem_user)
		tok = WordPunctTokenizer()
	    words = tok.tokenize(rem_num)
	    tweets_updated = (' '.join(words)).strip()	
	
	return tweets_updated





 



if __name__ == '__main__':
	prod_name = input("Enter hashtag to search: ")
	get_tweets(prod_name)

	
	
	