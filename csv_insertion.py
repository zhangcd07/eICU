import pandas as pd
import csv
from io import StringIO
from sqlalchemy import create_engine

#从dataframe写入数据库的函数 -the function to write dataframe into postgreSQL
def psql_insert_copy(table, conn, keys, data_iter):
    # gets a DBAPI connection that can provide a cursor
    dbapi_conn = conn.connection
    with dbapi_conn.cursor() as cur:
        s_buf = StringIO()
        writer = csv.writer(s_buf)
        writer.writerows(data_iter)
        s_buf.seek(0)

        columns = ', '.join('"{}"'.format(k) for k in keys)
        if table.schema:
            table_name = '{}.{}'.format(table.schema, table.name)
        else:
            table_name = table.name

        sql = 'COPY {} ({}) FROM STDIN WITH CSV'.format(
            table_name, columns)
        cur.copy_expert(sql=sql, file=s_buf)

#打开eICU数据库 -set up connection with local eICU database
engine = create_engine('postgresql://USER_NAME:PASSWORD@HOST_NAME:5432/eICU')

#提取CSV并写入数据库的函数。使用说明：调用最后一个函数，变量名为希望导入的CSV数据名加引号。导入成功后postgreSQL中会出现一个新的表格，进入该表格然后调整列性质即可，注意table名不可以含有大写字母。
#this function could insert csv to a new table. Instruction：do not include capital letter in the variable.
#example：insert_csv_to_new_table('intakeoutput')。
def insert_csv_to_new_table(table):
    df=pd.read_csv('YOUR_LOCAL_EICU_PATH/%s.csv/%s.csv'%(table,table))
    df.to_sql(table, engine, method=psql_insert_copy)
    del df
    print('successfully added the csv to %s' %table)

#向已有数据表添加数据的函数。 -this function could add csv to existing table
def add_csv_to_exist_table(table):
    df=pd.read_csv('YOUR_LOCAL_EICU_PATH/%s.csv/%s.csv'%(table,table))
    df.to_sql(table, engine, if_exists='append', method=psql_insert_copy)
    del df
    print('successfully appended the csv to %s' %table)

#若insert_csv_to_new_table因文件过大报错，可使用此函数。 if you are having trouble with the first function, try this one as it works for extra-large csv
def insert_large_csv_to_new_table(table):
    df=pd.read_csv('YOUR_LOCAL_EICU_PATH/%s.csv/%s.csv'%(table,table))
    n=700000
    df1=df.iloc[0:n,:]
    df1.to_sql(table, engine, method=psql_insert_copy)
    while n<df.shape[0]:
        df1=df.iloc[n:n+700000,:]
        df1.to_sql(table, engine, if_exists='append', method=psql_add_copy)
        n=n+700000  
    df1=vital.iloc[n:,:]
    df1.to_sql(table, engine, if_exists='append', method=psql_add_copy)
    del df
    del df1
    print('successfully added the large file to %s' %table) 