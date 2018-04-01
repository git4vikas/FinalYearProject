import pandas as pd, json, matplotlib.pyplot as plt

with open('RawData.json') as data_file:
    data = json.load(data_file)
df = pd.DataFrame(data['data'], columns=['N', 'P', 'K'])

print(data['data'][0]['N'],len(data['data']))
for i in range(len(data['data'])):
    if int(data['data'][i]['N']) < 456 or int(data['data'][i]['P']) < 20 or int(data['data'][i]['K']) < 470:
        print(data['data'][i]['date'],data['data'][i]['N'],data['data'][i]['P'],data['data'][i]['K'], "ORGANIC")
    else:
        print(data['data'][i]['date'],data['data'][i]['N'],data['data'][i]['P'],data['data'][i]['K'], "INORGANIC")
df.plot()
plt.show()
