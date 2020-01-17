a= str(input("enter the string\n"))
a = a.lower()
count = 0
read = 0
for count in range(len(a)-3):
   if a[count]=="c" and a[count+1]=="o" and a[count+2]=="d" and a[count+3]=="e":
        count=count+1
        read= read+1
print(read)