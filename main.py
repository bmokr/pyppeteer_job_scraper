from env_manager.env_mng import EnvironmentManager
from scraper.scraper import JobScraper


# Initialization of environmental variables
manager = EnvironmentManager()
manager.set_env('.env.pages')

# Run
if __name__ == '__main__':
    scraper = JobScraper()
    scraper.search()
