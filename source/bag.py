from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

with open("simple.txt", "r") as file:
    documents = file.read().splitlines()

    count_vectorizer = CountVectorizer()

    bag_of_words = count_vectorizer.fit_transform(documents)

    feature_names = count_vectorizer.get_feature_names_out()
    pd.DataFrame(bag_of_words.toarray(), columns = feature_names)
    df = pd.DataFrame(bag_of_words.toarray(), columns=feature_names)
    print(df)

    tfidf_vectorizer = TfidfVectorizer()
    values = tfidf_vectorizer.fit_transform(documents)

    feature_names = tfidf_vectorizer.get_feature_names_out()
    df = pd.DataFrame(values.toarray(), columns=feature_names)
    print(df)
