from pprint import pprint
from collections import defaultdict

input_array = [
    [1, 1, 1, 0, 0, 0, ],
    [0, 1, 0, 0, 0, 0, ],
    [1, 1, 1, 0, 0, 0, ],
    [0, 0, 2, 4, 4, 0, ],
    [0, 0, 0, 2, 0, 0, ],
    [0, 0, 1, 2, 4, 0, ],
]


def get_sand_watch(input):
    print("Input data")
    pprint(input)
    result_list = list()
    temp_dict = defaultdict(list)
    for row_index in range(len(input)-2):
        a = input[row_index:row_index + 3]
        count = 0
        for column in a:
            divider = 0
            count += 1
            for column_index in range(len(column)-2):
                divider += 1
                temp_dict[divider].append(column[column_index:column_index + 3])
            if count == 3:
                result_list.append(temp_dict)
                temp_dict = defaultdict(list)
                count = 0
    return result_list


def print_result(input):
    count = 0
    for row_index in input:
        for watchs in row_index.values():
            for watch in watchs:
                print(watch)
            count += 1
            print("####### %s" % count)

if __name__ == "__main__":
    result_list = get_sand_watch(input_array)
    print_result(result_list)

