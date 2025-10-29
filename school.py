a=eval(input("Enter a list : "))
b=eval(input("Enter an element to be searched : "))
v=[]
for i in range(len(a)):
	if a[i] == b:
		v.append(i)
# if v:
# 	print("Element found at indices:", v)
# else:
# 	print("Element not found")
print(len(v))	
        
