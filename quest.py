"""
Program by Steve Trostle
"""


u = input("\nEnter primary character: ")
v = input("\nEnter secondary character: ")

for row in range(10):
    for col in range(10):
        if ((col == 0 or col == 9) and (row == 0 or row == 9)) \
        or ((col in range(3,7) and row == 1)) \
        or ((col in range(2,8) and row == 2)) \
        or ((col in range(2,4) or col in range(6,8)) and row == 3) \
        or ((col in range(6,8) and row == 4)) \
        or ((col in range(4,7) and row == 5)) \
        or ((col in range(4,6) and row == 6)) \
        or ((col in range(4,6) and row == 8)):
                print(u+u, end="")
        else:
            print(end=v+v)
    print("\r")
