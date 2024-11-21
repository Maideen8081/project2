mark1=int(input("Enter Your mark1: "))
mark2=int(input("Enter Your mark2: "))
mark3=int(input("Enter Your mark3: "))
mark4=int(input("Enter Your mark4: "))
mark5=int(input("Enter Your mark5: "))
assert (mark1,mark2,mark3,mark4,mark5<=100)and(mark1,mark2,mark3,mark4,mark5>=0)
total=mark1+mark2+mark3+mark4+mark5
Average=total/5
print( "Total mark is ",total)
print("Average of Marke is",Average)
