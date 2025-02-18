<<<<<<< HEAD
import re
with open("ingest_this.txt","r") as file:
	for line in file:
=======
import re
with open("ingest_this.txt","r") as file:
	for line in file:
>>>>>>> master
		print(re.findall(r'\d+',line))	