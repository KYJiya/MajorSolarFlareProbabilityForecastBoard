import pprint
from tqdm import tqdm

from db import insert, engine
from core import get_value


if __name__=="__main__":
    engine = engine.dbEngine()
    
    url = 'http://jsoc.stanford.edu/cgi-bin/ajax/jsoc_info'

    harpnum = ""
    key = "HARPNUM"

    harpnum = get_value.get_harpnum(harpnum, key)
    harpnum = harpnum["keywords"][0]["values"]

    key = "T_REC,HARPNUM,NOAA_ARS,TOTUSJH,TOTUSJZ,TOTPOT,USFLUX,ABSNJZH,SAVNCPP"

    for k_1 in tqdm(harpnum):
        data = get_value.get_sharp_value(k_1, key)
        
        if "keywords" in data:
            insert.hmi_insert(engine, data)
            insert.probability_long_insert(engine, data)

            noaa_ars = data["keywords"][2]["values"][0].split(",")

            short_term_data = []
            mid_term_data = []
            for k_2 in tqdm(noaa_ars, leave=False):
                short_term_data.extend(get_value.get_flare_event(k_2, 'short_term'))
                mid_term_data.extend(get_value.get_flare_event(k_2, 'middle_term'))
            
            # 중복 제거
            short_term_data = list(set(short_term_data))
            mid_term_data = list(set(mid_term_data))
            short_term_data.sort()
            mid_term_data.sort()
            insert.probability_insert(engine, data, short_term_data, mid_term_data)
        else:
            pass
