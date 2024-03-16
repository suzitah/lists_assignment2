my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1,15)
new_list=["mary","john","peter"]
my_list.extend(new_list)
my_list.remove("peter")
# my_list.sort() wont work because my list is a mix of str and int
print(my_list)
print(my_list.index(30))