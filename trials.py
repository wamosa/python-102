my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"List after appending: {my_list}") 
my_list[1]=15
print(my_list)
# Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])
print(my_list)
#removing the last element from the list
my_list.pop()
#sorting the list in ascending order
my_list.sort()
#printing the index of the value 30
index_of_30 = my_list.index(30)
print(index_of_30)




