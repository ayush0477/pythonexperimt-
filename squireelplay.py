temp = int(input("enter the temparure value\n"))
summer = str(input("enter the summer value true or false\n"))
if(temp>=60 and temp<=90 and summer=="false"):
    print("true")
elif (temp>=60 and temp<=100 and summer=="true"):
    print("true")
else:
    print("false")