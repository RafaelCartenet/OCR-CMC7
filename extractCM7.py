from sklearn import svm
from sklearn.externals import joblib
from utils.CMC7 import *
from utils.parameters import *
import warnings
import sys
import time
warnings.filterwarnings("ignore", category=DeprecationWarning)

# translates numerical digits into symbols if needed (represented by letters)
def translatedigit(digit):
    if digit == 10: digit = "a"
    elif digit == 11: digit = "b"
    elif digit == 12: digit = "c"
    else: digit = int(digit)
    return digit

# from a jpeg scan as input, prints the associated CMC7 code
def extractCMC7code(filename):
    res = ""
    brain = joblib.load('brain/brain.pkl')
    code = CMC7(filename)
    for i in range(nbDigits):
        digit = translatedigit(brain.predict(code.digitToVector(i))[0])
        res += str(digit)
        if i in gaps:
            res += " "
    print(res)

if __name__ == "__main__":
    a = time.time()
    extractCMC7code(sys.argv[1])
    print(round(time.time()-a,2), "sec")
