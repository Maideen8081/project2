ip="10.20.30.78.30.70"
var=ip.split(".")
print(var)
var[3],var[5]=var[5],var[3]
print(var)
var1=".".join(var)
print(var1)
print(type(var1))
