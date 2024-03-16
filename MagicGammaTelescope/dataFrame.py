import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

columns = ["fLength","fWidth","fSize","fConc","fConc1","fAsym","fM3Long","fM3Trans","fAlpha","fDist","class"]
df = pd.read_csv('magic04.data',names=columns)

#print(df)

#now let's change the class value g=1, h=0

df['class'] = (df['class'] == 'g').astype(int)

print(df['class'])

