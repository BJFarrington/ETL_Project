import pymongo
import newweatherapidata
import datetime


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.idahopotatoes_db



potatoes_col = db.temp

post = {"Data" : df}

potatoes_col.insert_one(post)

results = potatoes_col.find()
for result in results:
    print(result)
