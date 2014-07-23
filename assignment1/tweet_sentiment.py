import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def get_score(word):
    afinnfile = open(sys.argv[1])
    for line in afinnfile:
        scores = {}
        term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score) # Convert the score to an integer.
#       print scores.items()
	if word in scores:
                return scores[word]
		


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    for line in tweet_file:
	json_tweet = json.loads(line)
#	print json_tweet.keys()	
	if "text" in json_tweet.keys():
	    words_in_tweet = json_tweet["text"].split()
	    total_tweet_score = 0
#	    print json_tweet["text"]
	    for word in words_in_tweet:
		    res = get_score(word)
		    if type(res) == int:
			total_tweet_score += get_score(word)
#	    for word in words_in_tweet:
#		print word
		   
#	    lines(str(json_tweet["text"]))
            
	    print total_tweet_score

if __name__ == '__main__':
    main()
