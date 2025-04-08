import pymongo
import pandas as pd

MONGO_URI = "mongodb+srv://albertosandoval950:5uGWgQ5JRvyd6DJM@cluster0.doxfk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

myclient = pymongo.MongoClient(MONGO_URI)

mydb = myclient["COMP467"]


collection = mydb["Weekly Assignment 6"]

data_dict = pd.read_excel("WeeklyAssignment6_datasample.xlsx").to_dict(orient="records")

collection.insert_many(data_dict)

rizzler = collection.find_one({"Test Owner":"The Rizzler"},{"_id":0,"Test #":1, "Test Case":1})

print(rizzler)