# Medium level


# Question - 1
def greatestOfThree(num1, num2, num3):
    if num1>num2:
        if num1>num3:
            return num1
        return num3
    elif num2>num3:
        return num2
    return num3
print(greatestOfThree(10,1,3))
print(greatestOfThree(1,11,3))
print(greatestOfThree(1,12,32))



# Question - 2
def leap(year):
    if year/100 == year//100:
        if year % 400 == 0:
            return "Leap Year"
    elif year % 4 == 0:
        return "Leap Year"
    return "Not a Leap Year"
print(leap(1400))
print(leap(2400))
print(leap(1484))


#Question - 4
def grade(marks):
    if marks>= 90 and marks<=100:
        return "A"
    elif marks>=80 and marks<=89:
        return "B"
    elif marks>=70 and marks<=79:
        return "C"
    elif marks<70 and marks>=0:
        return "Fail"
    return "Invalid"
print(grade(120))
print(grade(10))
print(grade(-20))
print(grade(90))



# Question - 5
def triangle(side1, side2, side3):
    if side1>0 and side2>0 and side3>0:
        if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
            return "Forms Triangle"
        return "Cannot form a Triangle"
    return "Invalid side lengths"
print(triangle(1,-2,3))
print(triangle(24,21,3))
print(triangle(10,7,5))
