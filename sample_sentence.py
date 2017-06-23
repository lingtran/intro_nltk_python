import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

sentence = "What is the weather in Chicago?"
tokens = word_tokenize(sentence)

print(tokens)

stop_words = set(stopwords.words('english'))
clean_tokens = [w for w in tokens if not w in stop_words]

print(clean_tokens)

tagged = nltk.pos_tag(clean_tokens)

print(tagged)
