from NasaPower_request import get_power
from ET0_HS_calculation import ET0_HS
import numpy as np

def water_balance (cad,lat,long,start_date,end_date):
    df = get_power(
        period = "daily",
        parameters = ["T2M","T2M_MAX","T2M_MIN","PRECTOTCORR"],
        community= "AG",
        latitude= lat,
        longitude= long,
        start = start_date,
        end = end_date
    )

    df = ET0_HS(df)
    df["cad"] = cad

    for row in df.iterrows():


    return df


def calculate_preciptation


water_balance(100,0,0,'2020-01-01','2020-12-31')