import random

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def getLabel():
    letters = "".join(random.choices(alphabet, k=3))
    numbers = str(random.randint(1000, 9999))
    Label = letters + numbers

    return Label

def getRandomData():
    data = []
    for i in range(9):
        data.append(random.randint(1, 200))
    return data
