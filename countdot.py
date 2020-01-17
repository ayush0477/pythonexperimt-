a= str(input("enter the string\n"))
a = a.lower()
count = 0
read = 0
for count in range(len(a)):
   if a[count]=="c" or a[count]=="o" or a[count]=="e":
        count=count+1
        read= read+1
print(read)