# import datetime
# from apscheduler.schedulers.blocking import BlockingScheduler
# import urllib.request
#
# sched = BlockingScheduler()
#
#
# @sched.scheduled_job('cron', minute='*/2')
# def scheduled_job():
#     print('this job runs every day */2 min.')
#     print(f"{datetime.datetime.now().ctime()}")
#     print('====== APScheduler CRON ==========')
#
#     url = "https://jtimebot.heroku.com/"
#     conn =urllib.request.urlopen(url)
#
#     for key,value in conn.getheaders():
#         print(key, value)
#
# sched.start()

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()