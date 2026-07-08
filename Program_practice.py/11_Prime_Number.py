for Num in range(2, 100):
    prime = True

    for i in range(2, Num):
        if Num % i == 0:
            prime = False
            break

    if prime:
        print(Num)