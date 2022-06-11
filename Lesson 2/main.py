def isPowerOfTwo(n: int) -> bool:
    if n == 1:
        return True
    if n < 1 or n % 2 != 0:
        return False
    isPowerOfTwo(n/2)
a = int(input("Number: "))
print(isPowerOfTwo(a))