import cx_Oracle
from sqlalchemy import create_engine
from dotenv import load_dotenv
import sys
import os


def dbEngine():
    load_dotenv(verbose=True)

    if sys.platform.startswith("darwin"):
        cx_Oracle.init_oracle_client(
            lib_dir=os.environ.get("HOME")+"/MajorSolarFlareProbabilityForecastBoard/db/instant/instantclient_21_6",
            config_dir="")
    elif sys.platform.startswith("win"):
        cx_Oracle.init_oracle_client(
            lib_dir=r"db\instant\instantclient_21_3",
            config_dir=r"db\instant\Wallet_DB20220512224308")
    # else assume system library search path includes Oracle Client libraries
    # On Linux, use ldconfig or set LD_LIBRARY_PATH, as described in installation documentation.

    username = "admin"
    # set the password in an environment variable called "MYPW" for security
    password = os.environ.get("password")
    dsn = "db20220512224308_high"

    engine = create_engine(
        f'oracle://{username}:{password}@{dsn}/?encoding=UTF-8&nencoding=UTF-8', max_identifier_length=128)

    return engine

# with engine.connect() as conn:
#     print(conn.scalar("select sysdate from dual"))