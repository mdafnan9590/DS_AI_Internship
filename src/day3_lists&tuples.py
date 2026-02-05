#task1
#Create a list named inventory 

inventory_list=["Apples", "Bananas", "Carrots", "Dates"]
print(inventory_list)

#Append(Eggs)

inventory_list.append("Eggs")
print(inventory_list)

#Remove(Bananas bcoz it sold out)

inventory_list.remove("Bananas")
print(inventory_list)

#organize the inventory alpabets using Sort

inventory_list.sort()
print("final updated inventory:",inventory_list)

#task2
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
first_reading = temperatures[0]
last_reading = temperatures[-1]
Afternoon_Peak = temperatures[3:6]
print(Afternoon_Peak)
last_3_hours =temperatures[-3:]
print(last_3_hours)

print(temperatures)
print(Afternoon_Peak)
print(last_3_hours)

#task3
screen_res = (1920, 1080)
print( "Current Resolution: 1920x1080")
print(screen_res)
screen_res[0] = 1280
print("Tuples cannot be modified")


