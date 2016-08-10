from PIL import Image
from utils.Matrix import *
import numpy as np

class Picture:
    def __init__(self, filename = None):
        self.im = Image.open(filename)
        self.width = 0
        self.height = 0
        self.BWvector = 0
        self.matrix = 0

    def crop(self, coordcheque):
        self.im = self.im.crop(coordcheque)
        self.width = self.im.size[0]
        self.height = self.im.size[1]
        self.BWvector = self.intoBWVector()
        self.matrix = vecIntoMatrix(self.BWvector,[self.width, self.height])

    def intoBWVector(self):
        gray = self.im.convert('L')
        BW = list(np.asarray(gray.getdata(), dtype=np.int))
        boundary = (1.2*max(BW) + 0.8*min(BW)) // 2
        return [(0 if BW[i]>boundary else 1) for i in range(self.width*self.height)]
