import requests
import pprint

from db.engine import dbEngine
from db.insert import hmi_insert, probability_long_insert
import db.model as model


params = {
    "ds": "",
    "op": "rs_list",
    "key": "",
}


def get_harpnum(url, harpnum, key):
    params["ds"] = f"hmi.mharp_720s_nrt[{harpnum}][$]"
    params["key"] = key

    response = requests.get(
        url,
        params=params,
    )

    data = response.json()

    return data


def get_sharp_value(url, harpnum, key):
    params["ds"] = f"hmi.sharp_720s_nrt[{harpnum}][$]"
    params["key"] = key

    response = requests.get(
        url,
        params=params,
    )

    data = response.json()

    return data


if __name__=="__main__":
    engine = dbEngine()
    
    url = 'http://jsoc.stanford.edu/cgi-bin/ajax/jsoc_info'

    harpnum = ""
    key = "HARPNUM"

    data = get_harpnum(url, harpnum, key)

    key = "T_REC,HARPNUM,NOAA_ARS,TOTUSJH,TOTUSJZ,TOTPOT,USFLUX,ABSNJZH,SAVNCPP"
    harpnum = data["keywords"][0]["values"][0]
    
    data = get_sharp_value(url, harpnum, key)
    
    hmi_insert(engine, data)

    probability_long_insert(engine, data)
    
    pprint.pprint(data)