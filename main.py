#!/usr/bin/env python3

import logging
import sqlite3

import requests_cache
from telegram.ext import Updater
from telegram.utils.request import Request

from WotDBot import Bot

from command.CreateDaily import CreateDaily
from command.Remove import Remove
from command.Start import Start
from command.WordOfTheDay import WotD

requests_cache.install_cache(cache_name='cache', backend='sqlite', expire_after=14400)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

token = open('.token').read().strip()
request = Request(con_pool_size=8)
bot = Bot(token, request=request)
updater = Updater(bot=bot, use_context=True)

dispatcher = updater.dispatcher
job_queue = updater.job_queue
db_name = 'database.sqlite'


def initialize_db():
    connection = sqlite3.connect(db_name)
    cursor = connection.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'enabled_chats\'')

    result = cursor.fetchone()
    if result is None:
        connection.executescript('''
                            create table enabled_chats
                            (
                                chat_id  TEXT  not null
                                constraint "database.sqlite_pk" primary key,
                                time_of_the_day NUMERIC not null
                            );
                            create unique index "database.sqlite_chat_id_uindex"
                            on enabled_chats (chat_id);
                            ''')
        connection.close()


initialize_db()

start_handler = Start()
pdg_handler = WotD()
pdg_daily_handler = CreateDaily(db_name, job_queue)
pdg_remove_schedule = Remove(db_name, job_queue)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(pdg_handler)
dispatcher.add_handler(pdg_daily_handler)
dispatcher.add_handler(pdg_remove_schedule)

pdg_daily_handler.create_daily_job_from_db()

if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
    logging.debug('''
    ========================================================
                          ACTIVE JOBS
    ========================================================''')
    for job in job_queue.jobs():
        logging.debug('Name: ' + str(job.name) + ' enabled: ' + str(job.enabled) + ' will run in: ' + str(job.interval))

    logging.debug('''
    ========================================================
                         END OF ACTIVE JOBS
    ========================================================
    ''')

updater.start_polling()
