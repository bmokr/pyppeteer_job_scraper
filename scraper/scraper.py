from env_manager.env_mng import EnvironmentManager
import asyncio
from pyppeteer import launch
import concurrent.futures
from .indeed import Indeed


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
        if url == "https://pl.indeed.com/":
            pager = Indeed(page, self._job + " " + self._level, self._cities)
            output = await pager.check_jobs()
            return output

        return 42
        #await browser.close()

    def  run(self, url):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(self.scrape(url))
        print(result)
        return result
        #asyncio.run(self.scrape(url))

    def search(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for url in self._pages:
                future = executor.submit(self.run(url))
                futures.append(future)
            
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                print("pentla", result)
