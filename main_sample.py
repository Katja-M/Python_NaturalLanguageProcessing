import nltk
nltk.download()
#This loads various text and we can refer to them by their name. These are objects of the type 'Text'
from nltk.book import *
#Text 1: Moby Dick by Herman Melville 1851
#Text 2:Sense and Sensibility by Jane Austen 1811
#Text 3: The Book of Genesis
#Text 4: Inaugural Address Corpus
#Text 5: Chat Corpus
#Text 6: Monty Python and the Holy Grail
#Text 7: Wall Street Journal
#Text 8: Personals Corpus
#Text 9: The Man Who Was Thursday by G. K. Chesterton 1908
import matplotlib
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem.lancaster import LancasterStemmer

#Concordance method will print all the occurence of a word along with some context
#Texts to explore: Moby Dick; Sense and Sensibility
#We look for the word monstruous
print(text1.concordance('monstrous'))
print(text2.concordance('monstrous'))

#Will show the differences in the use of 'monstrous'

#Let's what other words are used in the same context as 'monstrous'
print(text2.similar('monstrous'))
#This analyses will show that Jane Austen uses monstrous to represent positive emotions and to amplify those emotions

#Let's see where 'very' and 'monstrous' are used interchangeably
print(text2.common_contexts(['monstrous','very']))

#Let's see how the usage of word by Presidents changed over the years.
text4.dispersion_plot(['citizens', 'democracy','freedom', 'duties', 'America'])
#Plot will show that the word citizens has been used steadily while 'freedom' and 'America' are emphasized by more recent presidents

#Extracting features from a text
# Step 1: Split a piece of text into tokens (= constituent sentences or words)
# We imported two methods, word_tokenize and sent_tokenize

exampletext = 'Mary had a little lamb, Her fleece was white as snow.'
#Sent_tokenize returns a list. Each entry represents one sentence
sents = sent_tokenize(exampletext)
print(sents)
#word_tokenize will break any large piece of text into words.
words = [word_tokenize(sent) for sent in sents]
print(words)

#Step 2: Filter out stopwords
#Creates a set of all the stop words including the punctuation. We used a set because we do not care about the order of the stopwords
customStopWords = set(stopwords.words('english') + list(punctuation))

wordsWOStopwords = [word for word in word_tokenize(exampletext) if word not in customStopWords]
print(wordsWOStopwords)

#Stemming a word
exampletext2 = 'Mary closed on closing night when she was in the mood to close.'
#Close appears in different morphological forms here, stemming will reduce all form of the word 'close' to its root
#NLTK has multiple stemmers based on different rules/algorithms. Stemming is also known as lemmatization
#The LancasterStemmer is one particular stemmer
st = LancasterStemmer()
stemmedWords = [st.stem(word) for word in word_tokenize(exampletext2)]

#NLTK has the functionality to automatically tag words as nouns, verbs etc.
print(nltk.pos_tag(word_tokenize(exampletext2)))
