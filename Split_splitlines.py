#given IP Address to swap last number and Second number

ip="10.20.89.45.78"
var=ip.split(".")
#print(var)
var[2],var[4]=var[4],var[2]
#print(var)
var1=".".join(var)
print(var1)
