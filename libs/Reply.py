from libs.Intent import Intent
from dataclasses import dataclass


@dataclass
class Reply:
    reply_text: str
    intent: Intent

    def __repr__(self):
        return f"{self.intent}: {self.reply_text}"
