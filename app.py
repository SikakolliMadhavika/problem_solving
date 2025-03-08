# import math
# def apptitude_using_math(num1, num2):
#     value = num1/num2
#     print(value)
#     print(math.floor(value))
#     print(math.ceil(value))
#     print(value - math.floor(value))

# apptitude_using_math(13,5)

def apptitude_without_math(num1, num2):
    value = num1/num2
    floorvalue = num1//num2
    decimal = value - floorvalue
    print("The quotient value is",value)
    print("The decimal value is",decimal)
    if(decimal>0.5):
        print("The nearest or considered integer is",floorvalue + 1 )
    else:
        print("The nearest or considered integer is",floorvalue )
    print("The smallest integer value is",floorvalue)
    print("The biggest integer value is",floorvalue + 1)
    

apptitude_without_math(131,5)
