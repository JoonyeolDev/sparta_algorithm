finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def is_exist_target_number_binary(target, numbers):
    while numbers:
        avg_num = len(numbers) // 2
        if target > numbers[avg_num]:
            numbers = numbers[numbers[avg_num] + 1:]
        elif target < numbers[avg_num]:
            numbers = numbers[:numbers[avg_num]]
        else:
            return True
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
