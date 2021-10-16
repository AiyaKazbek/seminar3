try:
	num1 =int(input("Number1:"))
	num2 =int(input("Number2:"))
	num3 =int(input("Number3:"))
except:
	print("Error")
	exit()
max=0
if num1 > num2 and num1 > num3 :
    max = num1
elif num2 > num3 :
    max = num2
else :
    max = num3
print(max, "en ulken san.")
