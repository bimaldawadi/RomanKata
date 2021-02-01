numbers = {"I": 1,"V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

def Convert_Roman(inNumber):
    flag = None
    for sym, integer in numbers.items():
        if integer == inNumber: return sym
        if inNumber>integer:
            flag=sym
        rem = integer - numbers[flag]
        return flag + Convert_Roman(rem)