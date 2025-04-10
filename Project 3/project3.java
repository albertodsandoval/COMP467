import argparse
import os
import ffmpeg
import json


def main():
	parser = argparse.ArgumentParser()

	parser.add_argument("source", help="required file name")
	parser.add_argument("-w","--watermark", action="store_true",help="returns all cases by specified user")
	parser.add_argument("-g","--gif",action="store_true",help="when flagged, will return only repeatable bugs")
	parser.add_argument("-t","--thumbnail",type=str,help="when flagged, will return only blocker bugs")
	parser.add_argument("-m","--metadata",action="store_true",help="returns all cases on specified date MM/DD/YY format")

	args = parser.parse_args()

	if os.path.isfile(args.source):
		process_image(args.source, args)
	elif os.path.isdir(args.source):
		for file in os.listdir(args.source):
			if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
				path = os.path.join(args.source, file)
				process_image(path, args)

def process_image(source, args):
	new_name = update_file_name(source)
	if args.watermark:
		apply_watermark(source, new_name)
	if args.gif:
		apply_gif(source, new_name)
	if args.thumbnail != None:
		apply_thumbnail(source, new_name, args.thumbnail)
	if args.metadata:
		apply_metadata(source, new_name)

def update_file_name(path):
	filename = os.path.basename(path)
	name, ext = os.path.splitext(filename)
	version = name[-1]
	name = name[:-1]
	version = int(version)+1
	name += str(version)
	return name+ext

def apply_watermark(source, new_name):
	(
		ffmpeg
		.input(source)
		.output(new_name,vf=f"drawtext=text='{new_name}':fontcolor=white:fontsize=200:x=10:y=10",**{'frames:v': 1, 'update': 1})
		.run()
	)

def apply_thumbnail(source, new_name, dimensions):
	(
		ffmpeg
		.input(source)
		.output(new_name,vf=f"scale={dimensions}",**{'frames:v': 1,'update': 1})
		.run()
	)

def apply_metadata(source, new_name):

	output = ""

	try:
		probe = ffmpeg.probe(source)
		output = json.dumps(probe,indent=2)
	except ffmpeg.Error as e:
		print('Error:'. e.stderr.decode())

	with open("output.txt","w") as f:
		f.write(output)



if __name__ == "__main__":
	main()