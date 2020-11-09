from numpy import genfromtxt, isnan
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import math

dist_feature_map = {}
for d1 in [0,1]:
    for d2 in [0,1]:
        for i in range(1,8):
            for j in range(1,8):
                flag = False
                feature = [d1,i,d2,j]
                for file in os.listdir("/Users/ruoxili/Documents/NRL/rl-starter-files/storage"):
                    if file.startswith('{}_{}_{}_{}'.format(feature[0], feature[1], feature[2], feature[3])):
                        flag = True
                if flag:
                    x = [d1, i]
                    y = [d2, j]
                    d = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
                    dist_feature_map[d] = feature
print(dist_feature_map.keys())

def closest(lst, K): 
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def get_all_data(feature):
    all_data = []
    for file in os.listdir("/Users/ruoxili/Documents/NRL/rl-starter-files/storage"):
        if file.startswith('{}_{}_{}_{}'.format(feature[0], feature[1], feature[2], feature[3])):
            data = np.array(genfromtxt('storage/{}/log.csv'.format(file), delimiter=','))
            data = [[d[1],d[4]] for d in data if not isnan(d[0])]
            # print(data)
            all_data.append(data)
    return all_data

fig1, ax1 = plt.subplots()
bar_dist = plt.axes([0.15, 0.05, 0.65, 0.03])
slider_dist = Slider(bar_dist, 'Distance', 0, 10.0)

def plot_data(feature):
    all_data = get_all_data(feature)
    rreturn_means = []
    num = 75
    for i in range(num):
        rreturn_mean = []
        for data in all_data:
            if i < len(data):
                rreturn_mean.append(data[i][1])
        rreturn_means.append(rreturn_mean)
    ax1.cla()
    ax1.set_title('Dynamic Plot')
    ax1.set_xlabel('Number of frames X 2048')
    ax1.set_ylabel('Mean rreturn_mean')
    ax1.boxplot(rreturn_means)
    print(feature)


def update(val):
    # amp = samp.val
    # freq = sfreq.val
    # l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    # fig.canvas.draw_idle()
    # print(val)
    dist = closest(list(dist_feature_map.keys()), val)
    feature = dist_feature_map[dist]
    # update canvas
    plot_data(feature)

slider_dist.on_changed(update)

plt.show()