user_input=input("Please enter number of hours you worked in a week")
Number=int(user_input)
if (Number<0 or Number>168):
    print("INVALID")
elif (Number>50):
    Dollars=(40*8) + ((10 * 9) +  (Number-50)*10)
    print("YOU MADE",Dollars,"DOLLARS THIS WEEK")
elif (Number<=50):
    Dollars=((40*8) + ((Number-40) * 9))
    print("YOU MADE",Dollars,"DOLLARS THIS WEEK")
elif (Number<=40):
    Dollars=Number * 8
    print("YOU MADE",Dollars,"DOLLARS THIS WEEK")
   
