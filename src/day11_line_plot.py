#topic1
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,4,6,8,11]
plt.plot(x,y)
plt.show()


#topic2
x = [1,2,3,4,5]
y = [5,4,3,2,1]
plt.scatter(x,y)
plt.show()

#topic3
import matplotlib.pyplot as plt
categories = ['A','B','C']
values =[11,20,15]
plt.bar(categories,values)
plt.show()

#topic4
plt.subplot(1, 2, 1)
plt.plot([1,2,3], [1,4,9])
plt.title("Line Plot")
plt.subplot(1, 2, 2)
plt.bar(['A','B','C'], [3,7,5])
plt.title("Bar Chart")
plt.show()

#task1
import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5] 
revenue = [2000, 4500, 4000, 7500, 9000]
plt.plot(months,revenue)
plt.title("Monthly Revenue Growth")
plt.xlabel("maths")
plt.ylabel("Revenue in USD")
plt.show()