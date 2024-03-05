print("hello")
t=input(" for fahrenheint to celcius enter 2 and for celcius to fahrenheit enter 1 ")
if t=='1':
    celcius=float(input("write temperature : "))
    fahrenheit=(celcius*9/5)+32
    print(fahrenheit)
elif t=='2' :
    fahrenheit=float(input("write temperature  : "))
    celcius=(fahrenheit-32)*5/9
    print(celcius)