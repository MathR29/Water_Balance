import numpy as np

def ET0_HS(df):
    df["lat_rad"] = df["latitude"] * 0.0174533
    df["dr"] = 1 + 0.033 * np.cos((2 * np.pi / 365) * df["DOY"])
    df["Sd"] = 0.409 * np.sin((2 * np.pi / 365) * df["DOY"] - 1.39)
    df["ws"] = np.acos(-np.tan(df["lat_rad"]) * np.tan(df["Sd"]))
    df["Ra"] = (24 * 60) / (np.pi) * 0.0820 * df["dr"] * (
                df["ws"] * np.sin(df["lat_rad"]) * np.sin(df["Sd"]) + np.cos(df["lat_rad"]) * np.sin(df["ws"]))
    df["ET0_HS"] = 0.0135 * 0.17 * (df["Ra"] / 2.45) * (np.sqrt(df["T2M_MAX"] - df["T2M_MIN"])) * (df["T2M"] + 17.8)
    df["p_etp"] = df["PRECTOTCORR"] - df["ET0_HS"]

    return df



