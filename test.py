from IAvailabile import IAvailable
from TwitchScrapeAvailable import TwitchScrapeAvailable

available: IAvailable = TwitchScrapeAvailable()

username = 'aaaa'
print(f"Is '{username}' available? {available.is_username_available(username)}")