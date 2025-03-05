
#  sum of odd in given number
def sumOfOdd(num):
    sum =0
    while(num):
        if((num%10)%2 != 0):
            sum+= num%10
        num//=10
    return sum
print(sumOfOdd(2345))



# armstrong numbers in given range
def armstrongg(number):
    temp = number
    sum=0
    while(temp):
        sum+= (temp%10)** len(str(number))
        temp//=10
    if(sum == number):
        return True
    return False

def armstronginRange(num1, num2):
    for i in range(num1, num2+1):
        if(armstrongg(i)):
            print(i)
armstronginRange(12,250)



# smallest prime digit
def isPrime(digit):
    if digit<2:
        return False
    temp = digit
    for i in range(2, temp//2 +1):
        if(temp %i == 0):
            return False
    return True


def smallestPrime(number):
    primes = []
    i=0
    small=0
    while(number):
        if(isPrime(number%10)):
            primes.append(number%10)
        number//=10

    if(len(primes)==0):
        return 'No Prime digits in given number'
    if(len(primes)==1):
        return primes[0]
    for i in range(0, len(primes)-1):
        if(primes[i]<primes[i+1]):
            small=primes[i]
        else:
            small=primes[i+1]
    print(small)
print(smallestPrime(40460))

