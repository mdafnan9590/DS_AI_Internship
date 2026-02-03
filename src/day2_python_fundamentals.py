#task1
#Asking the name of the person
name=input("Enter The Name :")
#Asking the age of the person
Age=input("Enter The Age :")
#Type casting String into integer
Age=int(Age)
#Calculating the age of person in 2030
Age+4
#Displaying the age of the person 
print(f"Hey {name},you will be {Age} years old in 2030")

#task2
total_bill=float(input("enter total bill"))
total_no_of_pepole=int(input("enter number of people"))
share_per_person=total_bill/total_no_of_pepole
print(f"total bill:{total_bill}each person pays:{share_per_person}")

#task3
item_name="laptop"
quantity=2
price=49999.9
in_stock=True
print(item_name,quantity,price,in_stock)
total_cost=quantity*price
print("total cost:",total_cost)