input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    sum = 0
    for i in string:
        sum += int(i)
    if sum/len(string)>=0.5: return len(string)-sum
    return sum


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)