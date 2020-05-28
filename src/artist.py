import random as rd
from polygon import Polygon
from PIL import Image, ImageDraw, ImageFilter
import tempfile
from copy import deepcopy
import math

class Artist():
    def __init__( self, DNA , dna_size, img_size):
        self. dna_size = dna_size
        self.img_size = img_size
        self.fittness = 0
        if DNA == None:
            self.generateDNA(dna_size)
        else:
            self.DNA = DNA

    def generateDNA(self ,dna_size ):
        self.DNA = []
        for i in range(dna_size):
            vectors = []
            n_vertex = rd.randrange(3,5)
            color = (rd.randrange(0,256),rd.randrange(0,256),rd.randrange(0,256),rd.randrange(0,256))
            for j in range(n_vertex):
                vectors.append((rd.randrange(0, self.img_size[0]),rd.randrange(0, self.img_size[1])))
            polygon = Polygon(color,vectors)
            self.DNA.append(polygon)

    def mutate(self):
        _DNA = deepcopy(self.DNA)
        _DNA[rd.randrange(0, len(self.DNA))].mutate(self.img_size)
        if _DNA == self.DNA:
            print("fuck")
        return _DNA

    def getFittness(self,create_img , original_img):
        fittness = 0
        for y in range(self.img_size[1]):
            for x in range(self.img_size[0]):
                R,G,B = create_img.getpixel((x,y))
                R_,G_,B_ = original_img.getpixel((x,y))
                fittness += math.sqrt((R - R_)**2 + (G-G_)**2 + (B-B_)**2)
        self.fittness = fittness


    def draw(self, size, bg, save = False, save_path=None, name = None):
        new_image = Image.new('RGB', size, bg)
        draw = Image.new('RGBA', size)
        pdraw = ImageDraw.Draw(draw)

        for polygon in self.DNA:
            pdraw.polygon(polygon.vectors, fill=polygon.color, outline=polygon.color)
            new_image.paste(draw, mask=draw)

        if save:
            new_image = new_image.filter(ImageFilter.GaussianBlur(radius=3))
            new_image.save(save_path + '/' + name + '.png')
        return new_image
