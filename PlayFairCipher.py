# Create 5x5 Matrix
def createMatrix():
    return [["" for x in range(5)] for x in range(5)]


import math as maths

# def insertintomatrix(val):


# Find is the Value is Even or Odd
# If value is even return true
def iseven(val):
    return val % 2 == 0


# Make Pair in two of String
# Add "x" is character has no pair


def makePair(str):
    paired_str = []

    if len(str) % 2 != 0:
        str += "x"

    for i in range(0, len(str), 2):
        paired_str.append(str[i : i + 2])
    return paired_str


# Find char in string return True if Found
def findchar(str, char):
    for i in str:
        if char.lower() == i.lower():
            return True
    return False


# Remove Recursive Character from the String
def removeMultiocc(str):
    str = str.lower()

    newstr = ""
    for char in str:
        if not findchar(newstr, char):
            newstr = newstr + char
    return newstr


# Add "X" to the first letter of pair having same Character
def AddXtoSamePair(str):
    newstr = str
    for i in str:
        newstr = newstr.replace("{}{}".format(i, i), "{}x{}".format(i, i))
    return newstr


def SearchinMatrix(char, Matrix):
    for i in range(0, 5):
        for j in range(0, 5):
            if char == Matrix[i][j]:
                return [i, j]


#           0    1    2    3    4
#     0  [['p', 'u', 'b', 'l', 'i'],
#     1   ['c', 'o', 'k', 'a', 'd'],
#     2   ['e', 'f', 'g', 'h', 'm'],
#     3   ['n', 'q', 'r', 's', 't'],
#     4   ['v', 'w', 'x', 'y', 'z']]


def encryptusingvirtualbox(coords):
    Coords_of_First_char = coords[0]
    Coords_of_Second_char = coords[1]
    if Coords_of_First_char == Coords_of_Second_char:
        return coords
    if Coords_of_First_char[0] == Coords_of_Second_char[0]:
        return [
            [Coords_of_First_char[1] + 1, Coords_of_First_char[0]],
            [Coords_of_Second_char[1] + 1, Coords_of_Second_char[0]],
        ]
    if Coords_of_First_char[1] == Coords_of_Second_char[1]:
        return [
            [Coords_of_First_char[0] + 1, Coords_of_First_char[1]],[
                Coords_of_Second_char[0] + 1, Coords_of_Second_char[1]
            ]
        ]
    New_Coords_of_First_char = [Coords_of_First_char[0], Coords_of_Second_char[1]]
    New_Coords_of_Second_char = [Coords_of_Second_char[0], Coords_of_First_char[1]]
    return [New_Coords_of_First_char, New_Coords_of_Second_char]


# Choose the Alphabet Array base on Character Included in key
def iorj(str):
    if findchar(str, "i"):
        return [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
    else:
        return [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]


# Encrypt the Original Text
def encrypt(val, key):
    if ConstraintAlpha(val,key):
        return "Value and key only can be Alphabet"
    
    if findchar(key, "i") and findchar(key, "j"):
        return "Key can't Consist `I` and `J` together"
    smallalpha = iorj(key)

    matrix = createMatrix()
    pairedval = AddXtoSamePair(val.replace(" ", ""))
    pairedval = makePair(pairedval)
    key = key.replace(" ", "")
    key = removeMultiocc(key)

    index_i = 0
    index_j = 0

    for i in key:
        matrix[index_i][index_j] = i.lower()

        index_j = index_j + 1
        if index_j == 5:
            index_i = index_i + 1
            index_j = 0
    for i in smallalpha:
        if not findchar(key, i):
            matrix[index_i][index_j] = i.lower()
            index_j = index_j + 1
            if index_j == 5:
                index_i = index_i + 1
                index_j = 0
    NewValue = ""
    for pair in pairedval:
        # print(pair[0].lower(), pair[1].lower())
        Coords_of_First_char = SearchinMatrix(pair[0].lower(), matrix)
        Coords_of_Second_char = SearchinMatrix(pair[1].lower(), matrix)
        [NewCoordsofFirstChar, NewCoordsofSecondCoords] = encryptusingvirtualbox(
            [Coords_of_First_char, Coords_of_Second_char]
        )
        # print(NewCoordsofFirstChar, NewCoordsofSecondCoords, "exlaso")
        NewFirstValue = matrix[NewCoordsofFirstChar[0]][NewCoordsofFirstChar[1]]
        NewSecondValue = matrix[NewCoordsofSecondCoords[0]][NewCoordsofSecondCoords[1]]
        NewValue = NewValue + "{}{}".format(NewFirstValue, NewSecondValue)

    return NewValue.upper()


def ConstraintAlpha(key,val): 
    return not (key.isalpha() and val.isalpha())


def decryptusingvirtualbox(coords):
    Coords_of_First_char = coords[0]
    Coords_of_Second_char = coords[1]
    if Coords_of_First_char == Coords_of_Second_char:
        return coords
    if Coords_of_First_char[0] == Coords_of_Second_char[0]:
        return [
            [Coords_of_First_char[1] - 1, Coords_of_First_char[0]],
            [Coords_of_Second_char[1] - 1, Coords_of_Second_char[0]],
        ]
    if Coords_of_First_char[1] == Coords_of_Second_char[1]:
        return [
            [Coords_of_First_char[0] - 1, Coords_of_First_char[1]],[
                Coords_of_Second_char[0] - 1, Coords_of_Second_char[1]
            ]
        ]

    New_Coords_of_First_char = [Coords_of_First_char[0], Coords_of_Second_char[1]]
    New_Coords_of_Second_char = [Coords_of_Second_char[0], Coords_of_First_char[1]]
    return [New_Coords_of_First_char, New_Coords_of_Second_char]


#           0    1    2    3    4
#     0  [['p', 'u', 'b', 'l', 'i'],
#     1   ['c', 'o', 'k', 'a', 'd'],
#     2   ['e', 'f', 'g', 'h', 'm'],
#     3   ['n', 'q', 'r', 's', 't'],
#     4   ['v', 'w', 'x', 'y', 'z']]
def decrypt(val, key):
    if ConstraintAlpha(val,key):
        return "Value and key only can be Alphabet"
    if findchar(key, "i") and findchar(key, "j"):
        return "Key can't Consist `I` and `J` together"
    smallalpha = iorj(key)

    matrix = createMatrix()
    pairedval = AddXtoSamePair(val.replace(" ", ""))
    pairedval = makePair(pairedval)
    key = key.replace(" ", "")
    key = removeMultiocc(key)

    index_i = 0
    index_j = 0

    for i in key:
        matrix[index_i][index_j] = i.lower()

        index_j = index_j + 1
        if index_j == 5:
            index_i = index_i + 1
            index_j = 0
    for i in smallalpha:
        if not findchar(key, i):
            matrix[index_i][index_j] = i.lower()
            index_j = index_j + 1
            if index_j == 5:
                index_i = index_i + 1
                index_j = 0
    NewValue = ""
    for pair in pairedval:
        # print(pair[0].lower(), pair[1].lower())
        Coords_of_First_char = SearchinMatrix(pair[0].lower(), matrix)
        Coords_of_Second_char = SearchinMatrix(pair[1].lower(), matrix)
        [NewCoordsofFirstChar, NewCoordsofSecondCoords] = decryptusingvirtualbox(
            [Coords_of_First_char, Coords_of_Second_char]
        )
        # print(NewCoordsofFirstChar, NewCoordsofSecondCoords, "exlaso")
        NewFirstValue = matrix[NewCoordsofFirstChar[0]][NewCoordsofFirstChar[1]]
        NewSecondValue = matrix[NewCoordsofSecondCoords[0]][NewCoordsofSecondCoords[1]]
        NewValue = NewValue + "{}{}".format(NewFirstValue, NewSecondValue)
    return NewValue.upper()

key = "ok"
encval = encrypt("Exlaso", key)
print(encval) 
print(decrypt(encval,key))
# GVAHQA
