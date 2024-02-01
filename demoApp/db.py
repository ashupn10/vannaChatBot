import oracledb

def db_Connect_thinMode():
    connection=oracledb.connect(user="MOVIESTREAM",password="watchS0meMovies#",dsn="(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.ap-mumbai-1.oraclecloud.com))(connect_data=(service_name=ga97be9115f23e9_moviestreamworkshop2_low.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))")
    return connection

def db_Connect_thinModePool():
    ConnectionPool=oracledb.create_pool(user="MOVIESTREAM",password="watchS0meMovies#",dsn="(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.ap-mumbai-1.oraclecloud.com))(connect_data=(service_name=ga97be9115f23e9_moviestreamworkshop2_low.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))",min=1,max=5,increment=1)
    return ConnectionPool


# connection=db_Connect_thinMode()

# cursor=connection.cursor()
# cursor.execute("select * from movies limit 10")