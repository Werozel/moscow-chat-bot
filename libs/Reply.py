from Intent import Intent
from dataclasses import dataclass


@dataclass
class Reply:
    reply_text: str
    intent: Intent
