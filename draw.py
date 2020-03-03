from PIL import Image, ImageDraw

im_units = Image.new("RGBA", (800, 800), (255,255,255,0))

# draw_polygon = ImageDraw.Draw(im_units, None)
# draw_polygon.polygon([(0,0), (400,0), (200,200)], fill=(170,170,170,255))

im = im_units.transpose(Image.FLIP_LEFT_RIGHT)
im.save('./test.png')

