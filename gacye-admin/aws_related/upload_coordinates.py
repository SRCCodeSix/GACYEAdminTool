import json 
import pymysql

s = open('locations.json')
data = json.load(s)

n = len(data['features'])

print(data['features'][2]['geometry']) # [-149.647, 61.8122] which is longitude, latitude


RDS_HOSTNAME='database-2.cej2zfq0kc69.us-east-2.rds.amazonaws.com'
RDS_USERNAME='admin'
RDS_PASSWORD='GacyeDB123'
RDS_PORT=3306
db = pymysql.connect(host=RDS_HOSTNAME, user =RDS_USERNAME, password=RDS_PASSWORD)

# you have cursor instance here
cursor = db.cursor()
cursor.execute("select version()")

version = cursor.fetchone()

sql = '''SHOW databases'''
cursor.execute(sql)
resp = cursor.fetchall()
print(resp)

sql = '''USE defaultDB'''
cursor.execute(sql)

sql = '''SHOW tables'''
cursor.execute(sql)
resp = cursor.fetchall()
print(resp)

sql = '''DROP TABLE IF EXISTS coordinates'''
cursor.execute(sql)

sql = '''CREATE TABLE coordinates (
    id INT PRIMARY KEY AUTO_INCREMENT,
    latitude DECIMAL(9, 6) NOT NULL,
    longitude DECIMAL(9, 6) NOT NULL
)'''
cursor.execute(sql)

sql = '''SHOW tables'''
cursor.execute(sql)
resp = cursor.fetchall()
print(resp)

for i in range(n):
    coordinates = data['features'][i]['geometry']['coordinates']
    latitude, longitude = round(coordinates[1],3), round(coordinates[0],3)
    sql = f'''INSERT INTO coordinates (latitude, longitude) VALUES (
        {latitude},
        {longitude}
    )'''
    cursor.execute(sql)


sql = '''SELECT * FROM coordinates'''
cursor.execute(sql)
resp = cursor.fetchall()
print(resp)