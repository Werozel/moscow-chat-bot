from libs.Intent import Intent
from src.load_replies import load_replies
from src.build_model import build_model, VectorizerProvider
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfTransformer
import random


def infer_intent(request: str) -> Intent:
    df, doc_term_matrix = build_model()
    cv = VectorizerProvider.vectorizer
    idfs = TfidfTransformer(use_idf=True, smooth_idf=True, sublinear_tf=True)
    tf_idfs = idfs.fit_transform(doc_term_matrix)
    request_vec = cv.transform([request])
    results = cosine_similarity(tf_idfs, request_vec).reshape((-1,))
    i = results.argsort()[:-11:-1][0]
    intent_int = df.iloc[i, 0]
    print(f"{request=}\nbest match={df.iloc[i, 1]}")
    return Intent(intent_int)


def reply_to_intent(intent: Intent) -> str:
    replies = load_replies()
    fitting_replies = list(
        filter(
            lambda x: x.intent == intent,
            replies
        )
    )
    random.shuffle(fitting_replies)
    return random.choice(fitting_replies).reply_text
