# EC601 - MINI PROJECT 1: Sentiment-Analyser

This project is developed to analyse Twitter feeds and give an averall report of the sentiments/reviews of the people on a specific product or item which in turn is motivated from a User Story.

### USER STORIES:

As a company owner, I want to get feedback through sentiment analysis from twitter users' relevent posts.

As a company owner, I want to manuficature and make more popular and better products to the market. 

Then I could use this data to reviewing users' reviews and opinions.

a). Improve our product by getting the drawbacks from feedback

b). Get to know the popularity of my own product.

### MVP

Our MVP is combining Tweeter api and Google language api and use them to analyse users' sentiment. User data are grabbed from tweeter by using tweeter api and put into Google natural language api to analyse the sentiment of eaach commect them give for a certain product. We use "clean tweets" and keywords to find tweets that focuses on a certain type of product. By doing this we get feedbacks and use it to improve the product.
 
### LESSON WE LEARNED

1. What you liked doing?

We would like to do my coding and working on user stories, especially brain storming.

2. What you could have done better?

If we had down better on planning and had better coding capability, we might have done btter on this project.

3. What you will avoid in the future?

We will not put things to the end of deadline and we will try to have better discussion and communication on methods when we are completing a project.

### WORK DIVISION:
* Samyak is working on Twitter API to extract and clean the data from twitter feeds to get useful data for analysis.
* Zhinchao is working with the Google NLP ALI to analyse the data from Twitter API and give the final sentiment analysis.

### SPRINTS:
* SPRINT 1:
1. Define User Stories
2. Learn how to use GitHub and create a GitHub repository
3. Learn about Google NLP API and Twitter API and get access to authentication keys
4. Design a basic layout of the product based on the use stories

* SPRINT 2:
1. Divide the work 
2. Script for getting tweets from twitter feed
3. Script to analyse these tweets

* SPRINT:
1. Combine both the scripts designed in Sprint 2 to create the final product
2. Update the final system architecture

### PYTHON LIBRARIES USED:
To run this sentiment analysis app, the following libraries are required to be imported:
1. Google Cloud for Google NLP API
2. Tweepy for Twitter API
3. argparse for user-friendly interface

### ARCHITECTURE:
This app is designed by incorporating the Twitter API and the Google Natural Language API. 
Python programming language is used here to write the code for this app. The code is divided into three different files:
- main.py: This is python script which is used to run the Sentiment Analyser. It interacts with the files twitter.py and google_nlp.py.
- twitter.py: This python script is used to extract twitter feeds based on a search parameter(a keyword), clean them so that they can be analysed using the Google NLP API. 
- google_nlp.py: This python script uses the Google NLP API to work on the extracted and cleaned data using the 	  Twitter API and analyses it for sentiments to give an emotional review towards the product.



	
	
