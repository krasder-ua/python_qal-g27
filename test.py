a = int(input("Enter a: "))
print("a: ", a)
b = int(input("Enter b: "))
print("b: ", b)
if b != 0:
    print("a / b = ", a / b)
else:
    print("Oops, division by zero")

o = input("Enter o: ")
if o == '+':
    print("a + b = ", a + b)
elif o == '-':
    print("a - b = ", a - b)
elif o == '*':
    print("a * b = ", a * b)
elif o == '/':
    if b != 0:
        print("a / b = ", a / b)
    else:
        print("Oops, division by zero")
else:
    print("Oops, not operation yet")