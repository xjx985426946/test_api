from mysql.new import Pydb

db  = Pydb("intbee")
cursor = db.dodb()

sql ='SELECT * FROM intbee_sell_bill_spread;'
cursor.execute(sql)
results = cursor.fetchall()