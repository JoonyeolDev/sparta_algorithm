input = [0, 3, 5, 6, 1, 2, 4]

def find_max_plus_or_multiply(array):
    number = 0
    for i in array:
        if number*i > number+i : number*=i
        else: number+=i
    return number

result = find_max_plus_or_multiply(input)
print(result)