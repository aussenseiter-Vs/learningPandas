import pandas as pd 
import random

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def getLabel():
    letters = "".join(random.choices(alphabet, k=3))
    numbers = str(random.randint(1000, 9999))
    Label = letters + numbers

    return Label

def getRandomData(size=9, low=1, high=200):
    data = []
    for i in range(size):
        data.append(random.randint(low, high))
    return data

def getSeriesData(size=9):
    # Return label -> value pairs that can be plugged straight into pandas
    return {getLabel(): value for value in getRandomData(size)}

# Plug-in dictionary: {"ABC1234": 42, ...}
data = getSeriesData()

def main():
    print(data)

    series = pd.Series(data)
    print(series[series >= 150])

main()