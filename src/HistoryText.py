import nltk
from nltk import *

def main():

    #"test"
    file = input('Please enter a file to analyze: ')
    f = open(file)
    words = f.read()

    toks = word_tokenize(words)

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
    #print(f.read())

    string = "This is a test. A test like this should be disregarded. Carry on."
    str_bigrams = bigrams(string)
    #for pair in str_bigrams:
    #    print(pair)

    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(word_tokenize(f.read()))
    print(finder.nbest(bigram_measures.pmi, 10))
    """


main()
