# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/Sibyl_System/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "4726773"
    API_HASH = "34fa7c7ece67fbadb63f7823172e46a3"
    STRING_SESSION = "1AZWarzgBu3ecdnighnLB8jtb0rIIZu2UMbrmVLhEiEeGRFcv_Hiy9DYYs6NtAII2kGOEaOdGTwwBLme9fbiAY3IRQxosfiEE84B6cDNQIdatUs0goVNF4uj7N9x3Zi6aWbu-P3GDw_nS36qGX369uvCZO0f22MGMqMovT4o2IH3a9wD9R2XChs_CM0iwaU7SCjG4iCo7vtK26aAPUCiAdp6jVLC3pbQ6JghrGayWwPj7ttlr2AOzRaznQqRH71jpBWIGtfmrQbwVoo7RrfS6rV5z7AGPQCCaw-dO_iuw6TUt1TYYdNmcMW5Rk1qng0hiWXk2DS7nFUYabKpCL1pfVkiFDyy3u3g="
    MONGO_DB_URL = "mongodb+srv://userbot:userbot@cluster0.x5kew.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    SIBYL = 1690307965
    ENFORCERS = 1732236209
    INSPECTORS = 1511373882
    Sibyl_logs = -1001216545116
    Sibyl_approved_logs = -1001216545116
    BOT_TOKEN = "1729614497:AAFj_7Psr0gV59atqmE8pPWe59xxuCzpurM"
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
