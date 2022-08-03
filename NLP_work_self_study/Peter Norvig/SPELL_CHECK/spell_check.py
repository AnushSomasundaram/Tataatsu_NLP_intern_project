#This is a simple spell checker written by peter norvig

#Take away points ->
#Written comments inside function
# Written loops in single lines to avoid clutter
# Worked Bottom-Up ....first incorporated the written functions and then wrote them  
#Simple training Model

import re 
from collections import Counter

def word(text) : return re.findall(r'w',text.lower())

WORDS = Counter(word(open(big.txt).read()))

def P(word, N=sum(WORDS.values())):
    #base of the model
    #probability of word
    return WORDS[word]/N

def correction(word):
    #"Most probable spelling correction for word."
    return max(candidates(word),key=P)

def candidates(word):
    #"The subset of 'word' that appear in ther dictionary of word."
    return (known([word]) or known(edits1(word)  ) or known(edits2(word)) or [word])

def known(word):

    #The subset of word that appear in the dictionary of word
    return set(w for w in word if w in WORDS)

def edits1(word):
    "All edits that are one edit away from a word"
    letters = "abcdefghijklmnopqrstuvwxyz"
    splits  = [(word[:i],  word[i:])for i in range (len(word)+1)]
    deletes = [L+R[1:] for L, R in splits if len(R)>1]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    #All edits that are to edits away from 'word'
    return(e2 for e1 in edits1(word) for e2 in edits1(e1))


