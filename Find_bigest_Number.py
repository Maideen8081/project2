num1=int(input("Enter Your number1"))
num2=int(input("Enter Your number2"))
num3=int(input("Enter Your number3"))
if(num1>num2 and num1>num3):
    print(num1,"is greate")
elif(num2>num1 and num2>num3):
    print(num2,"is greate")
elif(num3>num1 and num3>num2):
    print(num3,"is greate")
else:
    print("Defaut ")
