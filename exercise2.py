try:
	n=int(input("n-dy engiz:"))
except:
	print("San engiz")
	exit()
i=1
summa=0
if n>0:
	while i<=n:
		num=1/i
		print(num)
		summa=summa+num
		i+=1
else:
	print("n 0-den ulken bolsyn")
print("Summa:",summa)
