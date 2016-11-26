#Benjamin Ramirez
#November 23 2016
import pymysql
from pymysql import *
# conn= pymysql.connect(host='localhost',
#                       user='root',
#                       password='skate805',
#                       db='aerodb',
#                       charset='utf8mb4',
#                       cursorclass=pymysql.cursors.DictCursor)
# a=conn.cursor()
# sql='CREATE TABLE `users` (`id` int(11) NOT NULL AUTO_INCREMENT,`email` varchar(255) NOT NULL,`password` varchar(255) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;'
# a.execute(sql)

class MyDB():
    def __init__(self, host, user, password, database):

        self.database = database
        try:
            self.connection = pymysql.connect(host=host,
                                              user=user,
                                              password=password,
                                              db=database,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)

            self.cursor = self.connection.cursor()
        except:
            print("COULDNT CONNECT")


    def execute_query(self, query):
        try:
            print(query)
            self.cursor.execute(query)
        except:
            print("Query Failed")
