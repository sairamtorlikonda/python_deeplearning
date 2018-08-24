s=input("enter the string:")
d=l=0
for c in s:
    if c.isalpha():
        l=l+1
    elif c.isdigit():
        d=d+1
    else:
        pass
print("letters:",l)
print("digits:",d)
