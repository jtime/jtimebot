from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request

sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes = 3)
# def timed_job():
#     print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/20')
def scheduled_job():
    url = "https://jtimebot.heroku.com/"
    conn =urllib.request.urlopen(url)

    for key,value in conn.getheaders():
        print(key,value)

sched.start()
