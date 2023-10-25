import random

def is_prime(x: int)-> bool:
    i = 2
    while x%i != 0:
       i += 1
    return i == x 

def primes(count: int)-> list[int]:
    lst = []
    num = 2
    while len(lst) < count:
       if is_prime(num):
           lst.append(num)
       num += 1
    return lst

def checksum(x:list[int])-> int:
   sum = 0
   for i in x:
      sum = (i + sum) * 113 % 10000007
   return sum

def pipeline()-> int:
    prime_numbers = primes(1000)
    random.seed(100)
    random.shuffle(prime_numbers)
    result = checksum(prime_numbers)
    return result

if __name__ == "__main__":
    primes_checksum = pipeline()
    print(primes_checksum)
