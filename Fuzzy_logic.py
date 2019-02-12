import numpy as np
import matplotlib.pyplot as plt
import copy

Hspeed = [[0, 20], [0, 40], [0, 60], [0.2, 80], [0.7, 100], [1, 120], [1, 140], 'high']
Mspeed = [[0, 20], [0.4, 40], [0.7, 60], [1, 80], [0.7, 100], [0.1, 120], [0, 140], 'medi']
Lspeed = [[1, 20], [1, 40], [0.6, 60], [0.2, 80], [0, 100], [0, 120], [0, 140], 'low']
Hfuel = [[0, 3], [0.1, 6], [0.7, 9], [1, 12], [1, 15], 'high']
Mfuel = [[0, 3], [0.5, 6], [1, 9], [0.3, 12], [0, 15], 'low']
Lfuel = [[1, 3], [1, 6], [0.4, 9], [0.1, 12], [0, 15], 'medi']
speed = [20, 40, 60, 80, 100, 120, 140]
fuel = [3, 6, 9, 12, 15]
speed_list = [Hspeed, Mspeed, Lspeed]
fuel_list = []
fuel_list.extend([Hfuel, Mfuel, Lfuel])
ignited_list = []
mondami_list = []
fuzzy_responce_list = []
y_list = []


def selectignited(input_speed):
    print('Inputed number : ' + str(input_speed))
    for splist in speed_list:  # select list with speed
        for somelist in splist:  # select his sublist
            if (np.logical_and(somelist[1] == input_speed,
                               somelist[0] != 0)):  # check if there is inputed value and if its bigger then 0
                newlist = splist[:]  # create new to do not change main list
                newlist.append(somelist[0])  # add its ignition level for inputed number
                ignited_list.append(newlist)  # put list to some kind of result of this method
    rule()


def rule():
    for list_speed in ignited_list:  # select results from prev method
        for fue_list in fuel_list:  # select fuel list_rule
            if (list_speed[-2] == fue_list[-1]):  # looking for rule which is linked by the last index string
                print(str(list_speed[:-1]) + "______and its rule______" + str(fue_list))
                print('Ignition level ' + str(list_speed[-1]))
                new_list_f_fuel = copy.deepcopy(fue_list)  # create to do not break initial arrays
                new_list_f_fuel.pop(-1)
                new_list_f_speed = copy.deepcopy(list_speed)  # -//-
                new_list_f_speed.pop(-2)  # del element which is used as a link
                mondami_list.append([new_list_f_speed, new_list_f_fuel])  # putting them into one shell in ne list_rule
    del ignited_list[:]  # clearing  ignited to do not confuse for next values
    mondami()


def mondami():
    for list_mond in mondami_list:  # list_mond with 1 rule(2lists inside)
        indicator = (list_mond[0])[-1]  # selecting ignition level of current list_mond
        for idx, val in enumerate(list_mond[1]):  # loop
            if ((list_mond[1])[idx])[
                0] > indicator:  # if current number(associated by rule) is higher than ignition level
                ((list_mond[1])[idx])[0] = indicator  # current = ignition
                print("mondami_method after compare      " + str(val))
        fuzzy_responce_list.append((list_mond[1])[:])
    print('Lists for max ' + str(fuzzy_responce_list))
    del mondami_list[:]
    fuzzyresponce()


# find max out of 2 arrays and put it into resulting array
def fuzzyresponce():
    resultinglist = [0, 0, 0, 0, 0]
    for list_for_fuz in fuzzy_responce_list:  # list_for_fuz with fuel after mondami
        for indx, val in enumerate(list_for_fuz):
            if ((list_for_fuz[indx])[0] > resultinglist[indx]):  # compare and select max
                resultinglist[indx] = (list_for_fuz[indx])[0]
    print('after fuzzy responce ' + (str(resultinglist)))
    del fuzzy_responce_list[:]
    calculate_y(resultinglist)


def calculate_y(final_calculation_list):
    sum = 0
    prod = 0
    for indx, val in enumerate(final_calculation_list):
        sum += val
        prod += final_calculation_list[indx] * fuel[indx]
    y = prod / sum
    print('result ' + str(y))
    y_list.append(y)


def draw_plot():
    plt.plot(speed, y_list, )
    plt.yticks([5, 6, 7, 8, 9, 10, 11, 12])
    plt.xlabel('Speed')
    plt.ylabel('Litters per 100 km')
    plt.title('Fuel consumption depending on speed')
    plt.show()


for number in speed:
    selectignited(number)

draw_plot()
