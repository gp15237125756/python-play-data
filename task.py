import time
import datetime
import psycopg2
import random

from apscheduler.schedulers.blocking import BlockingScheduler


def my_job():
    print("start the task: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    number = ""
    for x in range(6):
        number = number + str(random.randint(0, 9))

    conn = psycopg2.connect(database="bozhon", user="bozhon", password="Aa123789", host="139.196.59.97", port="5432")
    print
    "Opened database successfully"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur = conn.cursor()
    cur.execute("SELECT ID,organization_id,key,created_at,updated_at  from t_pat_key order by id desc limit 1")
    result = cur.fetchone()
    if result is None:
        cur.execute(
            "INSERT INTO t_pat_key (ID,organization_id,key,created_at,updated_at) VALUES (1, 'b0651cd5-4593-4fd8-98f2-073027218f3d', '" + str(
                number) + "', '" + now + "', '" + now + "')")
    else:
        id = result[0] + 1
        cur.execute("INSERT INTO t_pat_key (ID,organization_id,key,created_at,updated_at) VALUES (" + str(
            id) + ", 'b0651cd5-4593-4fd8-98f2-073027218f3d','" + str(number) + "', '" + now + "', '" + now + "')")
    conn.commit()
    print
    "Records created successfully"
    conn.close()


sched = BlockingScheduler()
sched.add_job(my_job, 'cron', hour='0', minute='0', second='0')
print("task running: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
sched.start()
