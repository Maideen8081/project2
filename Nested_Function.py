"""def function1():
    print("function 1")
    def function2():
        print("function 2")
    return function2
print(function1())
#print(obj())
"""
"""def function2(x):
    print("function 1 is print")
    def function3(y):
        return x+y
    return function3
obj1=function2(10)
obj2=obj1(20)
print(obj2)
"""
def function3(num):
    print("Multiplication Table")
    def function4():
        for i in range(1,num+1):
            print(i,"*",num,"=",num*i)
    return function4
obj=function3(5)
print(obj())
