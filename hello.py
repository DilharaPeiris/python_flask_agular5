import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import sys 

path_to_file="F:\KDU\KDU\FYP\Dataset\OBDII.csv"
df=pd.read_csv(path_to_file, encoding='utf-8')

df.columns

d=df.iloc[:, [4,17]].values

print %df



# print("Output from Python") 
# print("First name: " + sys.argv[1]) 
# print("Last name: " + sys.argv[2]) 