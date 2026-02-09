def addmultiplenumbers(numbers):
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def isiteven(num):
    if not isitaninteger(num):
        return False
    return int(num) % 2 == 0

def isitaninteger(num):
    if isinstance(num, (int, float)):
        return num == int(num)
    return False

def main():
    print("Hello learners!")