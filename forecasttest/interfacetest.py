import tkinter as tk
import geocoder
from forecastiopy import *
apikey = 'e189b55a5cea6512bed42aca3e9e3aa4'
tempdata = []
dayindex = []


def geocode():
    place = e1.get() + ',' + e2.get()
    geoloc = geocoder.arcgis(place).latlng
    print(geoloc)
    fio = ForecastIO.ForecastIO(apikey,
                                units=ForecastIO.ForecastIO.UNITS_US,
                                lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                                latitude=geoloc[0], longitude=geoloc[1])

    print('Latitude', fio.latitude, 'Longitude', fio.longitude)
    print('Timezone', fio.timezone, 'Offset', fio.offset)
    print(fio.get_url())  # You might want to see the request url

    """if fio.has_currently() is True:
        currently = FIOCurrently.FIOCurrently(fio)
        print('Currently')
        # for item in currently.get().keys():
        # print(item + ' : ' + unicode(currently.get()[item]))
        # Or access attributes directly
        print(currently.temperature)
        print(currently.humidity)
    else:
        print('No Currently data')
        """
    if fio.has_hourly() is True:
        hourly = FIOHourly.FIOHourly(fio)
        print('Hourly')
        print('Summary:', hourly.summary)
        print('Icon:', hourly.icon)

        # for hour in range(0, hourly.hours()):
        #     print('Hour', hour + 1)
        #
        #     for item in hourly.get_hour(hour).keys():
        #         print(item + ' : ' + str(hourly.get_hour(hour)[item]))
        #      #Or access attributes directly for a given minute.
        #      #hourly.hour_5_time would also work
        # print(hourly.hour_49_temperature)

        for hour in range(0, hourly.hours()):

            print('Hour', hour + 1)
            print('Temperature:' + str(hourly.get_hour(hour)['temperature']))
            tempdata.append(str(hourly.get_hour(hour)['temperature']))
             #Or access attributes directly for a given minute.
             #hourly.hour_5_time would also work

        print(hourly.hour_49_time)
        for x in tempdata:
            print(x)
        indexcalc()



    else:
        print('No Hourly data')

def indexcalc():
    for x in tempdata:
        if x <= e3.get():
            dayindex.append(tempdata.index(x))
    for x in dayindex:
        print(x)






master = tk.Tk()
tk.Label(master, text="City").grid(row=0)
tk.Label(master, text="State").grid(row=1)
tk.Label(master, text="I don't want to run in higher than __ degrees").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)


tk.Button(master,
          text='Show Coordinates', command=geocode).grid(row=3,
                                                       column=0,
                                                       sticky=tk.W,
                                                       pady=4)







master.mainloop()