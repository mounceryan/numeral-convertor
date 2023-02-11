Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Inputting a number made of Arabic numerals

input_number = int(input("Enter a number: "))

#A validation to make sure that the code can only be executed if the Arabic numerals number is less than 4000

if input_number >= 4000:
    print("Enter a number less than 4000")
else:
    number = input_number

    number_digits = str(number)
    
    #The minimum length of a number using Roman numerals
    
    length_of_numeral = 1

    #Finding the units part of numeral

    if int(number_digits[-1]) == 1:
        units = "I"
    elif int(number_digits[-1]) == 2:
        units = "II"
    elif int(number_digits[-1]) == 3:
        units = "III"
    elif int(number_digits[-1]) == 4:
        units = "IV"
    elif int(number_digits[-1]) == 5:
        units = "V"
    elif int(number_digits[-1]) == 6:
        units = "VI"
    elif int(number_digits[-1]) == 7:
        units = "VII"
    elif int(number_digits[-1]) == 8:
        units = "VIII"
    elif int(number_digits[-1]) == 9:
        units = "IX"
    elif int(number_digits[-1]) == 0:
        units = ""

    #Finding the tens part of numeral

    if len(str(number)) > 1: #if the number is greater than one digit
        if int(number_digits[-2]) == 1:
            tens = "X"
        elif int(number_digits[-2]) == 2:
            tens = "XX"
        elif int(number_digits[-2]) == 3:
            tens = "XXX"
        elif int(number_digits[-2]) == 4:
            tens = "XL"
        elif int(number_digits[-2]) == 5:
            tens = "L"
        elif int(number_digits[-2]) == 6:
            tens = "LX"
        elif int(number_digits[-2]) == 7:
            tens = "LXX"
        elif int(number_digits[-2]) == 8:
            tens = "LXXX"
        elif int(number_digits[-2]) == 9:
            tens = "XC"
        elif int(number_digits[-2]) == 0:
            tens = ""
    else:
        tens = ""

    #Finding the hundreds part of numeral

...     if len(str(number)) > 2: #if the number is greater than two digits
...         if int(number_digits[-3]) == 1:
...             hundreds = "C"
...         elif int(number_digits[-3]) == 2:
...             hundreds = "CC"
...         elif int(number_digits[-3]) == 3:
...             hundreds = "CCC"
...         elif int(number_digits[-3]) == 4:
...             hundreds = "CD"
...         elif int(number_digits[-3]) == 5:
...             hundreds = "D"
...         elif int(number_digits[-3]) == 6:
...             hundreds = "DC"
...         elif int(number_digits[-3]) == 7:
...             hundreds = "DCC"
...         elif int(number_digits[-3]) == 8:
...             hundreds = "DCCC"
...         elif int(number_digits[-3]) == 9:
...             hundreds = "CM"
...         elif int(number_digits[-3]) == 0:
...             hundreds = ""
...     else:
...         hundreds = ""
... 
...     #Finding the thousands part of numeral
... 
...     if len(str(number)) > 3: #if the number is greater than three digits
...         if int(number_digits[-4]) == 1:
...             thousands = "M"
...         elif int(number_digits[-4]) == 2:
...             thousands = "MM"
...         elif int(number_digits[-4]) == 3:
...             thousands = "MMM"
...     else:
...         thousands = ""
...         
...     #Printing the Roman numeral
...     
