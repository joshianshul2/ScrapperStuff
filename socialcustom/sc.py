import schedule
import time
# Scrapper
import requests
import csv
import time
import pdb
import random
import re


def job():
    print("Aj")

def job2():
    print("Anji")
def job3():
    print("Sm")

def job4():
    print("Rishi")

def Load():
    schedule.every(10).seconds.do(job)
    schedule.every(10).seconds.do(job2)
    schedule.every().minutes.do(job3)
    schedule.every().hour.do(job)
    schedule.every().day.at("20:19").do(job4)
    schedule.every(1).to(2).minutes.do(job4)
    schedule.every().monday.do(job)
    schedule.every().minute.at(":17").do(job)
    schedule.every().wednesday.at("20:09").do(job3)
    schedule.every().thursday.at("11:41").do(job3)

Load()
while True:
    schedule.run_pending()
    time.sleep(1)
