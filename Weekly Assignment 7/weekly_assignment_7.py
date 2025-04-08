import ffmpeg
stream = ffmpeg.input('input.MOV')

(
	ffmpeg
	.input('input.MOV')
	.output('image-%d.png',r=1,f='image2')
	.run()
)