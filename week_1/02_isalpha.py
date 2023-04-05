def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for i in string:
        if i.isalpha() :
            idx = ord(i)-ord('a')
            alphabet_occurrence_array[idx]+=1
    # 이 부분을 채워보세요!

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))