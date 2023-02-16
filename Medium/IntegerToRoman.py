def intToRoman(self, num: int) -> str:
    roman = '' # used to store the roman numeral
    while num > 0:
        if num >= 1000:
            roman += 'M'
            num-=1000
        elif num >= 500:
            if num >= 900:
                roman += 'CM'
                num -= 900
            else:
                roman += 'D'
                num-=500
        elif num >= 100:
            if num >= 400:
                roman += 'CD'
                num -= 400
            else:
                roman += 'C'
                num -= 100
        elif num >= 50:
            if num >= 90:
                roman += 'XC'
                num -= 90
            else:
                roman += 'L'
                num -= 50
        elif num >= 10:
            if num >= 40:
                roman += 'XL'
                num -= 40
            else:
                roman += 'X'
                num -= 10
        elif num >= 5:
            if num >= 9:
                roman += 'IX'
                num -= 9
            else:
                roman += 'V'
                num -= 5
        elif num >= 1:
            if num >= 4:
                roman += 'IV'
                num -= 4
            else:
                roman += 'I'
                num -= 1
    return roman