import utils

'''
with open("tweets.txt", "r") as tweets:
    tweet_list = tweets.read().split("\n")
    
    for line in tweets.read().split("\n"):
        
        token_list = []
        for token in line.split():
            token_list.append(token)
        
        tweet_list.append(line)
    
normalised_tweets = [utils.canonize(tweet) for tweet in tweet_list]
print(normalised_tweets[:5])

normalised_tweets = [" ".join(tweet) for tweet in normalised_tweets]

print(normalised_tweets[:5])

with open("normalised_tweets.txt", "w") as file:
    doc = ""
    for tweet in normalised_tweets:
        doc += tweet
        doc += "\n"
    file.write(doc)
'''
normalised_tweets = []

with open("normalised_tweets.txt", "r") as file:
    for line in file.read().split("\n"):
        normalised_tweets.append(line.split())

sentence = "Tried a fucking awful new recipe for dinner"

def catify(sentence):
    keywords = utils.get_keywords(sentence, normalised_tweets)
    sentiment = utils.GetSentiment(sentence)
    return (keywords, sentiment)

print(catify(sentence))