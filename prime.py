n = int(input("Enter number: "))

if n <= 1:
    print("Not prime")
else:
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
