import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import ssl
import urllib.request

ssl.match_hostname = lambda cert, hostname: True
sched = BlockingScheduler()


# @sched.scheduled_job('interval', minutes = 3)
# def timed_job():
#     print('This job is run every three minutes.')

@sched.scheduled_job('cron', minute='*/2')
def scheduled_job():
    print('this job runs every day */2 min.')
    print(f"{datetime.datetime.now().ctime()}")
    print('====== APScheduler CRON ==========')

    url = "https://jtimebot.heroku.com/"
    conn =urllib.request.urlopen(url)

    for key,value in conn.getheaders():
        print(key, value)

sched.start()
