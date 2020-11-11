from numpy import genfromtxt, isnan
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import math

dist_feature_map = {}
for d1 in [1]:
    for d2 in [1]:
        for i in range(1,8):
            for j in range(1,8):
                feature = [d1,i,d2,j]
                for file in os.listdir("/Users/ruoxili/Documents/NRL/rl-starter-files/storage"):
                    if file.startswith('{}_{}_{}_{}'.format(d1, i, d2, j)):
                        x = [d1, i]
                        y = [d2, j]
                        d = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
                        if d in dist_feature_map:
                            dist_feature_map[d].append([d1,i,d2,j])
                        else:
                            dist_feature_map[d] = [[d1,i,d2,j]]
                        break

print(dist_feature_map)

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
# bar_dist = plt.axes([0.15, 0.05, 0.65, 0.03])
# bar_bridge1 = plt.axes([0.15, 0.05, 0.65, 0.03])
# bar_bridge2 = plt.axes([0.15, 0.10, 0.65, 0.03])
feature_plot = [0,1,0,1]
# slider_dist = Slider(bar_dist, 'Distance', 0, 6.0)
# slider_bridge1 = Slider(bar_bridge1, 'Bridge1', 1.0, 7.0)
# slider_bridge2 = Slider(bar_bridge2, 'Bridge2', 1.0, 7.0)

def plot_data_with_same_dist_same_orientation(dist):
    feature_list = dist_feature_map[dist]
    print(feature_list)
    all_data = []
    for feature in feature_list:
        all_data += get_all_data(feature)
    rreturn_means = []
    num = 75
    for i in range(num):
        rreturn_mean = []
        for data in all_data:
            if i < len(data):
                rreturn_mean.append(data[i][1])
        rreturn_means.append(rreturn_mean)
    ax1.cla()
    ax1.set_title('Dist = {}'.format(dist))
    ax1.set_xlabel('Number of frames X 2048')
    ax1.set_ylabel('Mean rreturn_mean')
    ax1.boxplot(rreturn_means)
    fig1.savefig('{}_dist_{}.png'.format(feature_list[0][0],dist))

def plot_data_with_same_dist(dist):
    feature_list = dist_feature_map[dist]
    print(feature_list)
    all_data = []
    for feature in feature_list:
        all_data += get_all_data(feature)
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

def plot_data(feature):
    all_data = get_all_data(feature) + get_all_data([feature[2],feature[3],feature[0],feature[1]])
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

def update(val):
    dist = closest(list(dist_feature_map.keys()), val)
    plot_data_with_same_dist_same_orientation(dist)

def update_bridge1(val):
    loc = closest([1,2,3,4,5,6,7], val)
    feature_plot[1] = loc
    plot_data(feature_plot)

def update_bridge2(val):
    loc = closest([1,2,3,4,5,6,7], val)
    feature_plot[3] = loc
    plot_data(feature_plot)

# plot_data(feature_plot)
# slider_dist.on_changed(update)
# slider_bridge1.on_changed(update_bridge2)
# slider_bridge2.on_changed(update_bridge1)
# plt.show()

for i in range(7):
    plot_data_with_same_dist_same_orientation(i)