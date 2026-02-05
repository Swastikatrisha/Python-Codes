#Program to Perform Operations on Set
#Creating a Set
set1= {10,20,30,40,50}
set2= {30,40,50,60,70}
print("Original Set1:", set1)
print("Original Set2:", set2)

#1. Adding Elements
set1.add(60)
print("After add(60):", set1)
#2. Removing Elements
set1.remove(20)       #Raises error if element is not present
print("After remove(20):", set1)
#3. Set Union
print("Union:", set1.union(set2))
#4. Set Intersection
print("Intersection:", set1.intersection(set2))
#5. Set Difference
print("Difference (set1-set2):", set1.difference(set2))
#6. Symmetric Difference
print("Symmetric Difference:", set1.symmetric_difference(set2))