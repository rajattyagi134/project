#Sample program to print day of week by the number enter from user
user_input=input("Enter any one number from 1 to 7 of the week:")
Number=int(user_input)
my_list=["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print(my_list[Number-1])

