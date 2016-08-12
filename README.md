# OCR-CMC7
## Rafael CARTENET
Python Optical Character Recognition of CMC7 codes on Bank Checks using SVM machine learning from Scikit-learn library

## Libraries used :
- sklearn
- numpy
- PIL

## Purpose
From a jpeg A4 scan containing a bank check, extract the CMC7 code. The goal was to computerize the extraction of the code CMC7 of a bank check which is used for validity. (mainly used in Europe only)  
More about CMC7 : https://en.wikipedia.org/wiki/Magnetic_ink_character_recognition

## Method
### Modelling Data
I started with 60 models of bank checks with the same format, same bank. The goal was to, from a new given bank check scan, extract the CMC7 code.  
I first found out the box where the CMC7 code is situated, and chose the coordinates of the top left corner and the bottom right one. On the 60 bank checks, the CMC7 is inside that box, with white background and black digits/symbols.  
  
Once i did that i transformed the cropped picture (according to the box) into a 0 1 Matrix according to the gray scale :  
For each box i computed the lighter pixel and the darker pixel, this way i could cancel the contrast effect, that can be different from a bank check to an other.  
I defined D the half value between the darker pixel and the lower pixel, which would then be my decision value. If a pixel is lower than D, then the pixel would become 0, if it's above, 1.  
  
Once it's done i got a matrix of 0 and 1 where the 1 represents the black and the 0 represents white. This way it's much easier to manage the digits.  

### Extract the digits
On the bank checks i used, there were 35 digits, but it's just a parameter. Analysing the different 01 Matrix i got, i found out that the hight and the width of the digits are always the same, because of course it's the same font.  
I made two functions that allowed me to detect my digits :
- cutleft (deletes the left columns full of zero of a given 01 Matrix)
- removebottom (deletes the bottom lines full of zero of a given 01 Matrix)
  
I cutleft my 01Matrix so i know that after that, the first column is the beginning of the first digit. Then, i know how wide is a digit so i just cut a new 01Matrix with the columns containing the first digit and only this digit from the "mother" 01 Matrix. I then removebottom this Matrix, which allows me to make sure that the digit is always aligned with the bottom left corner. As i know the height of a digit, i simply deleted the lines above that won't be useful.  
Once i did that i extracted the first 01Matrix, corresponding to the first digit matrix and cropped the "mother" 01 Matrix. Then i just repeated this process as many times as the number of digits !  
Once you extracted a the digit, you can simply convert it in a list of 0 and 1 (of length digitH x digitW). This is gonna be your input later for the machine learning. Which means that each bank check is gonna give you as many vectors as number of digits on your CMC7 code.

### Creation of Labeled data
Once i was able to extract nbDigits vectors representing my digits, i created Labeled Data, which means the classification of each vector. I created a TrainingFile.txt according to this format :
`0 1 0 1 ..... 0 1 0 0 1 X`
`1 1 0 0 ..... 1 1 1 0 0 Y`
`0 1 0 1 ..... 0 1 1 1 1 Z`





## Files
### toDataFile.py
Generate Labeled Data according to bank checks that you put in the trainingfiles sub directory.  
Filenames must follow the name defined in parameters.py  
Each digit is represented as a digitW*digitH vector, filed with 0 and 1, depending if the pixel is closer to black or white.  
Use :  
  `python toDataFile.py`

### CMC7training.py
Using the previously created Labeled Data, learn using SVM how to classify the different digits.  
Train using trainProportion percent of the labeled datas, and the remaining ones to test the accuracy of the model.  
Use :  
  `python CMC7training.py`

### extractCMC7.py
Extract the CMC7 code from a jpeg scan, using the previously trained SVM model.  
Use :  
  `python extractCMC7.py filename.jpeg`

### Settings
Check parameters.py  
