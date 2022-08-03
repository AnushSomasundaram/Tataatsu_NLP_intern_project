import nltk

#read or understnad text......first step

#tokenizing :- form of grouping things
#word tokenizers and sentence tokenizers
#lexicon and corporas.....corpora is just a body of text ex.Medical journals, presendtial speaches
#lexicon - words and their meanings...investor-speak and regualr english speak

#investor speak 'bull' = someone who is positive about the market
# english speak 'bull' = scary animal
# 
from nltk.tokenize import sent_tokenize, word_tokenize

example_Text = "Hello there , how are you doing today? The Sky is beautiful. You should not eat cardboard. "

print(sent_tokenize(example_Text))
print(word_tokenize(example_Text))

for i in word_tokenize(example_Text):
   print(i)

#What are stop words ? a the and.....filler words...as far as data analysis is concerned they are useless

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize




