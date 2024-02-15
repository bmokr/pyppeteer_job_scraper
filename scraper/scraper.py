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
