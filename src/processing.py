from libs.Intent import Intent
from src.load_replies import load_replies
import random


def infer_intent(request: str) -> Intent:
    pass


def reply_to_intent(intent: Intent) -> str:
    replies = load_replies()
    fitting_replies = list(
        filter(
            lambda x: x.intent == intent,
            replies
        )
    )
    return random.choice(fitting_replies).reply_text
