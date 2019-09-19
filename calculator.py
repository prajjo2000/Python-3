print("welcome to the calculator")
print("enter ur choice according to your operation")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y 

def div(x,y):
    return x/y

num = int(input())

if num == 1:
    print("you have choosen addition")
    print("enter your first number")
    a = int(input())
    print("enter your second number")
    b = int(input())
    ans = add(a,b)
elif num == 2:
    print("you have choosen subtraction")
    print("enter your first number")
    a = int(input())
    print("enter your second number")
    b = int(input())
    ans = sub(a,b)
elif num == 3:
    print("you have choosen multiplication")
    print("enter your first number")
    a = int(input())
    print("enter your second number")
    b = int(input())
    ans = mul(a,b)
elif num == 4:
    print("you have choosen division")
    print("enter your first number")
    a = int(input())
    print("enter your second number")
    b = int(input())
    ans = div(a,b)

print("your anser is")
print(ans)

