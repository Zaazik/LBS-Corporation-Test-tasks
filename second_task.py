from collections import defaultdict

input_data = ["икс", "зэт", "альфа", "варо", "икс", "икс", ]
check_data = ["икс", "зэт", "вап"]


def count_data(input, check):
    count_dict = defaultdict(int)
    for each in input:
        count_dict[each] += 1
    for each in check:
        print('"%s : %s"' % (each, count_dict[each]))

count_data(input=input_data, check=check_data)
