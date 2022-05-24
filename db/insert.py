from sqlalchemy.orm import Session
from core.probability import probability_long_calc
from . import model


def hmi_insert(engine, data):
    stmt = model.hmi_sharp(
        date=data['keywords'][0]['values'][0],
        harpnum=data['keywords'][1]['values'][0],
        noaa_ar=data['keywords'][2]['values'][0],
        h_ctotal=data['keywords'][3]['values'][0],    
        j_ztotal=data['keywords'][4]['values'][0],
        rho_tot=data['keywords'][5]['values'][0],
        phi=data['keywords'][6]['values'][0],
        h_cabs=data['keywords'][7]['values'][0],
        j_zsum=data['keywords'][8]['values'][0],
    )
    
    with Session(engine) as session:
        session.add(stmt)
        session.commit()


def probability_long_insert(engine, data):    
    stmt = model.probability_model_long(
        date=data["keywords"][0]["values"][0],
        harpnum=data['keywords'][1]['values'][0],
        noaa_ar=data["keywords"][2]["values"][0],
        p_l_totusjh=probability_long_calc("totusjh", float(data["keywords"][3]["values"][0])),
        p_l_totusjz=probability_long_calc("totusjz", float(data["keywords"][4]["values"][0])),
        p_l_totpot=probability_long_calc("totpot", float(data["keywords"][5]["values"][0])),
        p_l_usflux=probability_long_calc("usflux", float(data["keywords"][6]["values"][0])),
        p_l_absnjzh=probability_long_calc("absnjzh", float(data["keywords"][7]["values"][0])),
        p_l_savncpp=probability_long_calc("savncpp", float(data["keywords"][8]["values"][0])),
    )

    with Session(engine) as session:
        session.add(stmt)
        session.commit()
