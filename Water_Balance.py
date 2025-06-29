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

    for i,row in df.iterrows():

        if i==0:
            if row["p_etp"] < 0:
                df.loc[i,"nac"] = df.loc[i,"p_etp"]
                df.loc[i,"arm"] = cad * np.exp((df.loc[i,"nac"]/cad))
            else:
                df.loc[i, "arm"] = cad + df.loc[i,"p_etp"]
                df.loc[i, "nac"] = cad * np.log(df.loc[i,"arm"]/cad)

        else:
            if row["p_etp"] < 0:
                df.loc[i,"nac"] = df.loc[i-1,"nac"] + df.loc[i,"p_etp"]
                df.loc[i,"arm"] = cad * np.exp((df.loc[i,"nac"]/cad))

            else:
                df.loc[i, "arm"] =  df.loc[i-1, "arm"] + df.loc[i,"p_etp"]
                df.loc[i, "nac"] = cad * np.log(df.loc[i,"arm"]/cad)

        if df.loc[i, "nac"] >= 0:
            df.loc[i, "nac"] = 0

        if df.loc[i, "arm"] >= cad:
            df.loc[i, "arm"] = cad

    return df
