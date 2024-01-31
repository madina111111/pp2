a = 55
b = 55
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("b is greater than a")

a = 2
b = 200
print("A") if a > b else print("B")

a = 200
b = 200
print("A") if a > b else print("=") if a == b else print("B")

a = 300
b = 2
c = 55
if a > b and c > b:
    print("Both conditions are True")

a = 300
b = 40
c = 55
if a > b or b > c:
    print("At least one conditions are True")

a = 20 
b = 200
if not a > b:
    print("a is NOT greater than b")

x = 15
if x > 10:
    print("is greater than 10")
    if x > 20:
        print("also above 20")
    else:
        print("but not above 20")

a = 33
b = 200
if b > a:
    pass

