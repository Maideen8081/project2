num=14
temp=False
for i in range(2,num):
    if(i%num==0):
        temp=True
        break
if(temp==True):
    print("It's is Not  a prime Number")
else:
    print("It is a prime prime ")
