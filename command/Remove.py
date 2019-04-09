import logging
import sqlite3

from telegram.ext import CommandHandler

logger = logging.getLogger()


class Remove(CommandHandler):
    def __init__(self, db_name, job_queue):
        super(Remove, self).__init__(
            "remove",
            self.remove_schedule,
        )
        self.db_name = db_name
        self.job_queue = job_queue

    def remove_schedule(self, update, context):
        logger.debug("Called remove_schedule method")
        conn = sqlite3.connect(self.db_name)

        c = conn.execute('SELECT chat_id, time_of_the_day FROM enabled_chats WHERE chat_id = ?',
                         (update.message.chat_id,))

        query_result = c.fetchone()

        if query_result is not None:
            conn.execute('DELETE FROM enabled_chats WHERE chat_id = ?', (update.message.chat_id,))

            self.job_queue.get_jobs_by_name(str(update.message.chat_id)).schedule_removal()

            context.bot.send_message(chat_id=update.message.chat_id,
                                     text='Va bene, non ti manderò più la parola del giorno')

        else:
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text='Non ti mando la parola del giorno regolarmente')
