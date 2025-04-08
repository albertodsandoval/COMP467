import pymongo

MONGO_URI = "mongodb+srv://albertosandoval950:y6fmhzmwJMY0kZV9@users.a7kxh.mongodb.net/?retryWrites=true&w=majority&appName=Users"

myclient = pymongo.MongoClient(MONGO_URI)

mydb = myclient["LevelUp"]


collection = mydb["users"]

mydict = {"username":"John","password":"password"}

x = collection.insert_one(mydict)

print(collection.find_one({"username":"John"}))

# {'_id': ObjectId('67bec22323fa905cdbe6dd55'), 'username': 'John', 'password': 'password'}