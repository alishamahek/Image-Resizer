from PIL import Image
# import os

image = Image.open("n.png")
image.thumbnail((400,400))
image.save("3.png")
print(image.size)
# os.remove("UNSPLASH.jpg")