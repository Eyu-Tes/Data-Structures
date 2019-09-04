# Python lists - dynamic, heterogeneous
#              - linear data structure

my_list = [1, 2, 3, 4, 5, 6]
print(my_list)
print(type(my_list))

# Insertion
# ---------
# Insert at the beginning
my_list.insert(0, 'x')
print(f'{my_list} \t\t---\t\t Inserted \'x\' at the beginning')

# Insert at the middle
my_list.insert(3, 'z')
print(f'{my_list} \t\t---\t\t Inserted \'z\' at the middle')

# Insert at the end
my_list.append('y')
# my_list.insert(len(my_list), 'y')
print(f'{my_list} \t\t---\t\t Inserted \'y\' at the end')



# Deletion
# ---------
# Delete the beginning
my_list.pop(0)
# my_list.remove(1)
# del my_list[0]
print(f'{my_list} \t\t---\t\t Deleted \'x\' at the beginning')

# Delete at the middle
my_list.pop(3)
print(f'{my_list} \t\t---\t\t Deleted \'z\' at the middle')

# Delete at the end
my_list.pop()
print(f'{my_list} \t\t---\t\t Deleted \'y\' at the end')
