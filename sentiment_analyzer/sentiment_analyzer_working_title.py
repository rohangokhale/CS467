import sentiment_analyzer_lib.settings as settings
import sentiment_analyzer_lib.sentiment_analyzer_config as  config
import csv
import re

#remove extra words, such as 'the' and 'and'
def optimize_tweet_text(tweet_text):
	tweet_text = tweet_text.lower()
	#remove pronouns, prepositions, conjunctions, etc
	return tweet_text

#retrive show name
def get_show_name(tweet_text):
	for i in settings.TRACK_TERMS:
		if i.lower() in tweet_text:
			return i.lower()
	return False

#get show sentiment, return a number
def get_show_sentiment(tweet_text):
	return 0

#analyze tweet, return state, show name, and sentiment score
def tweet_analyzer(tweet_data):
	try:#error control in case we get invalid states, we want to return false
		tweet_text = tweet_data.split("\t")[config.TWEET_TEXT_COLUMN].strip()
		tweet_state = tweet_data.split("\t")[config.TWEET_STATE_COLUMN].strip()
		if tweet_state == "" or tweet_text == "":
			return False
	except IndexError:
		return False

	tweet_text = optimize_tweet_text(tweet_text)#could do one line, want it readable
	show_name = get_show_name(tweet_text)#get show name; may not be efficient memory-wise to do this way but makes easier to read

	if show_name == False or tweet_state == False:
		return False

	with open(config.SENTIMENT_DICTIONARY) as sentiment_dictionary:
		reader = csv.reader(sentiment_dictionary,delimiter=' ')
		for row in reader:
			usable_row = row[0].split(",")#convert row into a list so we can check if tweet word is in there, get the sentiment
			if re.search(r"\b" + re.escape(usable_row[1]) + r"\b", tweet_text):#use regex since we need whole words-http://stackoverflow.com/questions/4154961/find-substring-in-string-but-only-if-whole-words
				print(usable_row[1] + ": " + usable_row[2])


	show_sentiment = get_show_sentiment(tweet_text)
#	if show_sentiment == 0:
		#send show text to another file, so we can examine for possible addition to dictionary

	#put sentiment, show name and state into results


