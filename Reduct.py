import numpy as np
import copy

dict_for_incon ={}
turf_counter = -1
support = 0
set_collector = []
rule_dict = {}
first_set = [1, 0, 2, 4]
second_set = [3, 1, 2, 1]
third_set = [3, 2, 1, 4]
fourth_set = [1, 0, 2, 4]
fifth_set = [1, 0, 2, 4]
sixth_set = [3, 1, 2, 1]
seventh_set = [4, 2, 1, 3]

set_collector.extend([first_set, second_set, third_set, fourth_set, fifth_set, sixth_set, seventh_set])
copy_of_collector = copy.deepcopy(set_collector)


def con_to_str(some_list):
    lel = ''.join(str(e) for e in some_list)
    return lel


def turf_method():
    method_copy_collector = copy.deepcopy(set_collector)
    global turf_counter
    turf_counter += 1
    if turf_counter < len(method_copy_collector[0]) - 1:  # cannot create a rule from less than 2 elements

        for list_copy in method_copy_collector:
            list_copy.pop(turf_counter)  # turfing columns one by one

        print(str(turf_counter) + ' attribute is dropped')
        f_method(method_copy_collector)
    else:
        print('finish')
        print(dict_for_incon)


def f_method(list_of_lists):
    print('f_method begin' + str(set_collector))
    global turf_counter
    rule_dict[turf_counter] = {}  # create dictionary of dictionaries with key - dropped
    dict_for_incon[turf_counter]={}
    for outer_list in list_of_lists:
        if con_to_str(outer_list) in rule_dict[turf_counter]:  # no need to count same element once more
            continue
        for inner_list in list_of_lists:
            if (np.logical_and(outer_list[:-1] == inner_list[:-1], outer_list[-1] != inner_list[
                -1])):  # check if there is no same set which with different d
                list_of_lists.remove(inner_list)  # remove from outer loop to do not make relational inconsistency
                (dict_for_incon[turf_counter])[con_to_str(outer_list)]=1
                (dict_for_incon[turf_counter])[con_to_str(inner_list)]=1
                del (rule_dict[turf_counter])[con_to_str(outer_list)]  # if yes then delete

            if outer_list == inner_list:  # check if there is such a set with same d
                print(str(outer_list) + '        ' + str(inner_list))
                if (con_to_str(outer_list) in rule_dict[
                    turf_counter]):  # check if in resulting dictionary there is such a element
                    (rule_dict[turf_counter])[con_to_str(outer_list)] += 1  # if true then increment support
                else:
                    (rule_dict[turf_counter])[con_to_str(outer_list)] = 1  # if not set support  equal 2

    print(turf_counter)
    print(rule_dict)
    turf_method()


f_method(copy_of_collector)
