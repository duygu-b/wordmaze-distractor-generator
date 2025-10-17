import random
from collections import defaultdict
import nltk, stanza

nltk.download('gutenberg')
nltk.download('punkt')
from nltk.corpus import gutenberg

N_SENT = 400
sentences_list = []
#Extracting the first 300 sentences of auste-emma.txt file from Gutenberg - we can increase the number
for sentence in gutenberg.sents('austen-emma.txt')[:N_SENT]: #Gutenberg takes sentences separating tokens
    joined_sentence = " ".join(sentence) #combining the separated tokens of the sentences to make proper sentences
    sentences_list.append(joined_sentence) #adding these proper sentences into the list defined above

corpus_text = "\n".join(sentences_list) #merging all sentence, each one is on a new line

#Stanza model
stanza.download("en")
my_processing_model = stanza.Pipeline("en", processors="tokenize,pos")

#Generating pools
pos_pool = defaultdict(set)   #UPOS: word
rel_pool = set()              #PronType=Rel: word

doc = my_processing_model(corpus_text)
for sent in doc.sentences:
    for w in sent.words:
        if w.text.isalpha():
            word = w.text.lower()
            pos_pool[w.upos].add(word)
            if w.feats and "PronType=Rel" in w.feats:
                rel_pool.add(word)

#Target sentence
sentence = "Put the rabbit that is on the towel onto the tray"
my_tokens = my_processing_model(sentence)
my_tokens_list = []
for s in my_tokens.sentences:
    for w in s.words:
        my_tokens_list.append(w)

#Printing the POS of target sentence
print("Target Tokens (POS)")
for w in my_tokens_list:
    print(w.text, ":", w.upos, ", Features:", w.feats)

#Samples from pools
print("POS (samples)")
for pos, words in pos_pool.items():
    sample = random.sample(list(words), min(5, len(words)))#Takes the smaller value between 10 and the length of words
    print( pos, ":", sample)

if rel_pool:
    print("Relative Pronoun (samples):", random.sample(list(rel_pool), min(5, len(rel_pool))))
else:
    print("Relative pronoun not found.")

#Generating distractors
distractor = ["xxx"]
for i in range(1, len(my_tokens_list)):
    prev = my_tokens_list[i - 1]
    if prev.feats and "PronType=Rel" in prev.feats:
        pool = list(rel_pool - {prev.text.lower()})
    else:
        pool = list(pos_pool.get(prev.upos, set()) - {prev.text.lower()})
    if pool:
        distractor.append(random.choice(pool))
    else:
        distractor.append("???")

print("Results")
print("Target:    ", sentence)
print("Distractor:", " ".join(distractor))