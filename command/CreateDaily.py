import logging
import sqlite3
import datetime

from telegram.ext import CommandHandler

from command.WordOfTheDay import WotD

logger = logging.getLogger()


class CreateDaily(CommandHandler):
    def __init__(self, db_name, job_queue):
        super(CreateDaily, self).__init__(
            "daily",
            self.create_daily_job,
            pass_args=True
        )
        self.db_name = db_name
        self.job_queue = job_queue

    def create_daily_job(self, update, context):
        logger.debug("Called create_daily_job method")
        try:
            conn = sqlite3.connect(self.db_name)

            c = conn.execute('SELECT chat_id, time_of_the_day FROM enabled_chats WHERE chat_id = ?',
                             (update.message.chat_id,))

            query_result = c.fetchone()

            if query_result is None:

                WotD.get_wotd(update, context)

                scheduled_datetime = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1),
                                                               datetime.time.fromisoformat(context.args[0]))
                conn.execute('INSERT INTO enabled_chats (chat_id, time_of_the_day) VALUES (?, ?)',
                             (update.message.chat_id, scheduled_datetime.timestamp()))

                conn.commit()

                self.job_queue.run_daily(WotD.get_wotd, scheduled_datetime.time(), name=str(update.message.chat_id))

            else:
                unix_epoch = datetime.datetime.fromtimestamp(query_result[1])

                context.bot.send_message(chat_id=update.message.chat_id,
                                         text='Ti mando già la parola alle ' + str(unix_epoch.time())[:-3])

        except ValueError:
            context.bot.send_message(chat_id=update.message.chat_id, text='L\'ora deve essere nel formato hh:mm')

    def create_daily_job_from_db(self):
        logger.debug("Called create_daily_job_from_db method")
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        for row in cursor.execute('SELECT chat_id, time_of_the_day FROM enabled_chats'):
            unix_epoch = datetime.datetime.fromtimestamp(row[1])

            self.job_queue.run_daily(WotD.get_wotd, unix_epoch.time(), name=row[0])
