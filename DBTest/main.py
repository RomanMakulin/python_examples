import pymysql
from config import host, password, db_name, user

try:
    connection = pymysql.connect(
        host = host, 
        password = password,
        user = user,
        port = 3306,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )
    print("Success!")

    try:
        cursor = connection.cursor()

        #drop table
        drop_table = "drop table if exists test"
        cursor.execute(drop_table)
        connection.commit()

        # create table
        create_query = "create table if not exists test( id int primary key auto_increment, name_s varchar(45));"
        cursor.execute(create_query)
        print("Table was created")
        connection.commit()

        # insert
        insert_q = "insert into test (name_s) values ('roman'), ('olga'), ('ann');"
        cursor.execute(insert_q)
        print("Table was inserted")
        connection.commit()

        # update
        cursor.execute("UPDATE test SET name_s = 'new' WHERE id = 1;")
        connection.commit()

        # delete
        cursor.execute("delete from test where id = 3;")
        connection.commit()

        # select
        cursor.execute("Select * FROM test;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        
    finally:
        connection.close()    

except Exception as ex:
    print("Error. Disconnected")
    print(ex)    