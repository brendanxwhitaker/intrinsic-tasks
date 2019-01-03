#I had to add the pyemblib thing to my path each time I login
#the instructions to do this are in the github repo for pyemblib
#I checked 3 different words and it seems each vector has exactly
#100 components so I'm just going to assume we're in $\mathbb{R}^100$.
#Beginning to implement similarity/relatedness. 
import re
import os
import sys
import math
import pyemblib
import scipy.stats as stats
from tqdm import tqdm

emb_path = sys.argv[1]

def testFunc():
    print('testFunc')


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

parent = os.path.abspath(emb_path + "/../")
source_name = os.path.splitext(os.path.basename(emb_path))[0]
dest_path = os.path.join(parent, source_name + "_clean.bin")
pyemblib.write(embedding, dest_path, mode=pyemblib.Mode.Binary)
