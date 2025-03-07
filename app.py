import math
def apptitudeValues(num1, num2):
    value = num1/num2
    print(value)
    print(math.floor(value))
    print(math.ceil(value))
    print(value - math.floor(value))

apptitudeValues(13,5)
apptitudeValues(123,10)