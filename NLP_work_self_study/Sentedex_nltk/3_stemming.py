# stemming is a process of normalization .... the stemming
# exact same sentences but ride and riding are different
# I was taking a ride in the car
# I was riding in the car
# porterstemmer ...... been around since 1979...algorithm to stem words

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

ps = PorterStemmer()

example_words = ["python", "python", "Pythoning", "Pythonly"]

for w in example_words:
    print(ps.stem(w))

new_text = "it is very important"

