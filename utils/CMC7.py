from utils.Picture import *
from utils.Matrix01 import *
import psutil
from utils.parameters import *

class CMC7:
    def __init__(self, scanJPGA4file):
        self.scan = Picture(scanJPGA4file)
        self.scan.crop(coordcheque)
        self.CMC7_01 = Matrix01(self.scan.matrix) # 0.04
        self.digits = self.CMC7_01.extractDigits() # 0.12

    # returns a Vector containing all the pixel of the ith digit
    def digitToVector(self, i):
        return matToVector(self.digits[i].m)

    # opens the scan, waits for a correct input which needs to be the CMC7 code
    def toTrainingString(self):
        self.scan.im.show()
        res = ""
        code = input().replace(" ", "")
        while len(code)!= nbDigits:
            print("incorrect")
            code = input().replace(" ", "")
        for proc in psutil.process_iter():
            if proc.name() == "dllhost.exe":
                proc.kill()
        for i in range(nbDigits):
            res += vecToString(matToVector(self.digits[i].m)) +digcode[code[i]] + "\n"
        return res
