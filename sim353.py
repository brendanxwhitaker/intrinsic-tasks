#I had to add the pyemblib thing to my path each time I login
#the instructions to do this are in the github repo for pyemblib
#I checked 3 different words and it seems each vector has exactly
#100 components so I'm just going to assume we're in $\mathbb{R}^100$.
#Beginning to implement similarity/relatedness. 
import re
import pyemblib
import math
import scipy.stats as stats
import sys
from tqdm import tqdm

emb_path = sys.argv[1]

def testFunc():
    print('testFun')

wordsim = open("wordsim353_agreed.txt")

print("Preprocessing. ")
file_name_length = len(emb_path)
last_char = emb_path[file_name_length - 1]

# Decide if it's a binary or text embedding file, and read in
# the embedding as a dict object, where the keys are the tokens
# (strings), and the values are the components of the corresponding 
# vectors (floats).
embedding = {}
if (last_char == 'n'):
    embedding = pyemblib.read(emb_path, mode=pyemblib.Mode.Binary, replace_errors=True)
elif (last_char == 't'):
    embedding = pyemblib.read(emb_path, mode=pyemblib.Mode.Text, replace_errors=True)
else:
    print("Unsupported embedding format. ")
    exit()

print("Source: ", emb_path)


result = []
humanRank = []
cosineRank = []
numMiss = 0
full_vocab = []

#'''
for line in tqdm(wordsim.read().splitlines()):
    #skips the headers
    if line[0] != '#':
        #the first column is the word type
        #the second column is the first word, followed by the second word
        #the third line is the human-rated similarity for comparison
        lineArray = re.split(r'\t+',line)
        #print(lineArray)
        wordA = lineArray[1]
        wordB = lineArray[2]
        humanRk = lineArray[3]

        # we populate the vocab
        if wordA not in full_vocab:
            full_vocab.append(wordA)
        if wordB not in full_vocab:
            full_vocab.append(wordB)    

        #lengthA = len(lineArray[1])
        #lengthB = len(lineArray[2])
        dotProd = 0
        if wordA in embedding and wordB in embedding:
            vecA = embedding[wordA]
            vecB = embedding[wordB]
        
        
            dotSum = 0
            sumSquaresA = 0
            sumSquaresB = 0
            for i in range(0,100):
                dotSum += vecA[i] *  vecB[i]
                sumSquaresA += (vecA[i])**2
                sumSquaresB += (vecB[i])**2
        
        
            magA = math.sqrt(sumSquaresA)
            magB = math.sqrt(sumSquaresB)
            dotProd = dotSum/(magA*magB)

            newRow = []
            for x in range(0,4):
                newRow.append(lineArray[x])
            newRow.append(dotProd)
            result.append(newRow)
            cosineRank.append(dotProd)
            humanRank.append(humanRk)
            
        else:
            dotProd = 0
            numMiss += 1
        #print dotProd        
for y in range(0,10):
    print(result[y])

print('the length of cosineRank is: ' + str(len(cosineRank)))
print('the length of humanRank is: ' + str(len(humanRank)))
rho = stats.spearmanr(humanRank,cosineRank)
print(rho)

print("number of misses: ",numMiss)
#'''

# we print the full vocab to a text file
with open("wordsim_vocab.txt","w") as f:
    for word in full_vocab:
        f.write(word + "\n")

#Here's some sample code for opening the word vectors from the binary file:
'''
testVec = embedding['population']
print testVec
lengthOfTestVec = len(testVec)
print lengthOfTestVec
vec2 = embedding['shower']
vec3 = embedding['architecture']
len2 = len(vec2)
len3 = len(vec3)
print len2
print len3
print vec2[0]
print vec2[1]
print vec2[2]
print vec2[99]
'''

#print 'CD' in embedding
