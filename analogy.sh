# Analogy task. 
srun -w adamantium -c 4 --mem 4000 -J analogy ./compute-accuracy glove.840B.300d.word2vec_clean.bin < questions-words.txt
