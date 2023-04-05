input = "abadabac"

def find_not_repeating_character(string):
    arr=[]
    for i in string:
        count = 0
        for j in string:
            if i==j: count+=1
        if count == 1 : arr.append(i)
    if arr==[] : return "_"
    return arr[0]


result = find_not_repeating_character(input)
print(result)