import pymongo
import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument("-u","--user", type=str,help="returns all cases by specified user")
parser.add_argument("-r","--repeatable",action="store_true",help="when flagged, will return only repeatable bugs")
parser.add_argument("-b","--blocker",action="store_true",help="when flagged, will return only blocker bugs")
parser.add_argument("-d","--date",type=str,help="returns all cases on specified date MM/DD/YY format")
parser.add_argument("-s","--spring",action="store_true",help="when flagged, will return only cases from spring. both fall and spring by default")
parser.add_argument("-f","--fall",action="store_true",help="when flagged, will return only cases from fall. both fall and spring by default")


args = parser.parse_args()

MONGO_URI = "mongodb+srv://albertosandoval950:5uGWgQ5JRvyd6DJM@cluster0.doxfk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

myclient = pymongo.MongoClient(MONGO_URI)

mydb = myclient["Project2"]

SpringCollection = mydb["Spring2024"]
FallCollection = mydb["Fall2024"]

query = {}

if args.user != None:
	query["Test Owner"] = args.user
if args.repeatable:
	query["Repeatable?"] = {"$in": ["Yes", "yes", "YES"]}
if args.blocker:
	query["Blocker?"] = {"$in": ["Yes", "yes", "YES"]}
if args.date != None:
	dateData = args.date.split("/")
	print(dateData)
	queryDate = datetime(int("20"+dateData[2]),int(dateData[0]),int(dateData[1]))
	query["Build #"] = queryDate

data = pd.DataFrame()
if args.spring and args.fall:
	data = pd.concat([data,pd.DataFrame(SpringCollection.find(query))],ignore_index=True)
	data = pd.concat([data,pd.DataFrame(FallCollection.find(query))],ignore_index=True)
elif args.spring:
	data = pd.concat([data,pd.DataFrame(SpringCollection.find(query))],ignore_index=True)
elif args.fall:
	data = pd.concat([data,pd.DataFrame(FallCollection.find(query))],ignore_index=True)
else:
	data = pd.concat([data,pd.DataFrame(SpringCollection.find(query))],ignore_index=True)
	data = pd.concat([data,pd.DataFrame(FallCollection.find(query))],ignore_index=True)

data = data.drop_duplicates();
data.to_csv('output.csv',index=False)

print(data)