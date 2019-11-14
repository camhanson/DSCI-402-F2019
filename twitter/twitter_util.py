# ---------------------------------------------------------------------
# Author: cgarcia
# About: This provides a few basic utilities for reading tweets from 
#        json-based tweet files. 
# ---------------------------------------------------------------------

import json

# Read in a properties file (key:val pairs) and return a corresponding dict.
def read_props(filename, sep = '='):
	whitespace = [" ", "\t", "\n"]
	clean = lambda x: ''.join([y for y in x if not(y in whitespace)]) #filter(lambda y: not(y in whitespace), x)
	split = lambda x: tuple(clean(x).split(sep))
	return dict(map(split, open(filename, 'r').readlines()))
	
# Read tweets as JSON objects from a file of json tweets.	
def read_tweets(filename):	
	data = open(filename, 'r').read().decode().split("\n")
	tweets = []
	for line in data:
		try:
			tweets.append(json.loads(line.strip()))
		except:
			print("JSON-unopenable tweet encountered")
	return tweets

# For a file of tweets, extract out the text portion of each.
def read_texts(filename):
	tweets = read_tweets(filename)
	text = []
	for tweet in tweets:
		try:
			text.append(unicode(tweet['text']).encode('ascii', 'ignore'))
		except:
			1 == 1
	return text

# Extract the specified object(by 'path') from the json tweet (as text where possible).
# The path is like a file path in the form of a list. If the path is
# only one level deep you don't need to put in a list. 
def get(json_tweet, path = 'text'):
	if type(path) != type([]):
		path = [path]
	try:
		depth = 0
		curr_obj = json_tweet
		while depth < len(path):
			curr_obj = curr_obj[path[depth]]
			depth += 1
		try:
			return str(curr_obj).encode('ascii', 'ignore')
		except:
			return curr_obj
	except:
		return None
        
#returns list of commonly-used punctuation.
def standard_punct_list():
    return ['.','?',',','-',"'",'"',';',':','/',"\t","\n",'!']
    
#returns a space if a character is deemed to be punctuation
def remove_punct(char, punct):
    if char in punct:
        return ''
    return char
    
#reads in a file of sentiment code words and parses out into a dict
def get_sentiment_codes(filename):
    lines = open(filename,'r').readlines()
    codes = {}
    for line in lines:
        words = line.lower().strip().replace("\t", ' ').replace("\n",' ').split(' ')
        words = [x for x in words if x != '']
        code = float(words[len(words)-1])
        codes[words[0]] = code
    return codes

#-----------------------------------------------------------------------------------------
#The following was worked on in class
#For a passage of text, build a tuple of form
#(total_word_count, sentiment_word_count,sentiment_score_sum)
def sentiment_tuple(codes,text,punct=standard_punct_list()):
    text = text.lower().replace("\t", ' ').replace("\n",' ').split(" ")
    text = ["".join([remove_punct(y,punct) for y in x]) for x in text if x != ' ']
    total_word_count = 0
    sentiment_word_count = 0
    sentiment_score_sum = 0
    for t in text:
        total_word_count += 1
        if t in codes:
            sentiment_word_count += 1
            sentiment_score_sum += codes[t]
    return total_word_count, sentiment_word_count, sentiment_score_sum
    
#Compute the normalized/standardized sentiment score for a given text.
#normalize_sentiment_words specifieds whether to use only sentiment words(versus all words) to compute the normalization.
#Normalizes scores to range from -1(very negative) to 1(very positive)
def sentiment_score(codes, text, normalize_sentiment_words = True, punct = standard_punct_list(), max_code_score = None):
    if max_code_score == None:
        max_code_score = max(codes.values())
    total_word_count, sentiment_word_count, sentiment_score_sum = sentiment_tuple(codes, text,punct)
    if total_word_count == 0 or sentiment_word_count == 0:
        return 0
    if normalize_sentiment_words:
        return sentiment_score_sum/(max_code_score*sentiment_word_count)
    else:
        return  sentiment_score_sum/(max_code_score*total_word_count)
        
            
            
         
	
	
	
	