import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('omw-1.4')

def compare_stemmer_and_lemmatizer(stemmer, lemmatizer, word, pos):
    """
    Print the results of stemming and lemmatization using the passed stemmer, lemmatizer, word and pos (part of speech)
    """
    print(f"Word: '{word}' (POS: {pos})")
    print("Stemmer:", stemmer.stem(word))
    print("Lemmatizer:", lemmatizer.lemmatize(word, pos))
    print()

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Сравнение стемминга и лемматизации
compare_stemmer_and_lemmatizer(stemmer, lemmatizer, word="seen", pos=wordnet.VERB)
compare_stemmer_and_lemmatizer(stemmer, lemmatizer, word="drove", pos=wordnet.VERB)