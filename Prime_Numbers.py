#print prime numbers
Start_Input=int(input("Enter The Start Values"))
End_Input=int(input("Enter The End Values"))
for var in range(Start_Input,End_Input):
    if(var>1):
        for i in range(2,var):
            if(var%i==0):
                break
        else:
            print(var)
