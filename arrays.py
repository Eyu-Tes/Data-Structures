# arrays - a single long box with equal partitions (homogeneous)
#        - linear data structure

from array import *

# arrayName = array(typecode, [Initializers])
my_array = array('i', [10, 20, 30, 40, 50])
print(my_array)
print(type(my_array))
for i in my_array:
    print(i, end="\t")
print()


# Insertion
# ---------
# Insert at the beginning
my_array.insert(0, 100)
print(f'{my_array} \t\t---\t\t Inserted 100 at the beginning')

# Insert at the middle
my_array.insert(3, 70)
print(f'{my_array} \t\t---\t\t Inserted 70 at the middle')

# Insert at the end
my_array.append(60)
# my_array.insert(len(my_array), 60)
print(f'{my_array} \t\t---\t\t Inserted 60 at the end')



# Deletion
# ---------
# Delete the beginning
my_array.pop(0)
# my_array.remove(100)
# del my_array[0]
print(f'{my_array} \t\t---\t\t Deleted 100 at the beginning')

# Delete at the middle
my_array.pop(2)
print(f'{my_array} \t\t---\t\t Deleted 70 at the middle')

# Delete at the end
my_array.pop()
print(f'{my_array} \t\t---\t\t Deleted 60 at the end')