from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather


API_KEY = 'e189b55a5cea6512bed42aca3e9e3aa4'

# Synchronous way
darksky = DarkSky(API_KEY)

latitude = 42.3601
longitude = -71.0589
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
)

print(forecast.MINUTELY)