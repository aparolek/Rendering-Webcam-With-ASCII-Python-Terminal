from PIL import Image, ImageOps

img = ImageOps.grayscale(Image.open(r"test.png"))


characters = "@@@@@@@@@@@@%%%%%%%%#########********+++++++++===="


size = img.size
art = ""
for j in range(0,size[1]):
    line = ""
    for i in range(0, size[0]):
        line += characters[round(img.getpixel((i,j))/255 * len(characters)  - 1)]
        line += characters[round(img.getpixel((i,j))/255 * len(characters)  - 1)]
    art += line + "\n"


a = open("art.txt", "w")
# best viewed in text file, cntrl + - to zoom in and out of a text file

a.write(art)
print("Complete")
