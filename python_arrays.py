#Arrays
cars = ["Ford", "Volvo", "BMW"]
cars2 = ["Ford", "Volvo", "BMW"]
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

#Access the Elements of an Array
x = cars[0]
cars[0] = "Toyota"

#The Length of an Array
x = len(cars)

#Looping Array Elements
for x in cars:
  print(x)

#Adding Array Elements
cars.append("Honda")

#Removing Array Elements
cars.pop(1)
cars2.remove("Volvo")