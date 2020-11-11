from numpy import genfromtxt, isnan
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import math


def closest(lst, K): 
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]


fig1, ax1 = plt.subplots()
bar_dist = plt.axes([0.15, 0.05, 0.65, 0.03])
# bar_bridge1 = plt.axes([0.15, 0.05, 0.65, 0.03])
# bar_bridge2 = plt.axes([0.15, 0.10, 0.65, 0.03])
feature_plot = [0,1,0,1]
slider_dist = Slider(bar_dist, 'size', 2, 16)
# slider_bridge1 = Slider(bar_bridge1, 'Bridge1', 1.0, 7.0)
# slider_bridge2 = Slider(bar_bridge2, 'Bridge2', 1.0, 7.0)


def plot_data_with_size(size):
    all_data = []
    for file in os.listdir("/Users/ruoxili/Documents/NRL/rl-starter-files/storage"):
        if file.startswith('exp2_{}_{}_{}'.format(1,0,size)):
            data = np.array(genfromtxt('storage/{}/log.csv'.format(file), delimiter=','))
            data = [[d[1],d[4]] for d in data if not isnan(d[0])]
            # print(data)
            all_data.append(data)
    rreturn_means = []
    num = 100
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

def update(val):
    size = closest(list(range(2,17)), val)
    plot_data_with_size(size)

plot_data_with_size(2)
slider_dist.on_changed(update)
# slider_bridge1.on_changed(update_bridge2)
# slider_bridge2.on_changed(update_bridge1)
plt.show()
