import pandas as pd, json, matplotlib.pyplot as plt

with open('data1.json') as data_file:
    data = json.load(data_file)
df = pd.DataFrame(data['data'], columns=['Nitrogen', 'Phosphorus', 'Potassium'])

print(data['data'][0]['Nitrogen'], len(data['data']))
for i in range(len(data['data'])):
    if int(data['data'][i]['Nitrogen']) < 456 and int(data['data'][i]['Phosphorus']) <25 and  int(data['data'][i]['Potassium']) < 470:
        print(data['data'][i]['date'], data['data'][i]['Nitrogen'], data['data'][i]['Phosphorus'], data['data'][i]['Potassium'], "ORGANIC")
    else:
        print(data['data'][i]['date'], data['data'][i]['Nitrogen'], data['data'][i]['Phosphorus'], data['data'][i]['Potassium'], "INORGANIC")
df.plot()
plt.show()
