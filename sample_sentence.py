import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

sentence = "What is the weather in Chicago?"
tokens = word_tokenize(sentence)

print(tokens)
# ['What', 'is', 'the', 'weather', 'in', 'Chicago', '?']

stop_words = set(stopwords.words('english'))
clean_tokens = [w for w in tokens if not w in stop_words]

print(clean_tokens)
# ['What', 'weather', 'Chicago', '?']

tagged = nltk.pos_tag(clean_tokens)

print(tagged)
# [('What', 'WP'), ('weather', 'NN'), ('Chicago', 'NNP'), ('?', '.')]

#ne_chunk from Numpy
print(nltk.ne_chunk(tagged))
# (S What/WP weather/NN (GPE Chicago/NNP) ?/.)
