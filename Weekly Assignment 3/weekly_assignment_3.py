import csv

intarray = [["index","value"]]

i = 1;
with open("ingest_this.txt","r") as file:
	for line in file:
		sum = 0
		values = line.split()
		if(len(values)!=0): #ignores empty lines
			for token in values:
				if(token.isdigit()):
					sum+=int(token)
			intarray.append([i,sum])
			i+=1

print(intarray)

# writes data array to a csv file
with open('output.csv','w',newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(intarray)