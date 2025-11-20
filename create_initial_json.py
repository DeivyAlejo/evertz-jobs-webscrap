import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
import os

from main import scrape_jobs, save_jobs

if __name__ == "__main__":
    try:
        jobs = scrape_jobs(),
        save_jobs(jobs[0])
    except Exception as e:
        print(e)