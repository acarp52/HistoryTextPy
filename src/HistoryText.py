import nltk
import os
import string
import re
import csv
from nltk import *
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet

"""
Takes a list of tokenized input strings and creates unigrams, bigrams, trigrams,
and tetragrams. It then prints the results.
"""
def make_tokens_test(toks):
    year = "test"

    myuni = toks
    mybi = bigrams(toks)
    mytri = trigrams(toks)
    mytetra = ngrams(toks,4)

    unifd = nltk.FreqDist(myuni)

    with open('out/{0}/1g.csv'.format(year), 'w', newline='') as csvfile:
        fieldnames = ['word1', 'frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        for ug in unifd.most_common(10):
            # print(ug)
            writer.writerow({'word1': ug[0], 'frequency': ug[1]})


    # print(unifd.most_common(5))
    # print('\n')
    print("Unigrams complete for {0}".format(year))

    bifd = nltk.FreqDist(mybi)

    with open('out/{0}/2g.csv'.format(year), 'w', newline='') as csvfile:
        fieldnames = ['word1', 'word2', 'frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()

        for bg in bifd.most_common(10):
            # print(bg)
            writer.writerow({'word1': bg[0][0], 'word2': bg[0][1], 'frequency': bg[1]})

    # print(bifd.most_common(5))
    # print('\n')
    print("Bigrams complete for {0}".format(year))


    trifd = nltk.FreqDist(mytri)
    with open('out/{0}/3g.csv'.format(year), 'w', newline='') as csvfile:
        fieldnames = ['word1', 'word2', 'word3', 'frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()

        for trig in trifd.most_common(10):
            # print(trig)
            writer.writerow({'word1': trig[0][0], 'word2': trig[0][1], 'word3': trig[0][2], 'frequency': trig[1]})
    # print(trifd.most_common(5))
    # print('\n')
    print("Trigrams complete for {0}".format(year))


    tetrafd = nltk.FreqDist(mytetra)
    with open('out/{0}/4g.csv'.format(year), 'w', newline='') as csvfile:
        fieldnames = ['word1', 'word2', 'word3', 'word4', 'frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()

        for tetrag in tetrafd.most_common(10):
            # print(tetrag)
            writer.writerow({'word1': tetrag[0][0], 'word2': tetrag[0][1], 'word3': tetrag[0][2], 'word4': tetrag[0][3], 'frequency': trig[1]})
    # print(tetrafd.most_common(5))
    print("Tetragrams complete for {0}".format(year))


    return "Analysis finished for {0}".format(year)

def make_tokens(toks, year):
    if year == "xxxx":
            return make_tokens_test(toks)

    myuni = toks
    mybi = bigrams(toks)
    mytri = trigrams(toks)
    mytetra = ngrams(toks,4)

    unifd = nltk.FreqDist(myuni)

    with open('out/{0}/1g.csv'.format(year), 'w', newline='') as csvfile:
        fieldnames = ['word', 'frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        for ug in unifd.most_common(10):
            # print(ug)
            writer.writerow({'word': ug[0], 'frequency': ug[1]})


    # print(unifd.most_common(5))
    # print('\n')
    print("Unigrams complete for {0}".format(year))

    bifd = nltk.FreqDist(mybi)

    with open('out/{0}/2g.csv'.format(year), 'w', newline='') as csvfile:
        fieldnames = ['word1', 'word2', 'frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()

        for bg in bifd.most_common(10):
            # print(bg)
            writer.writerow({'word1': bg[0][0], 'word2': bg[0][1], 'frequency': bg[1]})

    # print(bifd.most_common(5))
    # print('\n')
    print("Bigrams complete for {0}".format(year))


    trifd = nltk.FreqDist(mytri)
    with open('out/{0}/3g.csv'.format(year), 'w', newline='') as csvfile:
        fieldnames = ['word1', 'word2', 'word3', 'frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()

        for trig in trifd.most_common(10):
            # print(trig)
            writer.writerow({'word1': trig[0][0], 'word2': trig[0][1], 'word3': trig[0][2], 'frequency': trig[1]})
    # print(trifd.most_common(5))
    # print('\n')
    print("Trigrams complete for {0}".format(year))


    tetrafd = nltk.FreqDist(mytetra)
    with open('out/{0}/4g.csv'.format(year), 'w', newline='') as csvfile:
        fieldnames = ['word1', 'word2', 'word3', 'word4', 'frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()

        for tetrag in tetrafd.most_common(10):
            # print(tetrag)
            writer.writerow({'word1': tetrag[0][0], 'word2': tetrag[0][1], 'word3': tetrag[0][2], 'word4': tetrag[0][3], 'frequency': trig[1]})
    # print(tetrafd.most_common(5))
    print("Tetragrams complete for {0}".format(year))


    return "Analysis finished for {0}".format(year)

"""
Processes a string made from a raw input file and removes punctuation
and stop words. Returns a string with the cleaned data
"""
def process(rawFile):

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

def scandir(folder):
    path = r'C:\Users\acarp_000\PycharmProjects\HistoryText\{0}'.format(folder)  # remove the trailing '\'
    data = []
    for dir_entry in os.listdir(path):
        dir_entry_path = os.path.join(path, dir_entry)
        if os.path.isfile(dir_entry_path):
            data.append(dir_entry_path)

    return data

def build_model():
    d = scandir("training_data")
    for file_path in d:
        try:
            words = readfile(file_path)
            # print(file_path[61:65])     # retrieves pub year from title
            tok = word_tokenize(process(words))
            print(make_tokens(tok, file_path[61:65]))
            print()
        except UnicodeDecodeError:
            print("File for {0} could not be read.".format(file_path[61:65]))

def main():
    # ofile  = open('out.csv', "w", newline='')
    # writer = csv.writer(ofile, delimiter='\t', lineterminator='\n')

    """
    print("Please select a task, or enter h for help:")
    print("1 - Train language model")
    print("2 - Test  language model")
    print("3 - Try a specific file")
    """

    build_model()


    newfile = input("Please enter the file you would like to test: ")
    words = readfile(newfile)
    tok = word_tokenize(process(words))
    print(make_tokens(tok, "xxxx"))

    test_list = scandir("src/out/test")
    # print(test_list)

    rootdir = r'C:\Users\acarp_000\PycharmProjects\HistoryText\src\out'
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            # print(os.path.join(subdir, file))
            # print(file)
            with open(os.path.join(subdir, file), newline='') as csvfile, open(rootdir+'/test/{0}'.format(file)) as testfile:
                print("File = " + file)
                reader = csv.reader(csvfile)
                readertest = csv.reader(testfile)
                next(reader, None)
                row2 = next(readertest, None)
                for row in reader:
                    # row2 = next(readertest, None)
                    print("Current test row: "+ row2)
                    print("Current Data row: "+ row2)

                    for i in range(0, len(row)):
                        avg = 0
                        if row[i].isdigit():
                            break
                        else:
                            # print(i)

                            try:
                                TAG = nltk.pos_tag(row[i])
                                POS = TAG[0][1]
                                if POS == "NN":
                                    POS = 'n'
                                    t1 = wordnet.synset(row2[i] + '.n.01')
                                    tes = wordnet.synset(row[i] + '.n.01')
                                    # print(wordnet.path_similarity(tes, t1))
                                    avg += wordnet.path_similarity(tes, t1)
                                elif POS == "VB":
                                    POS = 'v'
                                    t2 = wordnet.synset(row2[i] + '.v.01')
                                    tes = wordnet.synset(row[i] + '.v.01')
                                    # print(wordnet.path_similarity(tes, t2))
                                    avg += wordnet.path_similarity(tes, t2)
                                else:
                                    break
                            except nltk.corpus.reader.wordnet.WordNetError:
                                # print("whoops")
                                pass

                        print(row2[i] + ": similarity = " + str(avg))
                        row2 = next(readertest, None)

                        """
                        try:
                            hit = wordnet.synset('me.n.01')
                            tes = wordnet.synset(i + '.n.01')
                            print(wordnet.path_similarity(tes, hit))
                        except nltk.corpus.reader.wordnet.WordNetError:
                            print("Word is not a noun.")
                        """

                    # print(row)




main()
