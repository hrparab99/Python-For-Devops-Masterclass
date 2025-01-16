def check_highest(a, b, c):
    if a >= b and a >= c:
        if a == b == c:
            print("All are equal")
        else:
            print("A is the Highest Value")
    elif b >= a and b >= c:
        print("B is the Highest Value")
    elif c >= a and c >= b:
        print("C is the Highest Value")

a = 20
b = 30
c = 10

check_highest(a,b,c)