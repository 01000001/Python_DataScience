import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def get_score(word, scores):
    if word in scores:
                return scores[word]
    else:
	return 0
		
   
def get_new_terms(word, tweet_score, new_terms):
	new_terms[word] = int(tweet_score)
	return new_terms


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    new_terms = {}
    scores = {}

    for line in sent_file:

	term,score = line.split("\t")
	scores[term] = int(score)

    for line in tweet_file:
	json_tweet = json.loads(line)
#	print json_tweet.keys()	
	if "text" in json_tweet.keys():
	    words_in_tweet = json_tweet["text"].split()
	    total_tweet_score = 0
	    new_words = []
#	    print json_tweet["text"]
	    for word in words_in_tweet:
#		    print word.encode("utf-8").lower()
#		    res = get_score(word.encode("utf-8").lower())
		    res = get_score(word,scores)
		    if res != 0:
			total_tweet_score += res
		    else:
			new_words.append(word)
	    for word in new_words:
		new_terms[word] = total_tweet_score
	    
		    

#	    for word in words_in_tweet:
#		print word
		   
#	    lines(str(json_tweet["text"]))
            
#	    print total_tweet_score

    for element in new_terms:
	print element, new_terms[element]

if __name__ == '__main__':
    main()
