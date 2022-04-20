import telegram.ext as tge
from config import TELEGRAM_TOKEN

updater = tge.Updater(TELEGRAM_TOKEN)
dispatcher: tge.Dispatcher = updater.dispatcher
