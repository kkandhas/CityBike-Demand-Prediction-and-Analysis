import requests
import time
import pandas as pd
from  __builtin__ import any as b_any


def weather_Data(df_climate):
    dates = []
    maxtempF = []
    cltype = []
    
    dk = df_climate.drop_duplicates(['start_day'])

    for x in dk['start_day']:
        dates.append(x)
        api_str = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=af846e459d4f4a93b4c221033172104&q=NY&date=' + x + '&format=json'
        # print api_str
        time.sleep(0.02)
        r = requests.get(api_str)
        print "request over"

        k = r.json()

        maxtempF.append(k['data']['weather'][0]['maxtempF'])

        size = len(k['data']['weather'][0]['hourly'])
        climate = []
        for l in range(size):
            climate.append(str(k['data']['weather'][0]['hourly'][l]['weatherDesc'][0].values()).split(" "))

            # print climate
        if b_any("snow" in x for x in climate):
            cltype.append("snow")
        elif b_any("rain" in x for x in climate):
            cltype.append("rain")
        elif b_any("sunny" in x for x in climate):
            cltype.append("sunny")
        else:
            cltype.append("clear")

    new_dict = dict(zip(dates, maxtempF))
    new_dict2 = dict(zip(dates, cltype))
    df_climate['High_temp'] = df_climate['start_day'].map(new_dict)
    df_climate['Climate_type'] = df_climate['start_day'].map(new_dict2)
    return df_climate
