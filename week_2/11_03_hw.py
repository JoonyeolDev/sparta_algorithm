numbers = [1, 1, 1, 1, 1]
target_number = 3
count = 0

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    arr =[]
    idx = 0
    count = 0
    # while문이 돌면 idx가 1씩 추가됨
    while idx < len(array):

        # idx가 0이면 최초의 수 넣어주고
        if idx == 0:
            arr.append(array[idx])
            arr.append(-array[idx])

        # idx가 len(array)-1 이면 target과 비교 후 같으면 count+1
        elif idx == len(array)-1 :
            for i in arr:
                if i+array[idx] == target or i-array[idx] == target:
                    count+=1
        # 1<idx<len(array)-2 이면 arr 플마 array[idx] 해주고

        else:
            for i in arr[:]:
                arr.append(i+array[idx])
                arr.append(i-array[idx])
            # array[idx] 값 추가 해주기 이전 arr값 정리
            arr = arr[2**idx:]
        idx+=1
    return count


def get_count(array, target, list_sum=0, idx=0):
    if idx == len(array):
        if list_sum == target:
            global count
            count +=1
        return
    get_count(array, target, list_sum + numbers[idx], idx + 1)
    get_count(array, target, list_sum - numbers[idx], idx + 1)

# get_count(numbers, target_number)
print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers,target_number))  # 5를 반환 해야 합니다!
