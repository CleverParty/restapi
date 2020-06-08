import numpy as np 

x = [int(x) for x in input("Enter multiple value: ").split()] 
print("List of students: ", x)  # taking multiple inputs 

num = x[0]
print(num)
start = x[2]
end = x[5]
print("vals being printsed")
for i in range(0,num):
    print(x[1])
    for index in range(0,x[1]):
        print(index)
        val_x = abs(x[index + 2] - x[index])
        val_y = abs(x[index + 3] - x[index +1])
        manhatten_dist = val_x + val_y
        print("manhatten distance is : ",manhatten_dist)
        if(manhatten_dist>=1000): # because for the students to be happy they should satisify the 50 meters for every beer so that comes about to 1000 meter for every crate of 20 beers
            print("happy")
        else:
            print("sad")
