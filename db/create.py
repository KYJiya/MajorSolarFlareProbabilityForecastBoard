from engine import dbEngine
import model


if __name__=="__main__":
    engine = dbEngine()
    conn = engine.connect()
    print(conn.scalar("select sysdate from dual"))
    model.Base.metadata.create_all(engine)