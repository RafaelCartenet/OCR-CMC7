# Paramètres

# ----- Entrainement ------- #
nbTrfiles = 59 # Nombres de chèques modèles
fname = "trainingfiles/tr" # noms Fichiers : trX.jpeg
ext = ".jpeg" # extension
trainProportion = 0.70

# ----- Format Chèques ----- #
digitW = 11 # Width en pixel d'un digit de chèque
digitH = 15 # Height en pixel d'un digit de chèque
nbDigits = 35 # Nb de digits contenus dans un code (symboles inclus)
coordcheque = (145, 1118, 675, 1155) # Coordonnées de la zone ou chercher le CMC7
digcode = {
"0":"0",
"1":"1",
"2":"2",
"3":"3",
"4":"4",
"5":"5",
"6":"6",
"7":"7",
"8":"8",
"9":"9",
"a":"10",
"b":"11",
"c":"12"} # Codification des différents digits du chèque (10, 11, 12 : symboles)
gaps = [7, 21] # Position des espaces dans le code
