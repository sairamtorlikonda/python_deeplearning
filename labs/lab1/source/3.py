python_lst = ['sai','sam','madhu','ramya','jon']#this has all the students attending the python class
web_lst = ['sai','kumar','siri','mark','david']#this has all the students attending the web class
new_lst = []# new list to store the students
for item in python_lst: #checking and iterating the items in the list
    if item not in web_lst:
        new_lst.append(item)

print("the student list who are attending only python class :",new_lst)
print("the student list who are attending  python class :" ,python_lst)
print("the student list who are attending web class :",web_lst)