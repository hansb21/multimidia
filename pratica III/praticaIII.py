from PIL import Image
from Cuif import Cuif
import math
import statistics

def PSNR(original,decodificada):
    print('Implemente o cálculo do PSNR aqui')
    og = original.load()
    dec = decodificada.load()
    mse = statistics.mean((og - dec) ** 2)
  
    if mse == 0:
       return 9999999999999

    maxB = 255.0
    psnr = math.log10(maxB / math.sqrt(mse)) * 20
    
    return psnr
if __name__ == "__main__":
    img = Image.open("mandril.bmp")
    matriculas = [17100532,21220183, 19100528, 19203165]
    
    # instancia objeto Cuif, convertendo imagem em CUIF.1
    cuif = Cuif(img,1,matriculas)
    
    # imprime cabeçalho Cuif
    cuif.printHeader()
    
    # mostra imagem Cuif
    cuif.show()
    
    #gera o arquivo Cuif.1
    cuif.save('mandril1.cuif')
    
    #Abre um arquivo Cuif e gera o objeto Cuif
    cuif2 = Cuif.openCUIF('mandril1.cuif')
    
    # Converte arquivo Cuif em BMP e mostra
    cuif2.saveBMP('mandril1.bmp')
    cuif2.show()
    img_dec = Image.open('mandril1.bmp')
    print(PSNR(img, img_dec)) 
    print("THE END")
