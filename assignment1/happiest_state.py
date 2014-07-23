import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def get_score(word, scores):
    if word in scores:
                return scores[word]["score"]
    else:
	return word
		
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    satets_tweet_score = {}
    total_scores = {}

    for line in sent_file:

	term,score = line.split("\t")
	scores[term] = {"score": int(score)}

    for line in tweet_file:
	json_tweet = json.loads(line)
#	print json_tweet.keys()
	if "text" in json_tweet.keys():
	    words_in_tweet = json_tweet["text"].split()
	    total_tweet_score = 0
	    new_words = []

	    
	    for word in words_in_tweet:
		    res = get_score(word,scores)
		    if type(res) == int:
			total_tweet_score += res
		    else:
			new_words.append(word)
			scores[word] = {'score': total_tweet_score}
	    for word in new_words:
                if word not in scores:
        		scores[word] = {'score': total_tweet_score}

            if json_tweet["place"]:
                country_code = json_tweet["place"]["country_code"]
                if country_code and country_code == "US":
                    if "," in json_tweet["place"]["full_name"]:
                        state = json_tweet["place"]["full_name"].split(",")[1][1:]
                        
                        if state in satets_tweet_score:
                            satets_tweet_score[state] = {'score': total_tweet_score, 'freq': satets_tweet_score[state]['freq'] + 1}
                        else:
                            satets_tweet_score[state] = {'score': total_tweet_score, 'freq': 1}
        for element in satets_tweet_score:
            if element not in total_scores:
                total_scores[element] = {'score': satets_tweet_score[state]['score'], 'freq': satets_tweet_score[state]['freq']}
            else:
                total_scores[element] = {'score': total_scores[element]['score'] + satets_tweet_score[state]['score'], "freq": total_scores[element]['freq'] + satets_tweet_score[state]['freq'] }

    best = {"score": 0}

    del total_scores["USA"]
    
    for element in total_scores:
    
        test = {"state": element, "score": total_scores[element]['score']/float(total_scores[element]['freq'])}

        if test["score"] > best["score"]:
            best = test

    print best["state"]
    #, best["score"]


    


#	print total_tweet_score
#
#    for element in scores:
#	print element, scores[element]

if __name__ == '__main__':
    main()
