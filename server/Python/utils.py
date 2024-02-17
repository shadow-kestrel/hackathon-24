from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
# nltk.download('stopwords')
# nltk.download('punkt')

def normalise(token_list):
    normalised = []
    for token in token_list:
        if token.isnumeric():
            normalised.append("NUM")
        elif token[:-2].isnumeric() and token[-2:] in ["st","nd","rd","th"]:
            normalised.append("Nth")
        else:
            normalised.append(token)
    return normalised

def remove_stopwords(token_list):
    stop_punct = stopwords.words('english') + [*'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ .']
    return [token for token in token_list if token not in stop_punct]

def stem(token_list):
    ps = PorterStemmer()
    return[ps.stem(token) for token in token_list]

def canonize(doc):
    doc = word_tokenize(doc)
    doc = normalise(doc)
    doc = remove_stopwords(doc)
    doc = stem(doc)
    return doc

# test_string = "A claw is a curved, pointed appendage found at the end of a toe or finger in most amniotes (mammals, reptiles, birds)."
# print(canonize(test_string))