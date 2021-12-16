# Atomic clock
n = int(input("Input:"))
n = n % (24*60)
hours = n // 60
minuts = n % 60
print()
print("Current time is", hours, ":", minuts)