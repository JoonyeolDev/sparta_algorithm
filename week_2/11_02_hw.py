menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
orders = ["오뎅", "콜라", "사이다"]

def find_menus(menus,orders):
    menus.sort()
    orders.sort()
    for i in orders:
        check_menus = menus
        while check_menus:
            idx = len(check_menus)//2
            if i > check_menus[idx]:
                check_menus = check_menus[idx+1:]
            elif i < check_menus[idx]:
                check_menus = check_menus[:idx]
            else: break
            if check_menus ==[]: return False
    return True

print(find_menus(menus,orders))