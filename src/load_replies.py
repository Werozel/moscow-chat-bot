from typing import List

import pandas

from libs.Reply import Reply
from libs.Intent import Intent
import pandas as pd


def load_replies() -> List[Reply]:
    replies = pandas.read_csv("replies.csv")
    result = []
    for _, info in replies.iterrows():
        result.append(Reply(info['reply'], Intent(info['intent'])))
    return result

