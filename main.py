import schedule
import os
import time
import datetime


# 定时任务

def extract_in():
    cmd = "scrapy crawl in_port -o in_port_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".json"
    os.system(cmd)


def extract_out():
    cmd = "scrapy crawl out_port -o out_port_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".json"
    os.system(cmd)


schedule.every().day.at("12:00").do(extract_in(), "extract_in")
schedule.every().day.at("12:00").do(extract_out(), "extract_out")

while True:
    schedule.run_pending()
    time.sleep(10)
