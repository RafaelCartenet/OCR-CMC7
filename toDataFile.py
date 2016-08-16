from utils.CMC7 import *
from utils.parameters import *

# ------------- Labeled Data Creation --------------- #
# Opens every jpeg file in the trainingfiles repository and asks the user to
# manually give the associated CMC7 code in order to create labeled data.
# 1 digit labeled data is represented as :
# 1 0 1 0 0 1 ....... 0 0 1 1 9 (if the digit is 9)
DataFile = open("trainingfiles/trainingData.txt", "w")
DataFile.write(str(nbDigits*nbTrfiles) + "\n")
for i in range(nbTrfiles):
    print(i + 1,"/",nbTrfiles)
    fi = fname + str(i + 1) + ext
    temp = CMC7(fi).toTrainingString()
    DataFile.write(temp)
DataFile.close()
