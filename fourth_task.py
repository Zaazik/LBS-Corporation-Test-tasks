from operator import itemgetter
from random import randint

from third_task import get_sand_watch, print_result


def start():
    row_list = list()
    choice = input("Hi, do you want to manually write or random?(Default random)")
    for row in range(6):
        line_list = list()
        for line in range(6):
            if choice in ['m', 'manually']:
                i = input('Enter %s digit of %s lines' % (line + 1, row + 1))
            else:
                i = randint(-9, 9)
            line_list.append(i)
        row_list.append(line_list)
    result_list = get_sand_watch(row_list)
    choice = input("Show send watch ?(y(default)/n)")
    if choice is not 'n':
        print_result(result_list)
    return result_list


def get_sum_sand_watch(result_list):
    watch_sum_list = list()
    for i in result_list:
        for watch in i.values():
            watch_sum = 0
            del watch[1][0]
            del watch[1][-1]
            for val in watch:
                watch_sum += sum(val)
            watch_sum_list.append((watch_sum, watch))
    return watch_sum_list

if __name__ == "__main__":
    result_list = start()
    result_sum_list = get_sum_sand_watch(result_list)
    best_watch = max(result_sum_list, key=itemgetter(0))

    print('Best sum : [%s] in watch' % best_watch[0])
    for i in best_watch[1]:
        print(*i)
