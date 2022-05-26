import math
import numpy as np
import datetime

from core.retail_data import retail_match_start_time


ab_parameter = {
    "totusjh": [1.61, -6.34],
    "totusjz": [1.56, -22.21],
    "totpot": [1.11, -27.25],
    "usflux": [1.34, -30.95],
    "savncpp": [1.16, -16.0],
    "absnjzh": [0.98, -3.31],
}


def probability_long_calc(parameter, value):
    r_l = r_l_calc(parameter, value)
    p = 100*(1. - np.exp(-r_l))

    return p


def probability_calc(parameter, value, short_term_data, mid_term_data):
    p = 100*(0.6*r_l_calc(parameter, value) + 0.2*r_s_calc(short_term_data) + 0.2*r_m_calc(mid_term_data))
    
    return p


def r_l_calc(parameter, value):
    log_param = math.log10(value)
    factor = ab_parameter[parameter][0]*log_param + ab_parameter[parameter][1]
    r_l = pow(10, factor)

    return r_l


def r_s_calc(short_term_data):
    class_num = float(len(short_term_data))
    r_s = class_num/1

    return r_s


def r_m_calc(mid_term_data):
    now = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    yesterday = now - datetime.timedelta(days=1)

    class_num = float(len(mid_term_data))
    if class_num == 0:
        r_m = 0
    else:
        start_time = retail_match_start_time(mid_term_data[0]).replace(hour=0, minute=0, second=0, microsecond=0)
        calc_day = float((yesterday - start_time).days)
        r_m = class_num/calc_day

    return r_m


    