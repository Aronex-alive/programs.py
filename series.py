#WAP a program to create fibonacci series
'''n=int(input("Enter the number of elements to be printed of fibonacci series : "))
first=0
second=1
if n==1:
    print("The series is: ",first)
elif n==2:
    print("The series is: ",first,second)
elif n>=3:
    print("The series is: ",first,second,end=' ')
    while n>=3:
     third=first+second
     print(third,end=" ")
     first=second
     second=third
     n-=1
else:
    print("Enter valid number")'''


for i in range(1,5):
    for j in range(3,i-1,-1):
        print(end=" ")
    for k in range(1,i+1):
        print(k,end="")
    for l in range(i-1,0,-1):
        print(l,end="")
    print()        


#WAP to reverse the entered number
n=int(input("Enter the number to be reversed: "))
while n>0:
    s=n%10
    print(s,end="")
    n=n//10























        
    
















    
    
    
