#WAP to get a input of a tuple from the user and then arrange the half of this tuple in acending order and the other half in decending order
a=eval(input("Enter a tuple : "))
l=[]
v=len(a)
if v%2==0:
    mid=v//2
    b=a[:mid]
    c=a[mid:]
    print(sorted(b)+sorted(c,reverse=True))
else:
    mid=(v//2)+1
    b=a[:mid]
    c=a[mid:]
    print(sorted(b)+sorted(c,reverse=True))
