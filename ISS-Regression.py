import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

coordinates = []
lin_reg_list = []
filename = 'dane13.txt'
intercept = 0
slope = 0
r_value =0
cx =[]
cy = []
ry = []


def read_file():
    with open(filename) as f:
        for line in f:
            coordinates.append(map(float, line.split()))


def linear_regression():
    global ry
    global  cx
    global r_value
    slope, intercept, r_value, p_value, std_err = stats.linregress(coordinates)
    for line in coordinates:
        lin_reg_list.append([line[0], intercept + slope * line[0]])
    cx, cy = separate_intoXY(coordinates)
    rx, ry = separate_intoXY(lin_reg_list)
    plt.scatter(cx, cy)
    plt.plot(rx, ry, 'r-')
    plt.show()


def separate_intoXY(coord):
    x =[]
    y = []
    for line in coord:
        x.append(line[0])
        y.append(line[1])
    return x, y


read_file()
linear_regression()




















