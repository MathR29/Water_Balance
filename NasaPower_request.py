import requests, json,pandas as pd
from datetime import date

def get_power(period,parameters, community, longitude, latitude, start, end):
    nasa_power_url = "https://power.larc.nasa.gov/api/temporal/{period}/point?parameters={parameters}&community={community}&longitude={longitude}&latitude={latitude}&start={start}&end={end}&format=JSON"
    url = nasa_power_url.format(period = period,
                                parameters = ",".join(parameters),
                                community = community,
                                longitude = longitude,
                                latitude = latitude,
                                start = start.replace("-", ""),
                                end = end.replace("-", ""))

    response_json = requests.get(url).json()["properties"]["parameter"]


    df = pd.DataFrame(response_json)
    df.index.name = "date"
    df = df.reset_index()
    df["date"] = pd.to_datetime(df["date"],format="%Y%m%d")
    df = df.assign(latitude = latitude,
                   longitude = longitude)
    df["DOY"] = df["date"].dt.dayofyear

    return df

