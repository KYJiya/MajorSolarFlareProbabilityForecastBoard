from sqlalchemy.orm import Session
from . import model


def hmi_insert(engine, data):
    stmt = model.hmi_sharp(
        date=data['keywords'][0]['values'][0],
        noaa_ar=data['keywords'][1]['values'][0],
        h_ctotal=data['keywords'][2]['values'][0],    
        j_ztotal=data['keywords'][3]['values'][0],
        rho_tot=data['keywords'][4]['values'][0],
        phi=data['keywords'][5]['values'][0],
        h_cabs=data['keywords'][6]['values'][0],
        j_zsum=data['keywords'][7]['values'][0],
    )
    
    with Session(engine) as session:
        session.add(stmt)
        session.commit()