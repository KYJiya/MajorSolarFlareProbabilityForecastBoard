from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.schema import Sequence


Base = declarative_base()


class hmi_sharp(Base):
    __tablename__ = "hmi_sharp"

    hmi_sharp_id_seq = Sequence('hmi_sharp_id_seq', metadata=Base.metadata)
    id = Column(
        Integer, 
        hmi_sharp_id_seq, 
        server_default=hmi_sharp_id_seq.next_value(),
        primary_key=True
    )
    date = Column(String(100))
    noaa_ar = Column(String(100))
    h_ctotal = Column(Float)    
    j_ztotal = Column(Float)
    rho_tot = Column(Float)
    phi = Column(Float)
    h_cabs = Column(Float)
    j_zsum = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'''hmi_sharp(
            id={self.id!r}, 
            date={self.date!r}, 
            noaa_ar={self.noaa_ar!r},
            h_ctotal={self.h_ctotal!r},
            j_ztotal={self.j_ztotal!r},
            phi={self.phi!r},
            h_cabs={self.h_cabs!r},
            j_zsum={self.j_zsum!r},
            created_at={self.created_at!r}    
        )'''


class probability_model_long(Base):
    __tablename__ = "probability_model_long"

    probability_model_long_id_seq = Sequence('probability_model_long_id_seq', metadata=Base.metadata)
    id = Column(
        Integer, 
        probability_model_long_id_seq, 
        server_default=probability_model_long_id_seq.next_value(),
        primary_key=True
    )
    date = Column(String(100))
    noaa_ar = Column(String(100))
    p_l_totusjh = Column(Float)
    p_l_totusjz = Column(Float)
    p_l_totpot = Column(Float)
    p_l_usflux = Column(Float)
    p_l_absnjzh = Column(Float)
    p_l_savncpp = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'''probability_model_long(
            id={self.id!r}, 
            date={self.date!r}, 
            noaa_ar={self.noaa_ar!r},
            p_l_totusjh={self.p_l_totusjh!r},
            p_l_totusjz={self.p_l_totusjz!r},
            p_l_totpot={self.p_l_totpot!r},
            p_l_usflux={self.p_l_usflux!r},
            p_l_absnjzh={self.p_l_absnjzh!r},
            p_l_savncpp={self.p_l_savncpp!r},
            created_at={self.created_at!r}
        )'''


class probability_model(Base):
    __tablename__ = "probability_model"

    probability_model_id_seq = Sequence('probability_model_id_seq', metadata=Base.metadata)
    id = Column(
        Integer, 
        probability_model_id_seq, 
        server_default=probability_model_id_seq.next_value(),
        primary_key=True
    )
    date = Column(String(100))
    noaa_ar = Column(String(100))
    p_totusjh = Column(Float)
    p_totusjz = Column(Float)
    p_totpot = Column(Float)
    p_usflux = Column(Float)
    p_absnjzh = Column(Float)
    p_savncpp = Column(Float)
    r_m = Column(Float)
    r_s = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'''probability_model(
            id={self.id!r}, 
            date={self.date!r}, 
            noaa_ar={self.noaa_ar!r},
            p_totusjh={self.p_totusjh!r},
            p_totusjz={self.p_totusjz!r},
            p_totpot={self.p_totpot!r},
            p_usflux={self.p_usflux!r},
            p_absnjzh={self.p_absnjzh!r},
            p_savncpp={self.p_savncpp!r},
            created_at={self.created_at!r}
        )'''
        