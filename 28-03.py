def revList(list):
    if len(list) == 0:
        return 
    print(list[-1])
    revList(list[0:-1])
revList([1,2,3,4])


def sumOfDigits(num):
    if num == 0:
        return 0
    digit = num%10
    # num = num//10
    return digit + sumOfDigits(num//10)
print(sumOfDigits(234))