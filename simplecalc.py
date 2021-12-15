# simple calc

print('Calculate')

a = input("Enter a = ")
b = input("Enter b = ")

o = '**'
if o == '+':
    c = int(a) + int(b)

elif o == '-':
    c = int(a) - int(b)

elif o == '*':
    c = int(a) * int(b)

elif o == '/':
    c = int(a) * int(b)

# Floor division цілісний поділ
elif o == '//':
    c = int(a) // int(b)
# Exponentiation зведення в ступінь
elif o == '**':
    c = int(a) ** int(b)
# Modulus поділ за модулем
elif o == '%':
    c = int(a) % int(b)

print()
print("a"+ o + "b=", c)