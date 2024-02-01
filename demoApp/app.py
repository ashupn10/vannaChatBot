import os
import vannaChatBot.demoApp.db as db
import pandas as pd
import vanna as vn
from dotenv import load_dotenv
from vanna.flask import VannaFlaskApp
load_dotenv()


# Get the db connection 

conn = db.db_Connect_thinMode()
ConnectionPool=db.db_Connect_thinModePool()

# overwrite the run_sql function 

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
        df=pd.DataFrame(result)
        # vn.generate_plotly_code(sql="sql",df=df)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()

    finally:
        if conn:
            ConnectionPool.release(conn)


#  set api for the vanna

vn.set_api_key(os.getenv('VANNA_API_KEY'))
models = vn.get_models()
print(models)
# check if the model exist

if 'mistralnew' not in models:
    print('creating Model')
    vn.create_model(model="mistralnew", db_type="oracle")
    vn.add_user_to_model(model='mistralnew',email=os.getenv('VANNA_USER'),is_admin=True)
    vn.update_model_visibility(public=True)
    print('model Created')
    print(vn.get_models())
else:
    vn.set_model('mistralnew')
    vn.add_user_to_model(model='mistralnew',email=os.getenv('VANNA_USER'),is_admin=True)
    vn.update_model_visibility(public=True)

vn.run_sql=run_sql
vn.run_sql_is_set = True
# vnn=model.model_vanna()


VannaFlaskApp(vn).run()
