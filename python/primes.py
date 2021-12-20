def isPrime(n):
    for i in range(2,n-1):
        if n % i == 0:
            return False
    
    return True

for i in range(100000):
    if isPrime(i):
        print(str(i), end='\r')


print()
