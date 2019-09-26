import logging

from telegram import Update
from telegram.ext import MessageHandler, Filters, Updater, CallbackContext

from decorators import Mode

logger = logging.getLogger(__name__)

mode = Mode(mode_name="smile_mode", default=False)


@mode.add
def add_smile_mode(upd: Updater, handlers_group: int):
    """ Set up all handler for SmileMode """
    logger.info("register smile-mode handlers")
    dp = upd.dispatcher
    dp.add_handler(MessageHandler(Filters.all, smile), handlers_group)


@mode.handler()
def smile(update: Update, context: CallbackContext):
    """ Delete all messages except stickers or GIFs """
    logger.debug(f"remove msg: {update.effective_message}")
    context.bot.delete_message(
        update.effective_chat.id,
        update.effective_message.message_id, 10
    )
