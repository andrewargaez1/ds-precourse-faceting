import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

cars_data = pd.read_csv('/home/aa1/Desktop/ds-precourse-faceting/data/cars.csv', sep='|')
cars_data.rename(columns={'Unnamed: 0': 'make_model'}, inplace=True)
cars_data.head()

cyl4 =  cars_data[cars_data['cyl']==4]
cyl6 =  cars_data[cars_data['cyl']==6]
cyl8 =  cars_data[cars_data['cyl']==8]
cyl4_hp = (np.array(cyl4['hp']))
cyl4_q = (np.array(cyl4['qsec']))
cyl6_hp = (np.array(cyl6['hp']))
cyl6_q = (np.array(cyl6['qsec']))
cyl8_hp = (np.array(cyl8['hp']))
cyl8_q = (np.array(cyl8['qsec']))

plt.subplot(3, 1, 1)
plt.scatter(cyl4_hp, cyl4_q, marker = '.')
plt.title("4 Cylinder")
plt.xlabel("Horse Power")
plt.ylabel("Quarter Mile Time")
plt.ylim([min(cars_data['qsec']-5),max(cars_data['qsec'])+1])
plt.xlim([min(cyl4_hp),max(cyl8_hp)])



plt.subplot(3, 1, 2)
plt.scatter(cyl6_hp, cyl6_q, marker = '.')
plt.title("6 Cylinder")
plt.xlabel("Horse Power")
plt.ylabel("Quarter Mile Time")
plt.ylim([min(cars_data['qsec']-5),max(cars_data['qsec'])+1])
plt.xlim([min(cyl4_hp),max(cyl8_hp)])



plt.subplot(3, 1, 3)
plt.scatter(cyl8_hp, cyl8_q, marker = '.')
plt.title("8 Cylinder")
plt.xlabel("Horse Power")
plt.ylabel("Quarter Mile Time")
plt.ylim([min(cars_data['qsec']-5),max(cars_data['qsec'])+1])
plt.xlim([min(cyl4_hp),max(cyl8_hp)])

plt.tight_layout()
plt.show()
