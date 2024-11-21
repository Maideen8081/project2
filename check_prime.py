flag=True
num=int(input("Enter the Prime Number"))

for i in range(2,num):
    if(i%num==0):
        print("not prime")
        flag=False
        break
if flag:
    print("not")
else:
    print("prime")    

