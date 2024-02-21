from env_manager.env_mng import EnvironmentManager
import asyncio
from pyppeteer import launch
import threading



class JobScraper:
    def __init__(self):
        manager = EnvironmentManager()
        manager.set_env('.env.pages')
        self._pages = manager.pages
        self._job = manager.job
        self._level = manager.level
        self._cities = manager.cities

    async def scrape(self, url):
        browser = await launch(autoClose=False, executablePath="BIN/thorium.exe", headless=False)
        page = await browser.newPage()
        await page.goto(url, {'timeout': 60000})



        #await browser.close()

    def  run(self, url):
        asyncio.run(self.scrape(url))

    def search(self):
        for url in self._pages:
            # self.run(page)
            t = threading.Thread(target=self.run, args=(url,))
            t.start()
            t.join()
