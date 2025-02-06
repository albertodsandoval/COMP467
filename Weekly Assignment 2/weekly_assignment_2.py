import re
with open("ingest_this.txt","r") as file:
	for line in file:
		print(re.findall(r'\d+',line))	