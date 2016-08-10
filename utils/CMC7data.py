class CMC7data:
    def __init__(self, filename, sep, inpsize, outsize):
        self.datafile = open(filename, "r")
        self.nbData = int(self.datafile.readline())
        self.InputVector = []
        self.ExpecVector = []
        for _ in range(self.nbData):
            temp = list(map(float,self.datafile.readline().replace(",",".").split(sep)))
            self.InputVector.append(temp[:inpsize])
            self.ExpecVector.append(temp[inpsize:])
