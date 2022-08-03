#import nltk
from nltk.corpus import state_union as state_union
from nltk.tokenize import PunktSentenceTokenizer
from sklearn.model_selection import train_test_split

# PunktSenctenceTokenizer is an unsupervised machine learning tokenizer
# It comes pre trained but you can train it on your own text too

train_text = state_union.raw("2005-GWBush.txt")
#sample_text = state_union.raw("2006-GWBush.txt")

print(train_text)
custom_sent_tokenizer = PunktSentenceTokenizer("train_Text")

