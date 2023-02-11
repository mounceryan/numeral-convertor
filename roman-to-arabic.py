Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Inputting a number made of Roman numerals
... 
... input_number_input = input("Enter a Roman numeral: ")
... validation = ""
... 
... input_number = input_number_input
... 
... #Find the last digit
... 
... if input_number[-1] == "I" and (len(input_number) == 1 or input_number[-2] != "I" and input_number[-2] != "V"):
...     units = 1
...     input_number_without_units = input_number[:-1]
... elif input_number[-1] == "I" and input_number[-2] == "I" and (len(input_number) == 2 or input_number[-3] != "I" and input_number[-3] != "V"): 
...     units = 2
...     input_number_without_units = input_number[:-2]
... elif input_number[-1] == "I" and input_number[-2] == "I" and input_number[-3] == "I" and (len(input_number) == 3 or input_number[-4] != "I" and input_number[-4] != "V"): 
...     units = 3
...     input_number_without_units = input_number[:-3]
... elif len(input_number) >= 2 and input_number[-1] == "V" and input_number[-2] == "I":
...     units = 4
...     input_number_without_units = input_number[:-2]
... elif input_number[-1] == "V":
...     units = 5
...     input_number_without_units = input_number[:-1]
... elif len(input_number) >= 2 and input_number[-2] == "V" and input_number[-1] == "I":
...     units = 6
...     input_number_without_units = input_number[:-2]
... elif len(input_number) >= 3 and input_number[-3] == "V" and input_number[-2] == "I" and input_number[-1] == "I":
...     units = 7
...     input_number_without_units = input_number[:-3]
elif len(input_number) >= 4 and input_number[-4] == "V" and input_number[-3] == "I" and input_number[-2] == "I" and input_number[-1] == "I":
    units = 8
    input_number_without_units = input_number[:-4]
elif len(input_number) >= 2 and input_number[-2] == "I" and input_number[-1] == "X":
    units = 9
    input_number_without_units = input_number[:-2]
elif len(input_number) >= 1 and input_number[-1] == "X" or input_number[-1] == "L" or input_number[-1] == "C" or input_number[-1] == "D" or input_number[-1] == "M":
    units = 0
    input_number_without_units = input_number
else:
    validation = "Not a valid Roman numeral."
    
#Find the second to last digit

tens = ""

if len(input_number_without_units) >=1:
    if input_number_without_units[-1] == "X" and (len(input_number_without_units) == 1 or input_number_without_units[-2] != "X" and input_number_without_units[-2] != "L"):
        tens = "1"
        input_number_without_tens = input_number_without_units[:-1]
    elif input_number_without_units[-1] == "X" and input_number_without_units[-2] == "X" and (len(input_number_without_units) == 2 or input_number_without_units[-3] != "X" and input_number_without_units[-3] != "L"): 
        tens = "2"
        input_number_without_tens = input_number_without_units[:-2]
    elif input_number_without_units[-1] == "X" and input_number_without_units[-2] == "X" and input_number_without_units[-3] == "X" and (len(input_number_without_units) == 3 or input_number_without_units[-4] != "X" and input_number_without_units[-4] != "L"): 
        tens = "3"
        input_number_without_tens = input_number_without_units[:-3]
    elif len(input_number_without_units) >= 2 and input_number_without_units[-1] == "L" and input_number_without_units[-2] == "X":
        tens = "4"
        input_number_without_tens = input_number_without_units[:-2]
    elif input_number_without_units[-1] == "L":
        tens = "5"
        input_number_without_tens = input_number_without_units[:-1]
    elif len(input_number_without_units) >= 2 and input_number_without_units[-2] == "L" and input_number_without_units[-1] == "X":
        tens = "6"
        input_number_without_tens = input_number_without_units[:-2]
    elif len(input_number_without_units) >= 3 and input_number_without_units[-3] == "L" and input_number_without_units[-2] == "X" and input_number_without_units[-1] == "X":
        tens = "7"
        input_number_without_tens = input_number_without_units[:-3]
    elif len(input_number_without_units) >= 4 and input_number_without_units[-4] == "L" and input_number_without_units[-3] == "X" and input_number_without_units[-2] == "X" and input_number_without_units[-1] == "X":
        tens = "8"
        input_number_without_tens = input_number_without_units[:-4]
    elif len(input_number_without_units) >= 2 and input_number_without_units[-2] == "X" and input_number_without_units[-1] == "C":
        tens = "9"
        input_number_without_tens = input_number_without_units[:-2]
    elif len(input_number_without_units) >= 1 and input_number_without_units[-1] == "C" or input_number_without_units[-1] == "D" or input_number_without_units[-1] == "M":
        tens = "0"
        input_number_without_tens = input_number_without_units
    else:
        validation = "Not a valid Roman numeral."
        
#Find the third to last digit

hundreds = ""

if len(input_number_without_tens) >=1:
    if input_number_without_tens[-1] == "C" and (len(input_number_without_tens) == 1 or input_number_without_tens[-2] != "C" and input_number_without_tens[-2] != "D"):
        hundreds = "1"
        input_number_without_hundreds = input_number_without_tens[:-1]
    elif input_number_without_tens[-1] == "C" and input_number_without_tens[-2] == "C" and (len(input_number_without_tens) == 2 or input_number_without_tens[-3] != "C" and input_number_without_tens[-3] != "D"): 
        hundreds = "2"
        input_number_without_hundreds = input_number_without_tens[:-2]
    elif input_number_without_tens[-1] == "C" and input_number_without_tens[-2] == "C" and input_number_without_tens[-3] == "C" and (len(input_number_without_tens) == 3 or input_number_without_tens[-4] != "C" and input_number_without_tens[-4] != "D"): 
        hundreds = "3"
        input_number_without_hundreds = input_number_without_tens[:-3]
    elif len(input_number_without_tens) >= 2 and input_number_without_tens[-1] == "D" and input_number_without_tens[-2] == "C":
        hundreds = "4"
        input_number_without_hundreds = input_number_without_tens[:-2]
    elif input_number_without_tens[-1] == "D":
        hundreds = "5"
        input_number_without_hundreds = input_number_without_tens[:-1]
    elif len(input_number_without_tens) >= 2 and input_number_without_tens[-2] == "D" and input_number_without_tens[-1] == "C":
        hundreds = "6"
        input_number_without_hundreds = input_number_without_tens[:-2]
    elif len(input_number_without_tens) >= 3 and input_number_without_tens[-3] == "D" and input_number_without_tens[-2] == "C" and input_number_without_tens[-1] == "C":
        hundreds = "7"
        input_number_without_hundreds = input_number_without_tens[:-3]
    elif len(input_number_without_tens) >= 4 and input_number_without_tens[-4] == "D" and input_number_without_tens[-3] == "C" and input_number_without_tens[-2] == "C" and input_number_without_tens[-1] == "C":
        hundreds = "8"
        input_number_without_hundreds = input_number_without_tens[:-4]
    elif len(input_number_without_tens) >= 2 and input_number_without_tens[-2] == "C" and input_number_without_tens[-1] == "M":
        hundreds = "9"
        input_number_without_hundreds = input_number_without_tens[:-2]
    elif len(input_number_without_tens) >= 1 and input_number_without_tens[-1] == "M":
        hundreds = "0"
        input_number_without_hundreds = input_number_without_tens
    else:
        validation = "Not a valid Roman numeral."
        
#Find the fourth to last digit

thousands = ""

if len(input_number_without_hundreds) >=1:
    if input_number_without_hundreds[-1] == "M" and len(input_number_without_hundreds) == 1:
        thousands = "1"
        input_number_without_thousands = input_number_without_hundreds[:-1]
    elif input_number_without_hundreds[-1] == "M" and input_number_without_hundreds[-2] == "M" and (len(input_number_without_hundreds) == 2 or input_number_without_hundreds[-3] != "M"): 
        thousands = "2"
        input_number_without_thousands = input_number_without_hundreds[:-2]
    elif input_number_without_hundreds[-1] == "M" and input_number_without_hundreds[-2] == "M" and input_number_without_hundreds[-3] == "M" and (len(input_number_without_hundreds) == 3 or input_number_without_hundreds[-4] != "M"): 
        thousands = "3"
        input_number_without_thousands = input_number_without_hundreds[:-3]
    else:
        validation = "Not a valid Roman numeral."

#Print Statements to show workings
# print("input_number_without_units: " + str(input_number_without_units))
# print("input_number_without_tens: " + str(input_number_without_tens))
# print("input_number_without_hundreds: " + str(input_number_without_hundreds))
# print("Thousands: " + str(thousands))
# print("Hundreds: " + str(hundreds))
# print("Tens: " + str(tens))
# print("Units: " + str(units))

#Validation and output

if validation == "Not a valid Roman numeral.":
    print(validation)
else:
    print("The Arabic numeral for the Roman numeral " + input_number + " is " + str(thousands) + str(hundreds) + str(tens) + str(units))
    
SyntaxError: multiple statements found while compiling a single statement
