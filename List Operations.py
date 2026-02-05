#Program to perform Operations on List
#Creating a List
my_list=[10,20,30,40,50]
print("Original List:", my_list)
#1. Indexing
print("Element at Index 2:", my_list[2])
#2. Slicing
print("List from Index 1 to 3:", my_list[1:4])
#3. Append
my_list.append(60)
print("After append(60):", my_list)
#4. Insert (add element at specific index)
my_list.insert(2,25)
print("After insert(2,25):", my_list)
#5. Remove (delete first occurence of element)
my_list.remove(40)
print("After remove(40):", my_list)
#6. Update Element
my_list[0]=5
print("After updating idex 0 to 5:", my_list)
#7. Reversing
my_list.reverse()
print("After reversing:", my_list)