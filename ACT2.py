def palidrome(a):
    b=len(a)-1
    d=0
    if a[b]!=a[d]:
        return False
        b+=1
        d-=1
    else:
        return True
a=(1,2,3,3,2,2)
if palidrome(a):
    print("Tuple is palindrome")
else:
    print("Tuple is not palindrome")
