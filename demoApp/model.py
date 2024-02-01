import vanna
import vannaChatBot.demoApp.db as db
import os
from vanna.remote import VannaDefault
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

conn = db.db_Connect_thinMode()
ConnectionPool=db.db_Connect_thinModePool()


# ConnectionPool = db.db_Connect_thinMode()
def run_sql(sql: str) -> pd.DataFrame:
    try:
        sql="select * from movies"
        print(sql)
        conn = ConnectionPool.acquire()
        cursor = conn.cursor()       
        # print(sql)
        cursor.execute("select * from movies")
        result = cursor.fetchall()
        cursor.close()
        print(result)
        return pd.DataFrame(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()

    finally:
        if conn:
            ConnectionPool.release(conn)


def model_vanna():
    # api_key = vanna.get_api_key('ashutosh.mishra@conneqtiongroup.com')
    # print(api_key)
    vanna_model_name = 'chinook'
    vn = VannaDefault(model=vanna_model_name, api_key=os.getenv('VANNA_API_KEY'))
    vn.run_sql = run_sql
    return vn