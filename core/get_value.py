import requests
import datetime
from bs4 import BeautifulSoup

from . import retail_data


now = datetime.datetime.now()
yesterday = now - datetime.timedelta(days=1)

hmi_url = 'http://jsoc.stanford.edu/cgi-bin/ajax/jsoc_info'
hmi_params = {
    "ds": "",
    "op": "rs_list",
    "key": "",
}

flare_event_url = 'http://helio.mssl.ucl.ac.uk/hec/hec_gui_free.php'
flare_event_params = {
    "sql": "",
}
flare_time_start = {
    "middle_term": ['2000-01-01 00:00:00', yesterday.strftime('%Y-%m-%d 00:00:00')],
    "short_term": [yesterday.strftime('%Y-%m-%d 00:00:00'), now.strftime('%Y-%m-%d 00:00:00')],
}

def get_harpnum(harpnum, key):
    hmi_params["ds"] = f"hmi.mharp_720s_nrt[{harpnum}][$]"
    hmi_params["key"] = key

    response = requests.get(
        hmi_url,
        params=hmi_params,
    )

    data = response.json()

    return data


def get_sharp_value(harpnum, key):
    hmi_params["ds"] = f"hmi.sharp_720s_nrt[{harpnum}][$]"
    hmi_params["key"] = key

    response = requests.get(
        hmi_url,
        params=hmi_params,
    )

    data = response.json()

    return data


def get_flare_event(noaa_ars, term):
    flare_event_params["sql"] = (
        "SELECT * FROM gevloc_sxr_flare "
        f"WHERE (nar={noaa_ars}) "
        "AND (xray_class LIKE 'M%' OR xray_class LIKE 'X%') "
        f"AND (time_start>='{flare_time_start[f'{term}'][0]}' "
        f"AND time_start<='{flare_time_start[f'{term}'][1]}')"
    )

    response = requests.get(
        flare_event_url,
        params=flare_event_params,
    )

    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    data = soup.body.get_text().strip()

    data = retail_data.retail_data(data)

    return data
