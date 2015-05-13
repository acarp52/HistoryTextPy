import nltk
import string
import re
from nltk import *
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

"""
Takes a list of tokenized input strings and creates unigrams, bigrams, trigrams,
and tetragrams. It then prints the results.
"""
def make_tokens(toks):
        myuni = toks
        mybi = bigrams(toks)
        mytri = trigrams(toks)
        mytetra = ngrams(toks,4)

        unifd = nltk.FreqDist(myuni)
        print(unifd.most_common(5))
        print('\n')

        bifd = nltk.FreqDist(mybi)
        print(bifd.most_common(5))
        print('\n')

        trifd = nltk.FreqDist(mytri)
        print(trifd.most_common(5))
        print('\n')

        tetrafd = nltk.FreqDist(mytetra)
        print(tetrafd.most_common(5))

"""
Processes a string made from a raw input file and removes punctuation
and stop words. Returns a string with the cleaned data
"""
def process(rawFile):
    #sentence = sentence.lower()
    tokenizer = RegexpTokenizer(r'\w+') #need to account for apostrophe
    tokens = tokenizer.tokenize(rawFile)
    filtered_words = [w for w in tokens if not w in stopwords.words('english')]
    #filtered_words = filter(lambda token: token not in stopwords.words('english'), tokens)
    #print(filtered_words)
    return " ".join(filtered_words)

def main():
    file = input('Please enter a file to analyze: ')
    words = ""

    with open(file) as input_data:
        # Skips text before the beginning of the interesting block:
        for line in input_data:
            match = re.search(r"^[***](.*)[***]$", line)
            if match:
                break
        # Reads text until the end of the block:
        for line in input_data:  # This keeps reading the file
            match = re.search(r"^[***](.*)[***]$", line)
            if match:
                break
            words += line   #appends to a string for the data in the file we are interested in

    """
    rTokenizer = RegexpTokenizer(r'\w+')
    rTokenizer.tokenize('Eighty-seven miles to go, yet.  Onward!')
    """

    #myuni = toks
    #mybi = bigrams(toks)
    #mytri = trigrams(toks)
    #mytetra = ngrams(toks,4)



    tok = word_tokenize(process(words))
    make_tokens(tok)

main()
