user_input=input("Please enter number of seconds")
Seconds=int(user_input)
Days= Seconds//(24*60*60)
Seconds_1=Seconds% (24*60*60)
Hours=Seconds_1//(60*60)
Seconds_2=Seconds_1%(60*60)
Minutes=Seconds_2//60
Seconds=Seconds_2%60
print(Days,"Days",Hours,"Hours",Minutes,"Minutes",Seconds,"Seconds")
   
