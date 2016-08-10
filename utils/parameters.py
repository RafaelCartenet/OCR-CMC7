# Parameters

# ------- Training -------- #
nbTrfiles = 59 # Nb of Samples of Bank Checks
fname = "trainingfiles/tr" # Files Names : trX.jpeg
ext = ".jpeg" # extension
trainProportion = 0.70

# ----- Checks Format ----- #
digitW = 11 # Width in pixel of one digit
digitH = 15 # Height in pixel of one digit
nbDigits = 35 # Number of Digits/Symbols in one code(symboles inclus)
coordcheque = (145, 1118, 675, 1155) # Coordonnates of the zone including the CMC7 code
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
"c":"12"} # bank checks codification (10, 11, 12 : symbols)
gaps = [7, 21] # Spaces position in the code.
