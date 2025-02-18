import csv

# imports provided files
baselight = open("Baselight_export_spring2025.txt","r")
xytech = open("Xytech_spring2025.txt","r")

# stores contexts of xytech file
# and separates string in list
xytech = xytech.read()
xytech = xytech.split()

# finds index of filepaths in xytech file
start_index = xytech.index("Location:") + 1
end_index = xytech.index("Notes:")

# reassigns array to only the filepath locations
xytech = xytech[start_index:end_index]

# initializes hashmap
hash_map = {}

# loops through all filepath locations on xytech
# and adds the variable bit of the string to the
# key and the entire filepath to the value:
# example
#
# KEY -> reel1/partA/1920x1080
# VALUE -> /hpsans13/production/dogman/reel1/partA/1920x1080
#
# since the variable bit is the same in baselight and on prem,
# we can search for the corresponding on prem filepath if we
# can read the variable bit on the baselight filepath
for index, item in enumerate(xytech):
	hash_map[item[28:]] = item

# storing content of baselight file as string
# and spliting it into an array
baselight = baselight.read()
baselight = baselight.split()

# initializing the an array with "Location" and
# "Frames" as the header
data = [["Location","Frames"]]

# initializes start frame and location to 0/""
start_frame = 0
end_frame = 0
current_location = ""

# starts for-loop that iterates through baselight tokens
for index, token in enumerate(baselight):

	# determines whether or not the current token is a digit
	if(not token.isdigit()):

		# if it is not a digit, it must be a filepath
		# so we set the current location to the hashmap value
		# at the read key from the token
		current_location = hash_map[token[29:]]

		# we also set the start_frame to be the NEXT token
		# because we know a frame is always preceeded by a 
		# filepath
		start_frame = baselight[index+1]

	# else the token is a digit
	else:
		print(token)

		# ensures we will not go out of range since we are testing
		# the NEXT index
		if(index+1 <= len(baselight)-1):

			# tests whether next frame is consecutive to current one
			if(baselight[index+1] == str(int(baselight[index])+1)):

				# updates the end frame to be the next frame
				end_frame = baselight[index+1]

			# next frame is NOT consecutive to current
			# we know we are done with this range and need
			# to store it
			else:

				# tests whether it is a range or a standalone frame
				if(start_frame == end_frame):

					# appends an array with the location and the frame
					data.append([current_location,str(start_frame)])

				# range of frames
				else:

					# appends an array with location and start frame - end frame
					data.append([current_location,str(start_frame)+"-"+str(end_frame)])

				# tests whether next token is a frame or a filepath
				if(baselight[index+1].isdigit()):

					# if it is a frame, we update the start frame
					# and end frame to be the next frame since we are 
					# done with our current range
					start_frame = baselight[index+1]
					end_frame = baselight[index+1]
				else:
					start_frame = baselight[index+2]
					end_frame = baselight[index+2]

		# if index+1 goes out of bounds, we still have to return last frame
		else:

			# tests whether it is a range or a standalone frame
			if(start_frame == end_frame):

				# appends an array with the location and the frame
				data.append([current_location,str(start_frame)])

			# range of frames
			else:

				# appends an array with location and start frame - end frame
				data.append([current_location,str(start_frame)+"-"+str(end_frame)])


# writes data array to a csv file
with open('output.csv','w',newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data)