from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func


Base = declarative_base()


class Flare(Base):
    __tablename__ = "Flare"

    id = Column(Integer, primary_key=True)
    date = Column(String(100))
    noaa_ar = Column(String(100))
    h_ctotal = Column(Float)
    p_totusjh = Column(Float)
    j_ztotal = Column(Float)
    p_totusjz = Column(Float)
    rho_tot = Column(Float)
    p_totpot = Column(Float)
    phi = Column(Float)
    p_usflux = Column(Float)
    h_cabs = Column(Float)
    p_absnjzh = Column(Float)
    j_zsum = Column(Float)
    p_savncpp = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'''Flare(
            id={self.id!r}, 
            date={self.date!r}, 
            noaa_ar={self.noaa_ar!r},
            h_ctotal={self.h_ctotal!r},
            p_totusjh={self.p_totusjh!r},
            phi={self.phi!r},
            p_usflux={self.p_usflux!r},
            h_cabs={self.h_cabs!r},
            p_absnjzh={self.p_absnjzh!r},
            j_zsum={self.j_zsum!r},
            p_savncpp={self.p_savncpp!r},
            created_at={self.created_at!r}    
        )'''