from sqlalchemy.orm import Session
from core import probability as pb
from . import model


def hmi_insert(engine, data):
    stmt = model.hmi_sharp(
        date=data['keywords'][0]['values'][0],
        harpnum=data['keywords'][1]['values'][0],
        noaa_ars=data['keywords'][2]['values'][0],
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
        noaa_ars=data["keywords"][2]["values"][0],
        p_l_totusjh=pb.probability_long_calc("totusjh", float(data["keywords"][3]["values"][0])),
        p_l_totusjz=pb.probability_long_calc("totusjz", float(data["keywords"][4]["values"][0])),
        p_l_totpot=pb.probability_long_calc("totpot", float(data["keywords"][5]["values"][0])),
        p_l_usflux=pb.probability_long_calc("usflux", float(data["keywords"][6]["values"][0])),
        p_l_absnjzh=pb.probability_long_calc("absnjzh", float(data["keywords"][7]["values"][0])),
        p_l_savncpp=pb.probability_long_calc("savncpp", float(data["keywords"][8]["values"][0])),
    )

    with Session(engine) as session:
        session.add(stmt)
        session.commit()


def probability_insert(engine, data, short_term_data, mid_term_data):
    stmt = model.probability_model(
        date=data["keywords"][0]["values"][0],
        harpnum=data['keywords'][1]['values'][0],
        noaa_ars=data["keywords"][2]["values"][0],
        p_totusjh=pb.probability_calc("totusjh", float(data["keywords"][3]["values"][0]), short_term_data, mid_term_data),
        p_totusjz=pb.probability_calc("totusjz", float(data["keywords"][4]["values"][0]), short_term_data, mid_term_data),
        p_totpot=pb.probability_calc("totpot", float(data["keywords"][5]["values"][0]), short_term_data, mid_term_data),
        p_usflux=pb.probability_calc("usflux", float(data["keywords"][6]["values"][0]), short_term_data, mid_term_data),
        p_absnjzh=pb.probability_calc("absnjzh", float(data["keywords"][7]["values"][0]), short_term_data, mid_term_data),
        p_savncpp=pb.probability_calc("savncpp", float(data["keywords"][8]["values"][0]), short_term_data, mid_term_data),
        r_m=pb.r_m_calc(mid_term_data),
        r_s=pb.r_s_calc(short_term_data),
    )

    with Session(engine) as session:
        session.add(stmt)
        session.commit()    