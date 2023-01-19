# File: FindPrimeFactors.py
# Student: Gaytri Riya Vasal
# UT EID: grv377
# Course Name: CS303E
# 
# Date Created: 10/26/2021
# Date Last Modified: 10/29/2021
# Description of Program: The following program will read in a series of positive integers and provide a list of prime factors for each integer.

def main():
    
    print("Find Prime Factors:")
    num = int(input("Enter a positive integer (or 0 to stop): "))

    def isPrime ( num ):
        import math
        if ( num < 2 or num % 2 == 0 ):
            return ( num == 2 )
        divisor = 3
        while ( divisor <= math . sqrt ( num )):
            if ( num % divisor == 0 ) :
                return False
            else:
                divisor += 2
        return True

    def findNextPrime ( num ):
        if ( num < 2 ):
            return 2
        if ( num % 2 == 0):
            num -= 1
        guess = num + 2
        while ( not isPrime ( guess )):
            guess += 2
        return guess
    
    while(True):
        if (num == 0):
            print("Goodbye!")
            return
        elif (num == 1):
            print("  1 has no prime factorization.")
            print()
            num = int(input("Enter a positive integer (or 0 to stop): "))
        elif (num < 0):
            print("  Negative integer entered. Try again.")
            print()
            num = int(input("Enter a positive integer (or 0 to stop): "))
        elif (num > 0):
            if (isPrime(num)):
               factors = [num]
               print("  The prime factorization of", num, "is:", factors)
               print()
               num = int(input("Enter a positive integer (or 0 to stop): "))
            else:
               factors = []
               num2 = num
               d = 2
               while (num2 > 1):
                   while (num2 % d == 0):
                       factors.append(d)
                       num2 /= d
                   d = findNextPrime(d)
               print("  The prime factorization of", num, "is:", factors)
               print()
               num = int(input("Enter a positive integer (or 0 to stop): "))
                   
main()
