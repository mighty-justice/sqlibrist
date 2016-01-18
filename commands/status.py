# -*- coding: utf8 -*-
import os
from sys import stdout

from helpers import get_connection



def status(config):
    """
    1. get applied migrations
    2. get all migrations
    3. check unapplied migrations

    :param config:
    :return:
    """

    connection = get_connection(config)

    with connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            select migration from sqitchpy.migrations
            order by datetime''')
            applied_migrations = cursor.fetchall()

    applied_migrations = {m[0] for m in applied_migrations}
    all_migrations = sorted(os.listdir('migrations/'))
    for i, migration in enumerate(all_migrations):
        if migration in applied_migrations:
            stdout.write(u'Migration %s - applied\n' % migration)
        else:
            stdout.write(u'Migration %s - NOT applied\n' % migration)