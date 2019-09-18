import string
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')


#-----------------------------READ LIWC---------------------------------------------------#
#method for read the liwc after create the liwc.csv file
def readingLiwc():
    base = open('liwc.csv','r',encoding='utf-8',errors='ignore').read().split('\n')
    dataLiwc = []

    for lineBase in base:
        wordsBase = lineBase.split(',')
        if (wordsBase != []):
            dataLiwc.append(wordsBase)

    return dataLiwc
#--------------------------------------------------------------------------------#

def search (lista, valor):
    return [lista.index(x) for x in lista if valor in x]

#-----------------------------FEATURES LIWC---------------------------------------------------#
def liwcFeatures(dataSet):

    #reading liwc
    wn = open('LIWC2007_Portugues_win.dic.txt','r',encoding='ansi',errors='ignore').read().split('\n')
    wordSetLiwc = []
    for line in wn:
        words = line.split('\t')
        if (words != []):
            wordSetLiwc.append(words)


    #indexes of liwc
    indices = open('indices.txt','r',encoding='utf-8',errors='ignore').read().split('\n')



    #dataset tokenization
    wordsDataSet = []

    for vector in dataSet:
        wordsLine = []
        for word in word_tokenize(vector[1]): #o texto tá na 2º coluna do csv, por isso pego vector[1]
            if word not in string.punctuation + "\..." and word != '``' and word != '"':
                wordsLine.append(word)
        wordsDataSet.append(wordsLine)


    #initializing liwc with zero
    liwc = []

    for j in range(len(dataSet)):
        liwc.append([0]*len(indices))


    #performing couting
    print("writing liwc ")

    for k in range(len(wordsDataSet)):
        for word in wordsDataSet[k]:
            position = search(wordSetLiwc, word)
            if position != []:
                tam = len(wordSetLiwc[position[0]])
                for i in range(tam):
                    if wordSetLiwc[position[0]][i] in indices:
                        positionIndices = search(indices, wordSetLiwc[position[0]][i])
                        liwc[k][positionIndices[0]] = liwc[k][positionIndices[0]] + 1



    #saving the liwc file
    output = open('liwc2.csv','w')

    for i in range(len(liwc)):
        for j in range(len(liwc[i])):
            output.write(str(liwc[i][j]))
            if j != (len(liwc[i]) - 1):
                output.write(',')
        output.write('\n')

#--------------------------------------------------------------------------------#



#reading dataset
base = open('base-final-menor.csv','r',encoding='utf-8',errors='ignore').read().split('\n')
dataSet = []
for lineBase in base:
    wordsBase = lineBase.split(';')
    if (wordsBase != []):
        dataSet.append(wordsBase)

liwcFeatures(dataSet)