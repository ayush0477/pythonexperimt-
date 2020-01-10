you = int(input('enter your style number 1 to 10\n'))
here = int(input('enter herstyle number1 to 10\n'))
if (you>=8 or here>=8):
    print(you,here,"-2 ,yes")
elif(you<=2 or here<=2):
    print(you,here,"-0,no")
else:
    print(you,here,("1,maybe"))