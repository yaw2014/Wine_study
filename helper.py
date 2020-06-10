# From a file name, approximate the probability of a word
# being generated from the same distribution as the file.
# Assume that each word is produced independently, regardless
# of order.
def makeWordProbMap(fileName):
    wordMap, nWords = makeWordCountMap(fileName)
    wordProbMap = {}
    for word in wordMap:
        count = wordMap[word]
        p = float(count) / nWords
        wordProbMap[word] = p
    print("{}: \t{}, ...".format(fileName, ", ".join(list(wordProbMap.keys())[:5])))
    return wordProbMap

# From a file name, count the number of times each word exists
# in that file. Return the result as a map (aka a dictionary)
def makeWordCountMap(fileName):
    wordMap = {}
    nWords = 0
    with open(fileName) as f:
        for line in f:
            words = line.split(' ')
            for word in words:
                word = standardize(word)
                if len(word) == 0: continue
                addWordToCountMap(wordMap, word)
                nWords+= 1
    return wordMap, nWords

# Add a word to a count map. Makes sure not to crash if the
# word has not been seen before.
def addWordToCountMap(wordMap, word):
    if not word in wordMap:
        wordMap[word] = 0
    wordMap[word] += 1

# Standardizes a word. For now, we are just going to make it
# lower case.
def standardize(word):
    return word.lower().strip(" .,-;\n:'`;?")