import math
import numpy as np


ab_parameter = {
    "totusjh": [1.61, -6.34],
    "totusjz": [1.56, -22.21],
    "totpot": [1.11, -27.25],
    "usflux": [1.34, -30.95],
    "savncpp": [1.16, -16.0],
    "absnjzh": [0.98, -3.31],
}


def probability_long_calc(parameter, value):
    log_param = math.log10(value)
    factor = ab_parameter[parameter][0]*log_param + ab_parameter[parameter][1]
    r = pow(10, factor)
    p = 100*(1. - np.exp(-r))

    return p