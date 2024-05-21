list = []
for i in range(0,20):
    try:
        x = int(input("Please provide the positive integer number: "))
    except ValueError:
        print("Only integers are allowed")
    
    if x == 0:
        suma = sum(list)
        print(suma)
        break

    elif i == 20:
        print("You have reached maximal size of list")
    else:
        list.append(x)

    

