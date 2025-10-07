'''#WAP for making a pattern in python
for i in range(2,12,2):
    for j in range(2,i+2,2):
        print(j,end='')
    print() '''  


#WAP to find the sum of n elements of fibonacci series
n=int(input("Enter the number of terms sum you want pf fibonacci series : "))
first=0
second=1
sum=0
while n>=0:
    sum=first + second
    first=second
    second=first+second
    print(sum)
    
    
    
    
    
