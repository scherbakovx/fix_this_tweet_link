from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from utils import replace_twitter_link
from texts import START_TEXT, HELP_TEXT

try:
    from bot_token import BOT_TOKEN
except ImportError:
    print("You need to create a bot_token.py file with BOT_TOKEN variable.")
    exit(1)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_text(START_TEXT % user.first_name)


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(HELP_TEXT)


def twit_fixer(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""

    updated_text = replace_twitter_link(update.message.text)
    if updated_text:
        update.message.reply_text(updated_text)


def main() -> None:
    """Start the bot."""
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, twit_fixer))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
