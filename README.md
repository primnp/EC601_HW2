# EC601_HW2
 EC601 A1 Fall 2021. Project 2: Build your own social media analyzer.

## MVP
A web application that tells user the sentiment of tweets from Twitter

## Target user
* A marketing analyst who wants to understand customers behavior
* For general use, a target user can also be anyone who wants to understand sentiment behind specific tweets

## User Stories
* As a marketing analyst, I want to know the sentiment of the text so that I can analyze social media user's feelings.
* As a marketing analyst, I want to have a UI that is easy to use.

**Stretch Goals**
* As a marketing analyst, I want to group social media users together using hashtags.
* As a marketing analyst, I want to see sentiments of different social media user under one hashtag so that I can compare them.
* As a marketing analyst, I want to save social media user's sentiment analysis so I can analyze changes in behavior.

## Modular software design
<p align="center">
Figure 1. Modular software design for social media analyzer web application
<br><img src="/Images/msd.png" width="80%" />
</p>
<br />

## Web UI with Flask
[webapp.py](https://github.com/primnp/EC601_HW2/blob/main/webapp.py) is a Web UI implemented with Flask. The file which incorporates TwitterAPI and Google NLP API is [social_analyzer.py](https://github.com/primnp/EC601_HW2/blob/main/social_analyzer.py). To run the web UI, place both [webapp.py](https://github.com/primnp/EC601_HW2/blob/main/webapp.py) and [social_analyzer.py](https://github.com/primnp/EC601_HW2/blob/main/social_analyzer.py) in the same directory, then do
```
python webapp.py
```

I decided to use Flask as a user interface for social media analyzer application. User can view extracted information from a specified Twitter user, view sentiment scores of tweets from a specified Twitter user, as well as find tweet text associated with a specified hashtag using URI.

Below is the URI for my social media analyzer:

URI  | What it does
------------- | -------------
/soc-analyze/(string:username)/(int:nooftweets)  | View all tweets (within nooftweets limit) data (including tweet texts, tweet likes, tweet posted time, and hashtags) from a specified user (username)
/soc-analyze/(string:username)/(int:nooftweets)/sentiments | View all tweets entities and sentiment scores (within nooftweets limit) from a specified user (username)
/soc-analyze/(string:username)/(int:nooftweets)/hashtag/(string:hashtag) | Find user's tweet text which has the specified hashtag

### Flask Example
1. /soc-analyze/(string:username)/(int:nooftweets)
<p align="center">
Figure 2. View all extracted tweets data from a specified user
<br><img src="/Images/ex1.png" width="80%" />
</p>
<br />
2. /soc-analyze/(string:username)/(int:nooftweets)/sentiments
<p align="center">
Figure 3. View all tweets entities and sentiment scores from a specified user
<br><img src="/Images/ex2.png" width="80%" />
</p>
<br />
3. /soc-analyze/(string:username)/(int:nooftweets)/hashtag/(string:hashtag)
<p align="center">
Figure 4. Find user's tweet text which has the specified hastag
<br><img src="/Images/ex3.png" width="80%" />
</p>
<br />

To handle error conditions, there is a log file (calc.log) which will be created when user runs the flask application. If there is an error, the results returned will be null ([]) and the log file will state that there is an error.

## Future Improvements
In the future, I aim to implement my user stories stretch goal and improve UI so that it will be more user friendly.

## Tests (for Project 3)
The following are **test cases for [social_analyzer.py](https://github.com/primnp/EC601_HW2/blob/main/social_analyzer.py)**

**Sunny day scenarios:**
1. twitter_retrieve function return a dict() of Twitter user data extracted. The dict() should have following key-value:

| Key | Value Type |
| --- | --- |
| Tweets | str |
| Likes | int |
| Time | datetime.datetime |
| Hashtags | list |

2. entities_sentiments function return a dict() of Twitter user data with entities and sentiments analyzed. The dict() should have the following key-value:

| Key | Value Type |
| --- | --- |
| Tweet text | str |
| Tweet Entities | list |
| Twitter's Likes | int |
| Twitter's Posted Time | datetme.datetime |
| Twitter's Hashtags | list |

3. txt_hashtag_retrieve function return an array of texts associated with the hashtag specified

**Rainy day scenarios:**
1. If user input the wrong Twitter user name or if a Twitter username does not exist
2. If user queries for more than 200 tweets per one Twitter user
3. If google cloud authentication failed
4. If Twitter authentication failed
5. If queried array is out of range
6. If user input the wrong type of input 
   * For example: string instead of array, string instead of a number, did not provide an input (None) etc.

All these rainy day scenarios were handled by: if an error occur, the function return an empty array on flask with information on log file on why the error occured

**Unit tests** for social_analyzer.py is [social_analyzer_test.py](https://github.com/primnp/EC601_HW2/blob/main/social_analyzer_test.py)

## Project 2 and 3 Timeline
**Project 2: Phase 1:**

a. Twitter APIs ~~(Due Sunday September 26th)~~ ***DONE***
  * Write test programs to exercise different twitter APIs.  For example, retrieving tweets, searching per time, hashtags, etc.
  * All your programs should be on GitHub including a README file explaining your tests and results.

b. Google NLP ~~(Due Wednesday September 29th)~~  ***DONE***
  * Write test programs to exercise different Google NLP APIs.  Focus on Sentiment analysis.
  * All your programs should be on GitHub including a README file explaining your tests and results.

**Project 2: Phase 2:**
* Define MVP and user stories ~~(Due Sunday October 3rd)~~ ***DONE***
* Translate user stories to a modular design ***DONE***
* Who is your user? ***DONE***
* What are the basic user stories? ***DONE***


**Overall Completion:**  Sunday October 10th

---

**Project 3a** ~~(Due Date:  October 29th)~~ ***DONE***
* Write Tests for your Project 2
* Write Unit tests for Project 2
  * Learn how to use Actions
  * Learn how to use Python Unit Tests

--- 

Notes:
* Error conditions
  * What happens if twitter is not responding
  * What happens if I pass the wrong handle
  * What happens if Google NLP API does not respond back

* Data back and forth
  * What do I send?
  * What do I get?
  * What is the format of the data?
  * How can I use such data?
