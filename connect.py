import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="stemsa019",
    database='pelanggan'

)



db.close()
