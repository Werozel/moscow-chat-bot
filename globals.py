import telegram.ext as tge
from config import TELEGRAM_TOKEN

updater = tge.Updater(TELEGRAM_TOKEN, use_context=True)
dispatcher: tge.Dispatcher = updater.dispatcher
