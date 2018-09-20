file1 = open("sai1.txt","r")
my_string1 = file1.read()
file2 = open("sai2.txt","r")
my_string2 = file2.read()


string1_lst = my_string1.split()#spliting the read file and storing it into the string1 as list
string2_lst = my_string2.split()#spliting the read file and storing it into the string2 as list
string3_lst =[ ]

for item1 in string1_lst:
    if item1.lower() not in string2_lst:
        # string3_lst + item1
        string3_lst.append(item1)# appending the checked items in the new list


print(my_string1 + "/n")
print(string1_lst)
print(my_string2 + "/n")
print(string2_lst)
print("\n")
print(" ".join(string3_lst))#printing the new list