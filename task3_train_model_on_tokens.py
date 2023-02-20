import gensim
import json

INFILE = "tokenized_corpus.json"

with open(INFILE, "r") as infile:
    tokens = json.loads(infile.readline())

model = gensim.models.Word2Vec(
    window=10,
    min_count=2
)

model.build_vocab(tokens)

model.train(tokens, total_examples=model.corpus_count, epochs=model.epochs)

print(model.wv.most_similar('legend'))