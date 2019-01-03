
#srun -J rando --mem 4000 -c 4 -w feldspar python3 sim353.py ./embeddings/top_10000_emb.txt Word2Vec
#srun -J rando --mem 50000 -c 10 -w adamantium python3 sim999.py ./embeddings/gigatext1.txt Word2Vec
srun -J sim353ld --mem 4000 -c 4 -w feldspar python3 sim353.py ../embeddings/GoogleNews-vectors-negative300.bin Word2Vec
#srun -J rando --mem 50000 -c 10 -w adamantium python3 sim999.py ./embeddings/wiki-news-300d-1M-subword.txt Word2Vec     # Works correctly. 
#srun -J rando --mem 50000 -c 10 -w adamantium python3 sim999.py ./embeddings/random__source--wiki-news-300d-1M-subword__2019-01-03-1134.txt Word2Vec 
#srun -J rando --mem 50000 -c 10 -w adamantium python3 sim353.py ./embeddings/glove.840B.300d.word2vec.txt Word2Vec 
