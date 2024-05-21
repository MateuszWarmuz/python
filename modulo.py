try:
    x = int(input("Please enter the positive integer number: "))
except ValueError:
    print("Only integers are allowed")

for i in range(x, 0, -1):
    if i%2 != 0:
        print(i)

