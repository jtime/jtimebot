import datetime
import urllib.request

from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()


#03/22 2317
# @sched.scheduled_job('interval', minutes=3)
# def time_job():
#     print('This job is run every three minutes.')
#
# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
# def scheduled_job():
#     print('this job is run every weekday at 5pm.')

#0316 p6-12
# @sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/20')
# def scheduled_job():
#     url = "https://jtimebot.herokuapp.com/"
#     conn = urllib.request.urlopen(url)
#
#     for key, value in conn.getheaders():
#         print(key, value)

@sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/2')
def scheduled_job():
    print("===============APScheduler CORN=========================")
    print("===============APScheduler CORN=========================")
    print(f"{datetime.datetime.now().ctime()}")
    print("===============APScheduler CORN=========================")
    print("===============APScheduler CORN=========================")
    
    url = "https://jtimebot.herokuapp.com/"
    conn = urllib.request.urlopen(url)

    for key, value in conn.getheaders():
        print(key, value)

sched.start()
