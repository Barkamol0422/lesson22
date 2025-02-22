def a(t):
    p = 1
    for n in t:
        p *= n
    return p
t = (1, 2, 3, 4, 5)
p = a(t)
print("The product of all numbers in the tuple is:", p)
