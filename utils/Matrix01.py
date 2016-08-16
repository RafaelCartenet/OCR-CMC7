from utils.Matrix import *
from utils.parameters import *

class Matrix01:
    def __init__(self, matrix):
        self.m = matrix
        self.height = len(self.m)
        self.width = len(self.m[0])

    def setMatrix(self, matrix):
        self.m = matrix
        self.height = len(self.m)
        self.width = len(self.m[0])

    # returns the first column from left which is not full of zeros
    def first1column(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.m[j][i] == 1:
                    return i

    # removes all the columns from the left which are full of zeros
    def cutleft(self):
        leftbound = self.first1column()
        self.setMatrix([[self.m[j][i] for i in range(leftbound, self.width)] for j in range(self.height)])

    # removes all the lines below the matrix which are full of zeros
    def removeBottom(self):
        for j in range(self.height-1,-1,-1):
            if max(self.m[j]) == 0:
                del self.m[j]
            else:
                self.height = j
                break

    # extract the most left digit of a 01Matrix, first cut the left columns of
    # the 01Matrix according to the most left column full of zero, then crop the
    # columns containing the digit, then removes the bottom and the top,
    # according to digit's height.
    def extractDig(self):
        self.cutleft()
        matdig = Matrix01([[self.m[j][i] for i in range(digitW)] for j in range(self.height)])
        matdig.removeBottom()
        matdig.setMatrix([[matdig.m[j][i] for i in range(digitW)] for j in range(matdig.height - digitH, matdig.height)])
        self.setMatrix([[self.m[j][i] for i in range(digitW+1, self.width)] for j in range(self.height)])
        return matdig

    # return a list containing all the digits (01 matrix)
    def extractDigits(self):
        return [self.extractDig() for _ in range(nbDigits)]
