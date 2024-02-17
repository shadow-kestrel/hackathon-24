import nltk
import spacy

from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def get_tf(term, document):

    delimiter = " "
    term_normalized = delimiter.join(utils.canonize(term))

    # print(term_normalized)

    numOfAppearancesInDoc = document.count(term_normalized)
    totalNumOfTermsInDoc = len(document)

    # print("NumOfAppearancesInDoc: {}".format(numOfAppearancesInDoc))
    # print("TotalNumOfTermsInDoc: {}".format(totalNumOfTermsInDoc))
  
    if (totalNumOfTermsInDoc != 0):
        return numOfAppearancesInDoc / totalNumOfTermsInDoc
    else:
        return 0
    
def get_idf(term, corpus):

    delimiter = " "
    term_normalized = delimiter.join(utils.canonize(term))

    numOfDocsInCorpus = len(corpus)
    numOfAppearrancesInCorpus = 0
    
    for document in corpus:
        
        if term_normalized in document:
            
            numOfAppearrancesInCorpus += 1

    # print(numOfAppearrancesInCorpus)

    if (numOfAppearrancesInCorpus != 0):
        return numOfDocsInCorpus / numOfAppearrancesInCorpus
    else:
        # Return high IDF value as the term is very uncommon
        return 10000

def get_tfidf(term, document, corpus):

    # print(get_tf(term, document))
    # print(get_idf(term, corpus))

    return get_tf(term, document) * get_idf(term, corpus)

def get_keywords(sentence, corpus, numOfKeywords = 10):

    

    # Get the most frequent named entities (Using the raw string here for better entity recognition)
    doc = nlp(sentence)
    named_entities = GetNamedEntities(doc)

    entityCounts = {}

    for entity in named_entities:
        if entity not in entityCounts:
            entityCounts[entity] = sentence.count(entity)




    # Get the most popular terms that are not entities
    normalized_sentence = utils.canonize(RemoveNamedEntities(sentence, named_entities))
    
    mostRelevantWords = {}


    for term in normalized_sentence:
        if term not in mostRelevantWords:

            pos_tag = nltk.pos_tag(word_tokenize(term))[0][1]

            mostRelevantWords[term] = [get_tfidf(term, normalized_sentence, corpus), pos_tag]
    
    return dict(sorted(mostRelevantWords.items(), key=lambda item: item[1], reverse=True)[:5]), dict(sorted(entityCounts.items(), key=lambda item: item[1], reverse=True)[:5])