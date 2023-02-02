"""
A function that converts roman numerals to integers.
The roman numerals are upto 4999
Roman numerals larger than that the symbol should be added to
the dict[rom_sym]
"""
def romanToInt(s: str) -> int:
    rom_sym = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0 # holds the integre converted to roman
    # iterating through the string
    for i in s:
        try:
            if rom_sym[i] >= rom_sym[s[s.index(i) + 1]]:
                integer += rom_sym[i]
            else:
                integer -= rom_sym[i]
        except IndexError:
            integer += rom_sym[i]
            
        # removes character already transversed
        s = s.replace(i, "#", 1)
    return integer

print(romanToInt("MMMMCMXCIX")) # Prints 4999
