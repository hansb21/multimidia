## Estudantes
## Hans Buss Heidemann - 19100528
## Júlio Gonçalves Ramos - 19203165


from urllib.request import urlopen
from PIL import Image # package pillow
import math

def criarImagemRGB():
    img = Image.new( "RGB", (512,512))
    raster = img.load()
    for i in range(0, img.size[0], 2):
        for j in range(0, img.size[1], 2):
            raster[i,j] = (220,219,97,255)
    (r, g, b) = img.getpixel((0, 0))
    print(r, g, b)
    return img

def criarImagemCinza():
    img = Image.new( "L", (256,512))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            raster[i,j] = i
    y = img.getpixel((5, 5))
    print(y)
    return img

def criarImagemBinaria():
    # checkerboard pattern.
    img = Image.new("1", (250,150))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if ((int(i/50)+int(j/50)) % 2 == 0):
                raster[i,j] = 0
            else:
                raster[i,j] = 1
    y = img.getpixel((0, 0))
    print(y)
    return img

def reduzirImagem(img):
    novaImg = Image.new( "RGB", (img.size[0]//2,img.size[1]//2))
    raster = novaImg.load()
    referencia = img.load()
    for i in range(0,img.size[0],2):
        for j in range(0,img.size[1],2):
            raster[i//2,j//2] = referencia[i,j]
    (r, g, b) = img.getpixel((0, 0))
    print(r, g, b)
    return novaImg

def img_cinza(img_og):
    img = Image.new( "L", (img_og.size[0], img_og.size[1]))
    ref = img_og.load()
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = img_og.getpixel((i, j))
            raster[i,j] = int(0.3 * r + 0.59 * g + 0.11 * b)
    return img

def img_bin(img_og):
    img = Image.new("1", (img_og.size[0], img_og.size[1]))
    raster = img.load()
    ref = img_og.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = img_og.getpixel((i, j))
            total= int(0.3 * r + 0.59 * g + 0.11 * b)
            if total >= 127:
                raster[i, j] = 1
            else:
                raster[i, j] = 0

    return img

def split_rbg(img_og):
    imgs = []
    raster = []
    for i in range(0, 3):
        imgs.append(Image.new( "RGB", (img_og.size[0], img_og.size[1])))
        print("Ok")
        raster.append(imgs[i].load())
       
    for i in raster:
        print(i)
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = img_og.getpixel((i, j))
            raster[0][i, j] = (r, 0, 0, 255)
            raster[1][i, j] = (0, g, 0, 255)
            raster[2][i, j] = (0, 0, b, 255)
    
    return imgs



img = Image.open(urlopen("https://www.inf.ufsc.br/~roberto.willrich/INE5431/peixe.jpg"))

img.show()
img_cinza(img).show()
img_bin(img).show()
imgs = split_rbg(img)
for i in imgs:
    i.show()
#criarImagemRGB().show()
#criarImagemCinza().show()
#criarImagemBinaria().show()


