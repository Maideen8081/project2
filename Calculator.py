print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Divition")
print("5.Power")
choice=input("Enter Your Choice")
num1=int(input("Enter The Number1"))
num2=int(input("Enter the Number2"))
if(choice=='1'):
   print("Addition of ",num1,"And",num2," Numbers is", num1+num2)
elif(choice=='2'):
   print("Subraction of ",num1,"And",num2,"Numbers is", num1-num2)
elif(choice=='3'):
   print("Multiplicationof ",num1,"And",num2," Numbers is", num1*num2)
elif(choice=='4'):
   print(" Divition of ",num1,"And",num2," Numbers is", num1/num2)
elif(choice=='5'):
   print(" Power of ",num1,"And",num2," Numbers is", num1**num2)
else:
    print("Invalid")
     


