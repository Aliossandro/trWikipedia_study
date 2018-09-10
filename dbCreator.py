# -*- coding: utf-8 -*-
import os
import sys
# reload(sys)
# sys.setdefaultencoding("utf8")

import psycopg2

# connection parameters
def get_db_params():
    params = {
        'database': 'trWiki',
        'user': 'postgres',
        'password': 'postSonny175',
        'host': 'localhost',
        'port': '5432'
    }
    conn = psycopg2.connect(**params)
    return conn

# create table
def create_table():
    ###statement table query
    query_table_1 = """
    		CREATE TABLE IF NOT EXISTS revision_metadata (    		    
    			page VARCHAR(255),
    			rev_Id VARCHAR(255) PRIMARY KEY,
    			par_Id VARCHAR(255),
                time_Stamp VARCHAR(255),
                user_Name VARCHAR(255),
                user_Id VARCHAR(255),
                revert VARCHAR(255),
                reverted VARCHAR(255),
                bytes VARCHAR(255),
                namespace VARCHAR(255)
                )
    		"""

    conn = None

    try:
        conn = get_db_params()
        cur = conn.cursor()

        cur.execute(query_table_1)
        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

