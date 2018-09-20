my_list=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    x=int(input("enter the value:"))
    my_list.append(x)
print("given numbers are",my_list)
print("the fist and last numbers are({},{})".format(my_list[0],my_list[-1]))
