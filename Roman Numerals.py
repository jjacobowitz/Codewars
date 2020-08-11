"""
Roman Numerals

Create a RomanNumerals class that can convert a roman numeral to and from an 
integer value. It should follow the API demonstrated in the examples below. 
Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting 
with the left most digit and skipping any digit with a value of zero. In Roman 
numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is 
written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in 
descending order: MDCLXVI.

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
Help
    * I = 1
    * V = 5
    * X = 10
    * L = 50
    * C = 100
    * D = 500
    * M = 1000
"""

class RomanNumerals():
    def to_roman(num):
        StringNum = str(num)
        Length = len(StringNum)
        NumToRoman = {1:{1:'I', 5:'V'}, 
                      10:{10:'X', 50:'L'}, 
                      100:{100:'C', 500:'D'}, 
                      1000:{1000:'M'}}
        converted = []
        for i in range(Length):
            place = 10**(Length - i - 1)
            current = int(StringNum[i])
            if current == 0:
                continue
            elif current <= 3:
                converted.append(NumToRoman[place][place]*(current))
            elif current == 4:
                converted.append(NumToRoman[place][place])
                converted.append(NumToRoman[place][5*place])
            elif current == 5:
                converted.append(NumToRoman[place][5*place])
            elif 6 <= current <= 8:
                converted.append(NumToRoman[place][5*place])
                converted.append(NumToRoman[place][place]*(current - 5))
            elif current == 9:
                converted.append(NumToRoman[place][place])
                converted.append(NumToRoman[10*place][10*place])
        return ''.join(converted)
    def from_roman(roman):
        RomanToNum = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = [RomanToNum[numeral] for numeral in roman]
        for i in range(len(roman)-1):
            if total[i] < total[i+1]:
                total[i] *= -1
        return sum(total)


print(RomanNumerals.to_roman(1) == 'I')
print(RomanNumerals.to_roman(2) == 'II')
print(RomanNumerals.to_roman(3) == 'III')
print(RomanNumerals.to_roman(4) == 'IV')
print(RomanNumerals.to_roman(30) == 'XXX')
print(RomanNumerals.to_roman(33) == 'XXXIII')
print(RomanNumerals.to_roman(40) == 'XL')
print(RomanNumerals.to_roman(50) == 'L')
print(RomanNumerals.to_roman(60) == 'LX')
print(RomanNumerals.to_roman(70) == 'LXX')
print(RomanNumerals.to_roman(80) == 'LXXX')
print(RomanNumerals.to_roman(300) == 'CCC')
print(RomanNumerals.to_roman(342) == 'CCCXLII')
print(RomanNumerals.to_roman(400) == 'CD')
print(RomanNumerals.to_roman(1000) == 'M')
print(RomanNumerals.to_roman(1990) == 'MCMXC')
print(RomanNumerals.to_roman(2000) == 'MM')

print(RomanNumerals.from_roman('I') == 1)
print(RomanNumerals.from_roman('XXI') == 21)
print(RomanNumerals.from_roman('XXX') == 30)
print(RomanNumerals.from_roman('XL') == 40)
print(RomanNumerals.from_roman('LX') == 60)
print(RomanNumerals.from_roman('LXXX') == 80)
print(RomanNumerals.from_roman('CCCXLII') == 342)
print(RomanNumerals.from_roman('CD') == 400)
print(RomanNumerals.from_roman('MMVIII') == 2008)
