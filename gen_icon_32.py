from PIL import Image, ImageDraw, ImageFont
import sys
import os
import getopt

chapter_index = None
output_dir = None

argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv, "i:o:", 
                               ["index =",
                                "output_dir ="])
  
except:
    print("Error")

for opt, arg in opts:
    if opt in ['-i', '--index']:
        chapter_index = arg
    elif opt in ['-o', '--output_dir']:
        output_dir = arg
  

print( chapter_index , output_dir)

if chapter_index != None and output_dir != None:
	
	if os.path.exists(output_dir):
		width = 32
		height = 32

		message = "%02d" % int(chapter_index)
		img = Image.new("RGB", (width,height), color='gray')
		imgDraw = ImageDraw.Draw(img)
		font = ImageFont.truetype("arialbd.ttf", size=20)
		textWidth, textHeight = imgDraw.textsize(message, font=font)
		xText = (width - textWidth) / 2
		yText = (height - textHeight) / 2

		# imgDraw.text((xText, yText), message, font=font, fill=(255, 255, 0))
		imgDraw.text((xText, yText),message,font=font, fill=(255,255,255))
		filename = "%s/chapter_%s_32.png" % (output_dir,message)
		img.save(filename)
	else:
		print("Usage : ./gen_icon_32 <chapter_index> <output_dir>")
		print("Error : %s directory not exists" % (output_dir))