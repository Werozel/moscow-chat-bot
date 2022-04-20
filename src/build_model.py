import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
import nltk


def tokenize_and_stem(text):
    tokens = nltk.word_tokenize(text)
    stemmer = nltk.stem.porter.PorterStemmer()
    return ' '.join([i for i in [stemmer.stem(t) for t in tokens] if len(i) > 2])


class VectorizerProvider:
    vectorizer = TfidfVectorizer(stop_words="english")


def load_train_data() -> pd.DataFrame:
    df = pd.read_csv("intent_train.csv")
    df['request_tokenized'] = pd.Series(df['request']).map(tokenize_and_stem)
    return df


def build_model():
    df = load_train_data()
    vectorizer = VectorizerProvider.vectorizer
    return df, vectorizer.fit_transform(df['request_tokenized'])
