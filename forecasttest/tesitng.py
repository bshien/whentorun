from forecastiopy import *

apikey = 'e189b55a5cea6512bed42aca3e9e3aa4'

Pleasanton = [37.6604, -121.8758]

fio = ForecastIO.ForecastIO(apikey,
                            units=ForecastIO.ForecastIO.UNITS_US,
                            lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                            latitude=Pleasanton[0], longitude=Pleasanton[1])

print('Latitude', fio.latitude, 'Longitude', fio.longitude)
print('Timezone', fio.timezone, 'Offset', fio.offset)
print(fio.get_url()) # You might want to see the request url

if fio.has_currently() is True:
	currently = FIOCurrently.FIOCurrently(fio)
	print('Currently')
	#for item in currently.get().keys():
		#print(item + ' : ' + unicode(currently.get()[item]))
	# Or access attributes directly
	print(currently.temperature)
	print(currently.humidity)
else:
	print('No Currently data')