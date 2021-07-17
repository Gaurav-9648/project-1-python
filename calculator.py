print('My Self Gaurav Mishra')
print('My First Project In python')
print('Project Name = Calculator')
def addition ():
    print("Addition")
    s = float(input("Enter the number: "))
    n = 0 
    ans = 0
    while s != 0:
        ans = ans + s
        n+=1
        s = float(input("Enter another number (0 to calculate): "))
    return [ans,n]
def subtraction ():
    print("Subtraction")
    s = float(input("Enter the number: "))
    n = 0 
    sum = 0
    while s != 0:
        ans = ans - s
        n+=1
        s = float(input("Enter another number (0 to calculate): "))
    return [ans,n]
def multiplication ():
    print("Multiplication")
    s = float(input("Enter the number: "))
    n = 0 
    ans = 1
    while s != 0:
        ans = ans * s
        n+=1
        s = float(input("Enter another number (0 to calculate): "))
    return [ans,n]
def average():
    an = []
    an = addition()
    n = an[1]
    a = an[0]
    ans = a / n
    return [ans,n]
while True:
    list = []
    print(" Enter '1' for addition")
    print(" Enter '2' for substraction")
    print(" Enter '3' for multiplication")
    print(" Enter '4' for average")
    print(" Enter 'Q' for quit")
    c = input(" ")
    if c != 'Q': 
        if c == '1':
            list = addition()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == '2':
            list = subtraction()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == '3':
            list = multiplication()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == '4':
            list = average()
            print("Ans = ", list[0], " total inputs ",list[1])
        else:
            print ("Sorry, invilid character")
    else:
        break