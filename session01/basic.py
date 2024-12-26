from PIL import Image

im_file = "../assets/image_01.jpg"

im = Image.open(im_file)
im.rotate(45)

im.save("../assets/temp/page_01.jpg")

print(im)