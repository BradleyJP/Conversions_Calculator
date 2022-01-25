import fractions
import math
#Note to self cubic anything is a measure of volume not length

#input your conversion
Number = float(input("How much: "))
print("reference")
ref = str(" c = celsius f = fahrenheit k = kelvin \n "
          " m = meters m2 = square meters m3 = cubic meters \n mi = miles \n ft = feet \n yd = yards ")
#asking for a reference won't move onto the next step
while ref:
    Convert1 = input("type ref to see unit tiltes \n What would you like to convert from: ", )
    if Convert1 == 'ref':
        print(ref)
    else:
        break
while ref:
    Convert2 = input("What are you converting it to: ", )
    if Convert2 == 'ref':
        print(ref)
    else:
        break

Fc = fractions.Fraction(5, 9)
F = 32
K = 273.15
#converts temperatures
#starting with freedom units
if Convert1 == "f":
    if Convert2 == "c":
        print("This is: ", (Number - F) * Fc, " celsius")
    elif Convert2 == "k":
        #to convert to kelvin from fahrenheit you have to first convert to celsius
        Cel = (Number - F) * Fc
        print("This is: ", Cel + K, " kelvin")
#conversions for celsius
elif Convert1 == "c":
    if Convert2 == "f":
        print("This is: ", (Number * Fc) + F, " fahrenheit")
    elif Convert2 == "k":
        print("This is: ", Number + K, " kelvin")
#conversions for kelvin
elif Convert1 == "k":
    if Convert2 == 'c':
        print("This is: ", Number - K, " celsius")
    elif Convert2 == 'f':
        print()

#conversions for meters
if Convert1 == "m":
    ft = 3.28084
    mi = 0.000621
    yd = 1.09361
    mm = 1000
    cm = 100
    km = 1000
    if Convert2 == "ft":
        print("This is: ", Number * ft, " feet")
    elif Convert2 == "mi":
        print("This is: ", Number * mi, " miles")
    elif Convert2 == "yd":
        print("This is: ", Number * yd, " yards")
    elif Convert2 == "mm":
        print("This is: ", Number * mm, " millimeters")
    elif Convert2 == "cm":
        print("This is: ", Number * cm, " centimeters")
    elif Convert2 == "km":
        print("This is: ", Number / km, " kilometers")
    elif Convert2 == "m2":
        op2 = float(input("Enter second operator: ", ))
        print("This is: ", Number * op2, "square meters")
    elif Convert2 == "m3":
        op2 = float(input("Enter second operator: ", ))
        op3 = float(input("Enter third operator: ", ))
        print("This is: ", Number * op2 * op3, "cubic meters")

#I want this to do dimentianal analysis
#converts cubic meters to varius mesures of volume, mass, and weight
if Convert1 == "m3":
    g = 1000000
    kg = 1000
    if Convert2 == "g":
        print("This is: ", Number * 1000000, "grams per cubic meter")
    elif Convert2 == "kg":
        print("This is: ", Number * kg, "kilograms per cubic meter")









