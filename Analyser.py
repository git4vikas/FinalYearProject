import pandas as pd
import json
with open('RawData.json') as data_file:
    data = json.load(data_file)

print(data)

df = pd.DataFrame(data['data'],columns=['N','P','K'])
print (df)
import matplotlib.pyplot as plt

df.cumsum()
df.plot()
plt.show()