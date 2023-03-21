import json
from pymongo import MongoClient
import os

client = MongoClient("mongodb://127.0.0.1:27117,127.0.0.1:27118")
db = client["MSS"]
collection = db["songs"]

rootdir = "MSS-JSON/"
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        with open(rootdir + file) as f:
            data = json.load(f)
            collection.insert_one(data)

client.close()
