import requests
import pprint

from db.engine import dbEngine
import db.model as model


def get_hmi():
    url = 'http://jsoc.stanford.edu/cgi-bin/ajax/jsoc_info'

    params = {
        "ds": "hmi.mharp_720s_nrt[][$]",
        "op": "rs_list",
        "key": "T_REC,HARPNUM,NOAA_ARS",
    }

    response = requests.get(
        url,
        params=params,
    )

    data = response.json()

    pprint.pprint(data)


if __name__=="__main__":
    engine = dbEngine()
    conn = engine.connect()
    print(conn.scalar("select sysdate from dual"))
    
    get_hmi()