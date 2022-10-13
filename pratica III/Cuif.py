import struct
from PIL import Image

class Cuif:
    
    # Construtor que criar uma imagem CUIF na memória
    def __init__(self,img,version,ids):
        if (img.mode!='RGB'):
            print('Image is not RGB, and will be converted to RGB')
            img=img.convert('RGB')
        self.image = img
        self.version = version
        self.number_of_students = len(ids)
        self.ids = ids
        self.width = img.size[0]
        self.height = img.size[1]
        self.raster = []
        self.file_stream= struct.pack('4sBB', 
                               bytes("CUIF",'ascii'), # Assinatura do arquivo
                               version, 
                               self.number_of_students)
        self.file_stream= self.file_stream + struct.pack('<II',img.size[0],img.size[1]) 
        for i in range(self.number_of_students):
            self.file_stream= self.file_stream + struct.pack('<I',ids[i]) 
                       
        if (version==1):
            self.generateCUIF1(img)  # Descompactado em formato RGB
        elif (version==2):
            self.generateCUIF2(img)

    
    # Método estático que criar uma imagem CUIF na memória a partir de um arquivo CUIF
    @staticmethod
    def openCUIF(filename):
        bmp = open(filename, 'rb')
        if (bmp.read(4).decode()!='CUIF'):
            raise ValueError('Invalid CUIF file')

        version = struct.unpack('B', bmp.read(1))[0]
        number_of_students = struct.unpack('B', bmp.read(1))[0]
        ids = []
        width =  struct.unpack('I', bmp.read(4))[0]
        height =  struct.unpack('I', bmp.read(4))[0]
        for i in range(number_of_students):
            ids.append(struct.unpack('I', bmp.read(4))[0])
        if (version==1):
            img = Cuif.readCUIF1(bmp,width,height)
        elif (version==2):
            img = Cuif.readCUIF2(bmp,width,height)

        return Cuif(img,version,ids)
            

    # Método estático que lê o raster (bitmap) para o formato CUIF.1
    @staticmethod
    def readCUIF1(bmp,width,height):
        r = Image.new( "L", (width,height))
        g = Image.new( "L", (width,height))
        b = Image.new( "L", (width,height))
        rasterR = r.load()
        rasterG = g.load()
        rasterB = b.load()
        for i in range(width):
            for j in range(height):
                rasterR[i,j] =  struct.unpack('B', bmp.read(1))[0]
        for i in range(width):
            for j in range(height):
                rasterG[i,j] = struct.unpack('B', bmp.read(1))[0]
        for i in range(width):
            for j in range(height):
                rasterB[i,j] = struct.unpack('B', bmp.read(1))[0]
        return Image.merge('RGB', (r, g, b))

    # Método que gera a parte de dados da imagem no formato CUIF.1
    def generateCUIF1(self,img):
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                (r, g, b) = img.getpixel((i, j))
                self.file_stream +=struct.pack('B',r)
                self.raster.append(r)
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                (r, g, b) = img.getpixel((i, j))
                self.file_stream +=struct.pack('B',g)
                self.raster.append(g)
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                (r, g, b) = img.getpixel((i, j))
                self.file_stream +=struct.pack('B',b)
                self.raster.append(b)

    # Método estático que lê o raster (bitmap) para o formato CUIF.2
    # Este método deve ser alterado para utilizar o espalo de cores YCbCr
    @staticmethod
    def readCUIF2(bmp,width,height):
        r = Image.new( "L", (width,height))
        g = Image.new( "L", (width,height))
        b = Image.new( "L", (width,height))
        rasterR = r.load()
        rasterG = g.load()
        rasterB = b.load()
        for i in range(width):
            for j in range(height):
                rasterR[i,j] =  struct.unpack('B', bmp.read(1))[0]
        for i in range(width):
            for j in range(height):
                rasterG[i,j] = struct.unpack('B', bmp.read(1))[0]
        for i in range(width):
            for j in range(height):
                rasterB[i,j] = struct.unpack('B', bmp.read(1))[0]
        return Image.merge('RGB', (r, g, b))

    # Método que gera a parte de dados da imagem no formato CUIF.2
    # Este método deve ser alterado para utilizar o espalo de cores YCbCr
    def generateCUIF2(self,img):
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                (r, g, b) = img.getpixel((i, j))
                self.file_stream +=struct.pack('B',r)
                self.raster.append(r)
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                (r, g, b) = img.getpixel((i, j))
                self.file_stream +=struct.pack('B',g)
                self.raster.append(g)
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                (r, g, b) = img.getpixel((i, j))
                self.file_stream +=struct.pack('B',b)
                self.raster.append(b)
                
    def rgb2YCbCr():
        print('Método que deve converter componentes RGB para YCbCr')

    # Método que salva a imagem CUIF em arquivo                
    def save(self,filename):
        f = open(filename, "wb")
        f.write(self.file_stream)
        f.close()
        
    # Método que mostra a imagem CUIF
    def show(self):
        self.image.show()
       
    
    # Método que imprime o cabeçalho CUIF
    def printHeader(self):
        print('Version: %s' % self.version)
        print('Number of Students: %s' % self.number_of_students)
        print('Students: %s' % self.ids)
        print('Width: %s' % self.width)
        print('Height: %s' % self.height)
 
    # Método que salva a imagem CUIF no formato BMP
    def saveBMP(self,filename):
        r = Image.new( "L", (self.width,self.height))
        g = Image.new( "L", (self.width,self.height))
        b = Image.new( "L", (self.width,self.height))
        rasterR = r.load()
        rasterG = g.load()
        rasterB = b.load()
        index = 0
        if (self.version==1):
            for i in range(self.width):
                for j in range(self.height):
                    rasterR[i,j] = self.raster[index]
                    index = index+1
            for i in range(self.width):
                for j in range(self.height):
                    rasterG[i,j] = self.raster[index]
                    index = index+1
            for i in range(self.width):
                for j in range(self.height):
                    rasterB[i,j] = self.raster[index]
                    index = index+1
            img = Image.merge('RGB', (r, g, b))
            img.save(filename)
        
            
if __name__ == "__main__":
    img = Image.open("teste.bmp")
    ids = [17100532,21220183]
    cuif = Cuif(img,1,ids)
    cuif.printHeader()
    cuif.show()
    cuif.save('teste1.cuif')
    cuif.saveBMP('teste1.bmp')
    cuif2 = Cuif.openCUIF('teste1.cuif')
    cuif2.printHeader()
    cuif2.show()
    print("THE END")
