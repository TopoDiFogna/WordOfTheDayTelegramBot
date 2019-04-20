import logging

from telegram.ext import CommandHandler

logger = logging.getLogger()


class Start(CommandHandler):
    def __init__(self):
        super(Start, self).__init__(
            "start",
            self.start
        )

    @staticmethod
    def start(update, context):
        logger.debug("Called start method")
        context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
