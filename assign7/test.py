def func():
    l1 = list()
    l2 = list()
    for i in range(0, 5):
        l1.append(i)
        l2.append(i + 3)
    print(l1)
    print(l2)


def func():
    l1 = list()
    l2 = list()
    for i in range(0, 5):
        l1.append(i)
        l2.append(i + 3)
    l1, l2 = l2, l1
    print(l1)
    print(l2)


c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0
for i in range(0, 10):
    if c[i] % 2 == 0:
        result += c[i]
print(result)

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0
for i in range(0, 10):
    if c[i] % 2 != 0:
        result += c[i]
print(result)


# • Write a function that takes n as an input and creates a list of n lists such that ith list contains first five multiples of i.
# • Write a function that takes a number as an input parameter and returns the correspond text in words, for example, on input 452, the function should return 'Four Five Two'. Use a dictionary for mapping digits to their string representation.
# • Given the following inputs, indicate in each case (a) to (w), whether the statements will execute successfully. If, so, give what will be the outcome of execution? Also give the output of print statements (where applicable):
subject = "computer"
subject = list(subject)
ch = subject[0]
for i in range(0, len(subject) - 1):
    subject[i] = subject[i + 1]
subject[len(subject) - 1] = ch
print("".join(subject))

quantity = [15, 30, 12, 34, 56, 99]
total = 0
for i in range(0, len(quantity)):
    if quantity[i] > 15:
        total += quantity[i]
print(total)

x = [1, 2, 4, 6, 9, 10, 14, 15, 17]
for i in range(0, len(x)):
    if x[i] % 2 == 0:
        x[i] = 4 * i
    elif x[i] % 3 == 0:
        x[i] = 9 * i
    else:
        x[i] *= 2
print(x)

address = "B-6, Lodhi road, Delhi"
list1 = [1, 2, 3]
list2 = ["a", 1, "z", 26, "d", 4]
tuple1 = ("a", "e", "i", "o", "u")
tuple2 = ([2, 4, 6, 8], [3, 6, 9], [4, 8], 5)
dict1 = {"apple": "red", "mango": "yellow", "orange": "orange"}
dict2 = {
    "X": ["eng", "hindi", "maths", "science"],
    "XII": ["english", "physics", "chemistry", "maths"],
}
list1[3] = 4
print(list1 * 2)


print(min(list2))
print(max(list1))
print(list(address))

tuple2[3] = 6
tuple2.append(5)
t1 = tuple2 + (5)
",".join(tuple1)
list(zip(["apple", "orange"], ("red", "orange")))
dict2["XII"]
list2.extend(["e", 5])
print(list2)
list2.append(["e", 5])
print(list2)
names = ["rohan", "mohan", "gita"]
names.sort(key=len)
print(names)
list3 = [(x * 2) for x in range(1, 11)]
print(list3)
del list3[1:]
print(list3)
list4 = [x + y for x in range(1, 5) for y in range(1, 5)]
print(list4)
# 3
r

dict2["XII"].append("computer science"), dict2
"red" in dict1
list(dict1.items())
list(dict2.keys())
dict2.get("XI", "None")

# • Consider the following three sets, namely vehicles, heavyVehicles, and lightVehicles: #⟩⟩⟩
vehicles = {"Bicycle", "Scooter", "Car", "Bike", "Truck", "Bus", "Rickshaw"}
heavyVehicles = {"Truck", "Bus"}
lightVehicles = {"Rickshaw", "Scooter", "Bike", "Bicycle"}
# Determine the output on executing the following statements: 1. 3. 4. 5. 6.
lytVehicles = vehicles - heavyVehicles
print(lytVehicles)
hvyVehicles = vehicles - lightVehicles
print(hvyVehicles)
averageWeightVehicles = lytVehicles & hvyVehicles
print(averageWeightVehicles)
transport = lightVehicles | heavyVehicles
print(transport)
transport.add("Car")
print(transport)
for i in vehicles:
    print(i)

len(vehicles)
min(vehicles)
set.union(vehicles, lightVehicles, heavyVehicles)
