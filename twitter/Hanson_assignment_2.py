from twitter_util import *
import functools as ft
import statistics as st

#returns list of words that I deem should be exlcluded from sentiment analysis   
def excluded_words():
    return['of','in','to','for','with','on','at','from','by','about','as','into','through','after','the','between', 'over',
    'out','during', 'it', 'this','is','a']
	
#Cleans up text to make it readable to the following functions
def pipeline(text):
    text = text.lower().replace("\t", ' ').replace("\n",' ').split(" ")
    text = ["".join([remove_punct(y,punct=standard_punct_list()) for y in x]) for x in text if x != ' ']
    return text


#Takes in 2 inputs : A set of sentiment coded words and
#a list of text passages. Then returns a dict of {word:sentiment}.
#The sentiment is a normalized score 	
def infer_word_sentiments(codes, text,ex_words = excluded_words()):
    words = set(ft.reduce(lambda x,y : x+y, [pipeline(text)]))
    words = words.difference(ex_words)
    words = words.difference(codes.keys())
    inferred_sentiments = {}
    while words:
        for w in words:
            sents = []
            for t in pipeline(text):
                if w in t:
                    sents.append(sentiment_score(codes,text))
            inferred_sentiments[w] = st.mean(sents)
        return inferred_sentiments
        
#Input: a set of sentiment-coded words (as a dict)
#and a set of tweets (parsed tweets as JSON). 
#This returns a dict of form {word:sentiment}.     
def infer_tweet_word_sentiments(codes, tweets):
    list = []
    for tweet in tweets:
        list.append(tweet['text'])
    return infer_word_sentiments(codes,list)

#Input: a dictionary of form {word:sentiment}, a number n,
# and direction (1 = most positive and 0 = most negative).
# Returns an ordered list of (word, score)
# tuples arranged in highest-magnitude-first order based on the specified direction.    
def top_n_words(sentiment_score_dict, n, direction=1):
    tup = list(sentiment_score_dict.items())
    if direction == 1:
        sort = (sorted(tup, key = lambda x: x[1],reverse=True))
    if direction == 0:
        sort = (sorted(tup, key = lambda x: x[1]))
    return sort[:n]
    
#This uses the above function to get the top n words and then
#produces a one-word-per-line output file that repeats the top n words 
#according to their proportion of the total top n score.     
def build_word_cloud_list(sentiment_score_dict, n, filename, direction=1):
    words = top_n_words(sentiment_score_dict, n, direction)
    file = open(filename,'r')
    for w in words:
        for i in range(int(w[1] * 100)):
            file.write(w[0])
            file.write('\n')
    file.close()
