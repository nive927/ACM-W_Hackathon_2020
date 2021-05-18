# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 00:15:51 2020

@author: Lakshmi Priya
"""

import numpy as np
from sentence_transformers import SentenceTransformer
sentences = ["I ate dinner.", 
       "We had a three-course meal.", 
       "Brad came to dinner with us.",
       "He loves fish tacos.",
       "In the end, we all felt like we ate too much.",
       "We all agreed; it was a magnificent evening."]

def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

model = SentenceTransformer('bert-base-nli-mean-tokens')

sentence_embeddings = model.encode(sentences)

#print('Sample BERT embedding vector - length', len(sentence_embeddings[0]))
#print('Sample BERT embedding vector - note includes negative values', sentence_embeddings[0])

#query = "I had pizza and pasta"
query = "End ate much"

query_vec = model.encode([query])[0]

max_sim = -1
sentence = ''
for sent in sentences:
  sim = cosine(query_vec, model.encode([sent])[0])
  if sim > max_sim:
      sentence = sent
      max_sim = sim
      
print("Sentence = ", sentence, "; similarity = ", max_sim)


'''
from gingerit.gingerit import GingerIt

text = 'The smelt of fliwers bring back memories.'

parser = GingerIt()
print(parser.parse(text)['result'])
'''

