import pandas as pd 
import random
from getData import getRandomData, getLabel

dataList = getRandomData()
IndexList = [getLabel() for _ in range(9) ]

series = pd.Series(dataList, index=IndexList)

print(series)