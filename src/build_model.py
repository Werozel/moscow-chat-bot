import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer
import nltk


def tokenize_and_stem(text):
    tokens = nltk.word_tokenize(text)
    stemmer = nltk.stem.porter.PorterStemmer()
    return [i for i in [stemmer.stem(t) for t in tokens] if len(i) > 2]


class VectorizerProvider:
    vectorizer = CountVectorizer(stop_words=None, tokenizer=tokenize_and_stem)


def load_train_data() -> pd.DataFrame:
    return pd.read_csv("intent_train.csv")


def build_model():
    df = load_train_data()
    vectorizer = VectorizerProvider.vectorizer
    return df, vectorizer.fit_transform(df['request'])
