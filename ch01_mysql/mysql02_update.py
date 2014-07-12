import mysql.connector as mysql

user = 'root'
pwd  = ''
host = '127.0.0.1'
db   = 'test'
data_file = 'mysql-test.txt'
create_table_sql = "CREATE TABLE IF NOT EXISTS mytable ( \
                    id int(10) AUTO_INCREMENT PRIMARY KEY, \
            name varchar(20), age int(4) ) \
            CHARACTER SET utf8"
 
cnx = mysql.connect(user=user, password=pwd, host=host, database=db)
cursor = cnx.cursor()
#尝试更新
update_sql="update mytable set name='shaoling2' where id=1"
cursor.execute(update_sql)
choice=input("Do you want to continue ?").strip()
if choice=='y':
    print("commit")
    cnx.commit()
    cursor.close()
    cnx.close()
else:
    #cnx.commit() 
    cursor.close()
    cnx.close()


