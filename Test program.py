n=int(input("enter the number of terms of fibonacii numbers you want: "))
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(a,b)
elif n>2:
    print(a,b,end=" ")
    while n>=3:
        c=a+b
        print(c,end=" ")
        a=b
        b=c    
        for n in range(n,3,-1):
            print("+",end="")
            n-=1
    print()       
else:
    print("invalid input")
          

