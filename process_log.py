'''Process logger'''
from os.path import exists
from time import sleep
from datetime import datetime
from sqlite3 import connect

from psutil import process_iter


def get_all_stats():
    '''Stats snapshot'''
    values = {}

    for pro in process_iter():
        if "DockerTest/main.py" in pro.cmdline()[-1]:
            cpu_percent = pro.cpu_percent()
            memory_info = pro.memory_info_ex()

            values[pro.pid] = {'name': pro.name(),
                               'cmd': ' '.join(pro.cmdline()),
                               'cpu': cpu_percent,
                               'rss': memory_info.rss / 1024 ** 2,
                               'vms': memory_info.vms / 1024 ** 2}

    return values


def main():
    '''Main function'''
    # Initial call (the psutil functions need to be called once before averages
    # work)
    get_all_stats()

    new = not exists('process-log.db')

    conn = connect('process-log.db')
    cur = conn.cursor()

    if new:
        cur.execute('CREATE TABLE history (date datetime, pid int, name text,'
                    ' cmd text, cpu real, rss real, vms real)')

    try:
        while True:
            sleep(5)
            now = datetime.now().isoformat()
            values = get_all_stats()

            values_to_insert = []

            for pid in values:
                dic = values[pid]
                values_to_insert.append((now, pid, dic['name'], dic['cmd'],
                                         dic['cpu'], dic['rss'], dic['vms']))

            cur.executemany('INSERT INTO history VALUES(?,?,?,?,?,?,?)',
                            values_to_insert)

            conn.commit()
    except KeyboardInterrupt:
        pass
    finally:
        conn.commit()
        conn.close()

main()
