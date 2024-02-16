from env_manager.env_mng import EnvironmentManager
import asyncio
from pyppeteer import launch


class JobScraper:
    def __init__(self):
        self._urls = None
        self._job = None
        self._level = None
        
    @property
    def urls(self):
        pass


manager = EnvironmentManager()
manager.set_env('.env.pages')

url1 = manager.url1
url2 = manager.url2
url3 = manager.url3
job_title = manager.job + ' ' + manager.level
city_where = manager.city2