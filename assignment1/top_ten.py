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
	if "entities" in json_tweet.keys():
	    entities_in_tweet = json_tweet["entities"]
	    if "hashtags" in entities_in_tweet:
                hastags_in_tweet = entities_in_tweet["hashtags"]
#                print hastags_in_tweet
                for element in hastags_in_tweet:
                    if "text" in element:
                        hashtag = element["text"]
                        if hashtag in words:
                            words[hashtag] = {'freq': words[hashtag]['freq'] + 1}
                        else:
                            words[hashtag] = {'freq': 1}
#	    for word in entities_in_tweet:
#		    print word.encode("utf-8").lower()
#		    res = get_score(word.encode("utf-8").lower())
#		    if word in words:
#			words[word] = {'freq': words[word]['freq'] + 1}
#		    else:
#			words[word] = {'freq': 1}
    total_freq = 0
    for element in words:
	total_freq += words[element]['freq']

    sorted_words = sorted(words, key=words.get)

    for i in range(10):
        element = sorted_words[-1-i]
#        print element, words[element]['freq']/float(total_freq)
        print element, words[element]['freq']
#    for element in words:
#	print element, words[element]['freq']/float(total_freq)
#        print element, words[element]['freq']
#    print total_freq

if __name__ == '__main__':
    main()
