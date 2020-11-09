from numpy import genfromtxt, isnan
import os
import numpy as np
import matplotlib.pyplot as plt

def get_all_data(feature):
    all_data = []
    for file in os.listdir("/Users/ruoxili/Documents/NRL/rl-starter-files/storage"):
        if file.startswith('{}_{}_{}_{}'.format(feature[0], feature[1], feature[2], feature[3])):
            data = np.array(genfromtxt('storage/{}/log.csv'.format(file), delimiter=','))
            data = [[d[1],d[4]] for d in data if not isnan(d[0])]
            # print(data)
            all_data.append(data)
    return all_data

all_data = get_all_data([1,3,1,1])
print(len(max(all_data, key=len)))
rreturn_means = []
num = 75
for i in range(num):
    rreturn_mean = []
    for data in all_data:
        if i < len(data):
            rreturn_mean.append(data[i][1])
    rreturn_means.append(rreturn_mean)
fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.boxplot(rreturn_means)
plt.show()