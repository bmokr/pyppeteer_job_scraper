from env_manager.env_mng import EnvironmentManager
import asyncio
from pyppeteer import launch
from scraper.scraper import JobScraper


# Initialization of environmental variables
manager = EnvironmentManager()
manager.set_env('.env.pages')

# Run the coroutine
if __name__ == '__main__':
    scraper = JobScraper()
    scraper.search()


# async def scrape_indeed():
#     browser = await launch(autoClose=False, executablePath="BIN/thorium.exe", headless=False)
#     page = await browser.newPage()


#     await page.goto(manager.url1, {'timeout': 60000})


#     await page.waitForSelector('#text-input-what')
#     await page.waitForSelector('#text-input-where')


#     await page.type('#text-input-what', manager.job + " " + manager.level)
#     await page.type('#text-input-where', manager.city1)


#     await page.click('button[type="submit"]')


#     await page.waitForNavigation()


#     job_listings = await page.querySelectorAll('.resultContent')
#     for job in job_listings:
#         # Extract the job title
#         title_element = await job.querySelector('h2.jobTitle span[title]')
#         title = await page.evaluate('(element) => element.textContent', title_element)

#         # Extract the href attribute
#         link_element = await job.querySelector('h2.jobTitle a')
#         href = await page.evaluate('(element) => element.getAttribute("href")', link_element)
#         url = manager.url1+href

#         # Extract the company name
#         company_element = await job.querySelector('div.company_location [data-testid="company-name"]')
#         company = await page.evaluate('(element) => element.textContent', company_element)


#         # Extract the location
#         location_element = await job.querySelector('div.company_location [data-testid="text-location"]')
#         location = await page.evaluate('(element) => element.textContent', location_element)


#         print({'title': title, 'company': company, 'location': location, 'link': url})




#     await browser.close()


# # Run the coroutine
# if __name__ == '__main__':
#     asyncio.run(scrape_indeed())