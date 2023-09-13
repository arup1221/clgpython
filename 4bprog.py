def roman2Dec(romstr):
    roman_digit = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romanBack = list(romstr)[::-1]
    value = 0

    rightval = roman_digit[romanBack[0]]
    for numreal in romanBack:
        leftval = roman_digit[numreal]
        if leftval < rightval:
            value -= leftval
        else:
            value += leftval
            rightval = leftval
    return value


romstr = input("Enter a Roman numeral: ")
print(roman2Dec(romstr))
