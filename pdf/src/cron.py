import requests
from django_cron import CronJobBase, Schedule


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # every 2 hours
    # RUN_AT_TIMES = ['19:00']

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    # schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'src.MyCronJob'  # a unique code

    def do(self):
        resp = requests.get('http://127.0.0.1:8000/src/september/')
        print(resp)

