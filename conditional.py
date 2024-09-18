day_of_week = input("enter day of the week : ").lower() #convert lowercase

print("Today day is : ",day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday": #true

    print(" I Learn New Things")

else: #false
    print (" i do routines things")

num1 = int(input("Enter a  first number : ")) #string casting str > int
num2 = int(input("Enter a second num : "))

choice = input("enter the operation: (options +,-,*,/,%)")

if choice == "+":
    sum_of_two_num = num1 + num2
    print ("do the addition: ",sum_of_two_num)

elif choice == "-":
    dif_of_two_num = num1 - num2
    print ("do subtraction :",dif_of_two_num)

elif choice == "*":
    prod_of_two_num = num1 * num2
    print("do multiply ;",prod_of_two_num)

elif choice == "/":
    div_of_two_num = num1 / num2
    print("do division :",div_of_two_num)

elif choice == "%":
    mod_of_two_num = num1 % num2
    print ("do modulus :",mod_of_two_num)
    
else:
    print("invalid operation")