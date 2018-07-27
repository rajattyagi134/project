#program to convert celsius to fahrenheit
user_input= input ("Please enter the temp in celsius to convert:")
celsius=float(user_input)
fahrenheit=((celsius*9)/5)+32
print("The temperature is :",fahrenheit,"degree Fahrenheit,")
if fahrenheit<32:
    print("It is freezing")
elif fahrenheit<50:
    print("It is chilly")
elif fahrenheit<90:
    print("It is OK")
else:   
    print("it is hot")

