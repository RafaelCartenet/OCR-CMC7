from utils.CMC7 import *
from utils.parameters import *

# ------------- Labeled Data Creation --------------- #
DataFile = open("trainingfiles/trainingData.txt", "w")
DataFile.write(str(nbDigits*nbTrfiles) + "\n")
for i in range(nbTrfiles):
    print(i + 1,"/",nbTrfiles)
    fi = fname + str(i + 1) + ext
    temp = CMC7(fi).toTrainingString()
    DataFile.write(temp)
DataFile.close()
