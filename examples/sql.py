import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='tester',
                             password='test',
                             database='test',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    # do something
   with connection.cursor() as cursor:
        try:
            sql = "update `user` set `age` = %s where `name` = %s"
            cursor.execute(sql, (23, 'python'))

            # connection is not autocommit by default. So you must commit to save your changes.
            connection.commit()
        except pymysql.err.ProgrammingError:
            print('Exception catched!!!')
