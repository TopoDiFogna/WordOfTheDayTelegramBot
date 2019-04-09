import logging

from telegram.ext import CommandHandler

from wotd_sources import unaparolaalgiorno

logger = logging.getLogger()


class WotD(CommandHandler):
    def __init__(self):
        super(WotD, self).__init__(
            "pdg",
            self.get_wotd
        )

    @staticmethod
    def get_wotd(update, context):
        logger.debug("Called get_wotd method")

        unaparolaalgiorno_word, unaparolaalgiorno_desc = unaparolaalgiorno.get_unaparolaalgiorno_wotd()

        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=unaparolaalgiorno_word + ': ' + unaparolaalgiorno_desc)
