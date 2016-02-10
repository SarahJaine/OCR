from PIL import Image
import subprocess

def read_orig(file_path):
	## call tesseract to do OCR on the orig image
	subprocess.call(['tesseract', file_path, 'output'])

	## read resulting file and close
	output_file = open('output.txt','r')
	print output_file.read()
	output_file.close()

def read_bw(file_path,file_path_new):
	## open image pathway and convert image to black and white
	image = Image.open(file_path).convert("L")
	image.save(file_path_new)

	## call tesseract to do OCR on the new image
	subprocess.call(['tesseract', file_path_new, 'output'])

	## read resulting file and close
	output_file = open('output.txt','r')
	print output_file.read()
	output_file.close()

def read_contrast(file_path,file_path_new):
	## open image pathway and convert image to black and white
	image = Image.open(file_path).convert("L")
	
	## set image threshold value and save
	image = image.point(lambda x:0 if x<143 else 255)
	image.save(file_path_new)

	## call tesseract to do OCR on the new image
	subprocess.call(['tesseract', file_path_new, 'output'])

	## read resulting file and close
	output_file = open('output.txt','r')
	print output_file.read()
	output_file.close()

