from utils.CMC7 import *
from sklearn import svm
from sklearn.externals import joblib
from utils.parameters import *
from utils.CMC7data import  *
import warnings
warnings.filterwarnings("ignore")

# -------------- Training SVM --------------------- #
# Import Data
data = CMC7data("trainingfiles/trainingData.txt", " ", digitW*digitH, 1)
nbData_Train = round(trainProportion*data.nbData)
nbData_Tests = data.nbData - nbData_Train
pourc_Train = round(nbData_Train / data.nbData, 2)
pourc_Tests = round(nbData_Tests / data.nbData, 2)

InpVECTOR = data.InputVector[:nbData_Train]
ExpVECTOR = data.ExpecVector[:nbData_Train]

# Initialisation
CLF = svm.SVC(gamma = 0.001, C = 100)

# Entrainement
CLF.fit(InpVECTOR, ExpVECTOR)

# -------------- Testing Model -------------------- #
InpVECTOR = data.InputVector[nbData_Train:]
ExpVECTOR = data.ExpecVector[nbData_Train:]
accu = 0
for i in range(nbData_Tests):
    prediction = CLF.predict(InpVECTOR[i])
    if prediction == ExpVECTOR[i]:
        accu += 1
accu = 100 * round(accu / nbData_Tests, 2)

print()
print("Rapport de test :")
print("----------------------------------------------")
print("Nombre de digits total : " + str(data.nbData) + " (" + str(data.nbData//nbDigits) + " chèques)")
print("Nombre de digits d'entrainement (" + str(100*pourc_Train) + "%) : " + str(nbData_Train))
print("Nombre de digits testées        (" + str(100*pourc_Tests) + "%) : " + str(nbData_Tests))
print()
print("Accuracy : " + str(accu) + "%")

# Export Brain
joblib.dump(CLF,'brain/brain.pkl')
