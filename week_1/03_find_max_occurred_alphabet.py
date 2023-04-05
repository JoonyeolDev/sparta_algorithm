input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    for i in string:
        if i.isalpha() :
            idx = ord(i)-ord('a')
            alphabet_occurrence_array[idx]+=1
    max_occurred_alphabet = 0
    max_occurred_index = 0
    for idx,value in enumerate(alphabet_occurrence_array):
        if value> max_occurred_alphabet :
            max_occurred_alphabet = value
            max_occurred_index = idx
    answer = chr(97+max_occurred_index)
    return answer


result = find_max_occurred_alphabet(input)
print(result)