from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os

png_file = os.path.join(os.path.dirname(__file__), "baby.jpg")
text = '宝宝的第108天'
out_file = os.path.join(os.path.dirname(__file__), "output.jpg")


# im = Image.open(png_file).convert('RGBA')
# txt=Image.new('RGBA', im.size, (0,0,0,0))
# fnt=ImageFont.truetype(os.path.join(os.path.dirname(__file__), "DENGL.TTF"), 20)
# d=ImageDraw.Draw(txt)
# d.text((txt.size[0]-80,txt.size[1]-30), "cnBlogs",font=fnt, fill='blue')
# out=Image.alpha_composite(im, txt)
# out.show()

img = Image.open(png_file)
# size = [0, 0]
# size[0] = int(img.size[0]/5)
# size[1] = int(img.size[1]/5)
watermark = Image.new('RGBA', img.size, (0,0,0,0))
FONT = os.path.join(os.path.dirname(__file__), "FZZJ-LYTJF.TTF")
size = 20
n_font = ImageFont.truetype(FONT, size)
n_width, n_height = n_font.getsize(text)
print(n_width, n_height)
text_box = min(watermark.size[0], watermark.size[1])
# while n_width+n_height < text_box:
#     size += 2
#     n_font = ImageFont.truetype(FONT, size)
#     n_width, n_height = n_font.getsize(text)

# text_width = (watermark.size[0] - n_width) / 2
# text_height = (watermark.size[1] - n_height) / 2

print(img.size)
text_width_position = 200
text_height_position = 180
draw = ImageDraw.Draw(watermark, 'RGBA')
draw.text((text_width_position, text_height_position), text, font=n_font, fill="#21ACDA")
watermark = watermark.rotate(0)
alpha = watermark.split()[1]
alpha = ImageEnhance.Brightness(alpha).enhance(0.9)
watermark.putalpha(alpha)
Image.composite(watermark, img, watermark).save(out_file, 'JPEG')

