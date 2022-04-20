import telegram
import telegram.ext as tge
from config import TELEGRAM_TOKEN

tg = telegram.Bot(token=TELEGRAM_TOKEN)
updater = tge.Updater(TELEGRAM_TOKEN)
dispatcher: tge.Dispatcher = updater.dispatcher
