#Program to Perform Operations on Dictionary
#Creating a Dictionary
my_dict= {
    "Name": "ABC",
    "Age": 25,
    "City": "Pune"
}
print("Original Dictionary:", my_dict)

#1. Accessing Elements
print("Name:", my_dict["Name"])
#2. Adding New Key-Value Pair
my_dict["Country"]="India"
print("After adding country:", my_dict)
#3. Updating Value
my_dict["Age"]=26
print("After updating age:", my_dict)
