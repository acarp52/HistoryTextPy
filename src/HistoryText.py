import nltk
import os
import string
import re
import csv
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

        with open('ug.csv', 'w') as csvfile:
            fieldnames = ['word', 'frequency']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for ug in unifd.most_common(5):
                print(ug)
                writer.writerow({'word': ug[0], 'frequency': ug[1]})

        print(unifd.most_common(5))
        print('\n')

        bifd = nltk.FreqDist(mybi)

        with open('bg.csv', 'w') as csvfile:
            fieldnames = ['word1', 'word2', 'frequency']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for bg in bifd.most_common(5):
                print(bg)
                writer.writerow({'word1': bg[0][0], 'word2': bg[0][1], 'frequency': bg[1]})

        print(bifd.most_common(5))
        print('\n')
        #
        # trifd = nltk.FreqDist(mytri)
        # print(trifd.most_common(5))
        # print('\n')
        #
        # tetrafd = nltk.FreqDist(mytetra)
        # print(tetrafd.most_common(5))

        return bifd.most_common(5)

"""
Processes a string made from a raw input file and removes punctuation
and stop words. Returns a string with the cleaned data
"""
def process(rawFile):
    #sentence = sentence.lower()
    # pattern = r'''(?x)               # set flag to allow verbose regexps
    #           ([A-Z]\.)+         # abbreviations, e.g. U.S.A.
    #           | \$?\d+(\.\d+)?%? # numbers, incl. currency and percentages
    #           | \w+([-']\w+)*    # words w/ optional internal hyphens/apostrophe
    #           | [+/\-@&*]        # special characters with meanings
    #         '''
    # tokenizer = RegexpTokenizer(pattern) #need to account for apostrophe
    tokenizer = RegexpTokenizer(r'\w+') #need to account for apostrophe
    # tokenizer = RegexpTokenizer(r"\w+([-']\w+)* | \w+") #need to account for apostrophe
    tokens = tokenizer.tokenize(rawFile)
    filtered_words = [w for w in tokens if not w in stopwords.words('english')]
    #filtered_words = filter(lambda token: token not in stopwords.words('english'), tokens)
    #print(filtered_words)
    return " ".join(filtered_words)

def readfile(f):
    words = ""
    with open(f) as input_data:
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
    return words

def scandir():
    path = r'C:\Users\acarp_000\PycharmProjects\HistoryText\training_data'  # remove the trailing '\'
    data = []
    for dir_entry in os.listdir(path):
        dir_entry_path = os.path.join(path, dir_entry)
        if os.path.isfile(dir_entry_path):
            data.append(dir_entry_path)

    return data

def main():
    ofile  = open('out.csv', "wb")
    writer = csv.writer(ofile, delimiter='\t')




    d = scandir()
    for file_path in d:
        try:
            words = readfile(file_path)
            tok = word_tokenize(process(words))
            bg = make_tokens(tok)
            # for x in bg:
            #     print('{0} occurs {1} times'.format(x[0], x[1]))



            # print(list(bg))
            # print(words)
        except UnicodeDecodeError:
            print("File could not be read.")

main()
