# OCR-CMC7
Python Optical Character Recognition of CMC7 codes on Bank Checks using SVM machine learning from Scikit-learn library

Libraries used :
- sklearn
- numpy
- PIL

From a jpeg A4 scan of a bank check, extract the CMC7 code according to its defined position on the A4 scan.

## toDataFile.py
Generate Labeled Data according to bank checks that you put in the trainingfiles sub directory.  
Filenames must follow the name defined in parameters.py  
Each digit is represented as a digitW*digitH vector, filed with 0 and 1, depending if the pixel is closer to black or white.  
Use :  
  `python toDataFile.py`
  
## CMC7training.py
Using the previously created Labeled Data, learn using SVM how to classify the different digits.  
Train using trainProportion percent of the labeled datas, and the remaining ones to test the accuracy of the model.  
Use :  
  `python CMC7training.py`

## extractCMC7.py
Extract the CMC7 code from a jpeg scan, using the previously trained SVM model.  
Use :  
  `python extractCMC7.py filename.jpeg`
  
### Settings
Check parameters.py  

