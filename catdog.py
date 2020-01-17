a= input("enter the str\n")
a.encode()
b="cat"
c="dog"
string=""
for i in a :
    string = string + i
    if b in string and c in string:
        x=("true")
    else:
        x=("false")

print(x)