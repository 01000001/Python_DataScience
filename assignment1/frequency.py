import sys
import json

def lines(fp):
    print str(len(fp.readlines()))
		

def main():
    tweet_file = open(sys.argv[1])
    words = {}

    for line in tweet_file:
	json_tweet = json.loads(line)
#	print json_tweet.keys()	
	if "text" in json_tweet.keys():
	    words_in_tweet = json_tweet["text"].split()
	    for word in words_in_tweet:
#		    print word.encode("utf-8").lower()
#		    res = get_score(word.encode("utf-8").lower())
		    if word in words:
			words[word] = {'freq': words[word]['freq'] + 1}
		    else:
			words[word] = {'freq': 1}
    total_freq = 0
    for element in words:
	total_freq += words[element]['freq']
    for element in words:
	print element, words[element]['freq']/float(total_freq)

#    print total_freq

if __name__ == '__main__':
    main()
