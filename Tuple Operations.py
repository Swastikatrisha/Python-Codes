#Program to Perform Operatiions on Tuple
#creating a Tuple
my_tuple= (10,20,30,40,50)
print("Original Tuple:", my_tuple)

#1. Indexing
print("Element at index 2:", my_tuple[2])

#2. Slicing
print("tuple from index 1 to 3:", my_tuple[1:4])

#3. Concatenation
new_tuple= my_tuple + (60,70)
print("After Concatenation:", new_tuple)

#4. Repetition
repeated_tuple= my_tuple * 2
print("After Repetition:", repeated_tuple)

#5. Nested Tuple
nested_tuple= ((1,2),(2,3,4),(True, False))
print(nested_tuple)