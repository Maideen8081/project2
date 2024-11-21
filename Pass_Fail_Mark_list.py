Marks=[10,20,30,80,60,40,20,80]
pass_Marks=[]
Fail_Marks=[]
for i in Marks:
    if(i>=35):
        pass_Marks.append(i)
    else:
        Fail_Marks.append(i)
print("The Pass_Mark is",pass_Marks)
print("The Fail_Marks is",Fail_Marks)

