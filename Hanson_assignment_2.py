#reads in a file of sentiment code words and parses out into a dict(created in class with professor
def get_sentiment_codes(filename):
    lines = open(filename,'r').readlines()
    codes = {}
    for line in lines:
        words = line.lower().strip().replace("\t", ' ').replace("\n",' ').split(' ')
        words = [x for x in words if x != '']
        code = float(words[len(words)-1])
        codes[words[0]] = code
    return codes
    
#returns list of commonly-used punctuation (created by professor)
def standard_punct_list():
    return ['.','?',',','-',"'",'"',';',':','/',"\t","\n",'!']

#returns a space is a character is deemed to be punctuation
def remove_punct(char, punct):
    if char in punct:
        return ''
    return char
    
#returns list of words that I deem should be exlcluded from sentiment analysis   
def excuded_words():
    return['of','in','to','for','with','on','at','from','by','about','as','into','through','after','the','between', 'over',
    'out','during', 'it']
    
#returns a space if a word is deemed excluded
def remove_word(char, excluded_words):
    if char in punct:
        return ''
    return char
    
#Takes in 2 inputs. 1) A set of sentiment coded words and 2)a list of text passages. Then returns a dict of {word:sentiment}  
def infer_word_sentiments(codes, text):
    text = text.lower().replace("\t", ' ').replace("\n",' ').split(" ")
    sentiment_word_count = 0
    sentiment_score_sum = 0
    for t in text:
        if t in codes:
            sentiment_word_count += 1
            sentiment_score_sum += codes[t]
        if t not in codes:
            word = t
            sentiment = sentiment_score_sum/sentiment_word_count
            dict={word:sentiment}
    return dict
    
codes = get_sentiment_codes(".../data_files/AFINN-111.txt")   
print(infer_word_sentiments(codes, "THIS is a HaPpY String!"))