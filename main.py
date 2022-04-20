from globals import tg, updater, dispatcher
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, Filters


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hi, I'm bot that can help you find things to do in Moscow!")


def help_handler(update: Update, _: CallbackContext) -> None:
    update.message.reply_markdown_v2("My topics are:\n • _Attractions_\n • _Parks_\n • _Restaurants_\n • _Bars_")


def message_handler(update: Update, _: CallbackContext) -> None:
    pass


def main():
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_handler))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, ))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
