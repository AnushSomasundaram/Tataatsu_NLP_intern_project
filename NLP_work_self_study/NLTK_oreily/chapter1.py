from nltk import *
from nltk.book import *
text1.concordance("monstrous")
text1.similar("monstrous")
text2.similar("monstrous")
text2.common_contexts(["monstrous", "very"])