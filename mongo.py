import pymongo
import weather api data


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.idaho_potatoes_db

potatoes_col = db.temp

potatoes_col.insert_one(all_data)