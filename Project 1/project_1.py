baselight = open("Baselight_export_spring2025.txt","r")
xytech = open("Xytech_spring2025.txt","r")

xytech = xytech.read()
xytech = xytech.split()

start_index = xytech.index("Location:") + 1
end_index = xytech.index("Notes:")

xytech = xytech[start_index:end_index]

baselight = baselight.read()

baselight = baselight.split()

xytech_index = 1

for index, item in enumerate(baselight):
	if(not item.isdigit()):
		item = item.split("/")
		item = item[3:]
		print(item)
