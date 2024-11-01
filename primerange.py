min_range = int(input("Enter minimum range: "))
max_range = int(input("Enter maximum range: "))

for n in range(min_range, max_range + 1):
    if n <= 1:
        print(n, "Not prime")
    else:
        is_prime = True
        for i in range(2, (n // 2) + 1):
            if n % i == 0:  
                is_prime = False
                break  
        if is_prime:
            print(n, "Prime")
     

            
      
