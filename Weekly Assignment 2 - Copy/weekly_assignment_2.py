with open("ingest_this.txt","r") as file:
	for line in file:
		values = line.split()
		for token in values:
			if(token.isdigit()):
				print(token+ " ", end="")
		print()