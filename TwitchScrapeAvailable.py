from IAvailabile import IAvailable

import requests
import time

class TwitchScrapeAvailable(IAvailable):

    def is_username_available(self, name: str) -> bool:
        url = f"https://www.twitch.tv/{name}"
    
        # Send a GET request with the username
        try:
            response = requests.get(url).text
            time.sleep(2)  # avoid rate limits
            return ("Sorry, unless you've got a time machine, that content is unavailable!"
                    in response or f"twitch.tv/{name.lower()}" not in response.lower())
        except Exception as e:
            print(f"Error: {e}")
            return False