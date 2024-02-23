class Justjoinit:
    def __init__(self, page, title, where):
        self._page = page
        self._title = title
        self._where = where

    # async def check_jobs(self):
    #     await self._page.waitForSelector('#text-input-what')
    #     await self._page.waitForSelector('#text-input-where')


    #     await self._page.type('#text-input-what', self._title) # manager.job + " " + manager.level)
    #     await self._page.type('#text-input-where', self._where) # manager.city1)


    #     await self._page.click('button[type="submit"]')


    #     await self._page.waitForNavigation()


    #     job_listings = await self._page.querySelectorAll('.resultContent')
    #     temporary = []
    #     for job in job_listings:
    #         # Extract the job title
    #         title_element = await job.querySelector('h2.jobTitle span[title]')
    #         title = await self._page.evaluate('(element) => element.textContent', title_element)

    #         # Extract the href attribute
    #         link_element = await job.querySelector('h2.jobTitle a')
    #         href = await self._page.evaluate('(element) => element.getAttribute("href")', link_element)
    #         # url = manager.url1+href

    #         # Extract the company name
    #         company_element = await job.querySelector('div.company_location [data-testid="company-name"]')
    #         company = await self._page.evaluate('(element) => element.textContent', company_element)


    #         # Extract the location
    #         location_element = await job.querySelector('div.company_location [data-testid="text-location"]')
    #         location = await self._page.evaluate('(element) => element.textContent', location_element)


    #         temporary.append({'title': title, 'company': company, 'location': location, 'link': href})

    #     return temporary
