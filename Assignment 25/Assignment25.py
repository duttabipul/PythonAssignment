
# Assignment: 25        Date: 05.06.2022
# [Bottom-To-Top] Sum series using recursion.

def Buttom_to_Top_Recursion(num):
    num -= 1
    if num > 0:
        Buttom_to_Top_Recursion(num)
    print(num)

Buttom_to_Top_Recursion(10)


# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9