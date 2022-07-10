def increment_by_five_1(a):
    a = a + 5

def increment_by_five_2(a):
    return b + 5

def increment_by_five_3(a):
    return a + 5

def increment_by_five_4(b):
    a = 5
    return a + b

def increment_by_five_5(c):
    value = c
    return increment_by_five_3(value)

def main1():
    x = 9
    increment_by_five_1(x)
    print(x)

def main2():
    b = 9
    y = increment_by_five_2(b)
    print(y)

def main3():
    x = 9
    y = increment_by_five_3(x)
    print(y)

def main4():
    b = 9
    c = increment_by_five_4(b)
    print(c)

main1()
main4()