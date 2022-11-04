from PIL import Image, ImageDraw, ImageFont

width = 32
height = 32

message = "03"
img = Image.new("RGB", (width,height), color='gray')
imgDraw = ImageDraw.Draw(img)
font = ImageFont.truetype("arialbd.ttf", size=20)
textWidth, textHeight = imgDraw.textsize(message, font=font)
xText = (width - textWidth) / 2
yText = (height - textHeight) / 2

# imgDraw.text((xText, yText), message, font=font, fill=(255, 255, 0))
imgDraw.text((xText, yText),message,font=font, fill=(255,255,255))
filename = "chapter_%s_32.png" % (message)
img.save(filename)