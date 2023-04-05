input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    num = 0
    for i in input:
        if i > num: num = i
    return max


result = find_max_num(input)
print(result)
