def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea','problems','help','please'],\
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],\
        ['my', 'delmation', 'is', 'so', 'cute', 'I', 'love', 'him'],\
        ['stop','posting','stupid','worthless','garbage'],\
        ['mr', 'licks', 'ate', 'my', 'steak','how','to','stop','him'],\
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    
    classVec = [0,1,0,1,0,1]
    return postingList, classVec

    
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)
    

def setOfWords2Vec(vocabList, inputSet):
    """For each input build a feature vector, with length of whole vocabulary
    set certain word to 1 if appear in input.
    ??? Does it going to make the dimensions too large
    """
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: {} is not in my Vocabulary!".format(word)
    
    return returnVec
    

def trainNBO(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)