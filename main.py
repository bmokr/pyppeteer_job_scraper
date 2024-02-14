from env_manager.env_mng import EnvironmentManager


# Initialization of environmental variables
manager = EnvironmentManager()
manager.set_env('.env.pages')

url1 = manager.url1
url2 = manager.url2
url3 = manager.url3
