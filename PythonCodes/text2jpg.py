from PIL import Image, ImageDraw
 
img = Image.new('RGB', (150, 11), color = (255, 255, 255))
 
d = ImageDraw.Draw(img)
d.text((1,-1), "Digital Manufacturing", fill=(0,0,0))
 
img.save('pil_text.png')