import json
import os

from nltk import sent_tokenize
from gensim.utils import simple_preprocess

CORPUSF = "all_python.txt"

tokens = []

f = open(CORPUSF)
corpus = f.read()
raw_sent = sent_tokenize(corpus)
for sent in raw_sent:
    tokens.append(simple_preprocess(sent))

f.close()

OUTF = "tokenized_corpus.json"

with open(OUTF, "w") as outf:
    outf.writelines(json.dumps(tokens))