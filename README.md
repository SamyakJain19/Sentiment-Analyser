# EC601 - MINI PROJECT 1: Sentiment-Analyser

This project is developed to analyse Twitter feeds and give an averall report of the sentiments/reviews of the people on a specific product or item which in turn is motivated from a User Story.

## SPRINTS:
	-Sprint 1:
	1. Define User Stories
	2. Learn how to use GitHub and create a GitHub repository
	3. Learn about Google NLP API and Twitter API and get access to authentication keys
	4. Design a basic layout of the product based on the use stories
	
	



PYTHON LIBRARIES USED:
To run this sentiment analysis app, the following libraries are required to be imported:
1. Google Cloud for Google NLP API
2. Tweepy for Twitter API
3. argparse for user-friendly interface

ARCHITECTURE:
This app is designed by incorporating the Twitter API and the Google Natural Language API. 
Python programming language is used here to write the code for this app. The code is divided into three different files:
-main.py: This is python script which is used to run the Sentiment Analyser. It interacts with the files twitter.pyand google_nlp.py.
-twitter.py: This python script is used to extract twitter feeds based on a search parameter(a keyword), clean them so that they can be analysed using the Google NLP API. 
-google_nlp.py: This python script uses the Google NLP API to work on the extracted and cleaned data using the 	  Twitter API and analyses it for sentiments to give an emotional review towards the product.



	
	
