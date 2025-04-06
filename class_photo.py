def validClassPhoto(red_shirts: list[int], blue_shirts:list[int]):
    red_shirts.sort(reverse=True)
    blue_shirts.sort(reverse=True)
    who_stands_behind = ""

    # Check Which is the back row
    if blue_shirts[0] > red_shirts[0]:
        who_stands_behind = blue_shirts
        who_stands_ahead = red_shirts
    elif red_shirts[0] > blue_shirts[0]: 
        who_stands_behind = red_shirts
        who_stands_ahead = blue_shirts
    else:
        return False

    print(f"Who stands behind : {who_stands_behind}")
    print(f"Who stands ahead : {who_stands_ahead}")

    # Check casewise if the order can be maintained
    count = 0
    for idx in range(0, len(blue_shirts)):
        if who_stands_behind[idx] > who_stands_ahead[idx]:
            print(f"{who_stands_behind[idx]}: {who_stands_ahead[idx]}")
            count += 1
            continue
        else: 
            return False

    if count == len(blue_shirts): 
        print(f"Successful photo !!!")
        return True

blue_shirts = [6,9,2,4,5]
red_shirts = [5,8,1,3,4]

validPhoto = validClassPhoto(red_shirts, blue_shirts)
print(f"Photo result: {validPhoto}\n")
