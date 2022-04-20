from libs.Intent import Intent
from src.load_replies import load_replies
from src.build_model import build_model, VectorizerProvider
from sklearn.metrics.pairwise import cosine_similarity
import random


def infer_intent(request: str) -> Intent:
    df, model = build_model()
    vectorizer = VectorizerProvider.vectorizer
    request_vec = vectorizer.transform([request])
    results = cosine_similarity(model, request_vec).reshape((-1,))
    i = results.argsort()[-10:][::-1][0]
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
    return random.choice(fitting_replies).reply_text
