import numpy as np 

x = [int(x) for x in input("Enter multiple value: ").split()] 
print("List of students: ", x)  # taking multiple inputs 
#test with 2 2 0 0 1000 0 1000 1000 2000 1000
def emotion(x,num):
    for i in range(0,num):
        for index in range(0,x[1]):
            print("index value is ",(x[index+3]))
            val_x = abs(x[index + 3] - x[index + 1])
            val_y = abs(x[index + 4] - x[index + 2])
            manhatten_dist = val_x + val_y
            print("manhatten distance is : ",manhatten_dist)
            if(manhatten_dist>=1000): # because for the students to be happy they should satisify the 50 meters for every beer so that comes about to 1000 meter for every crate of 20 beers
                return("happy")
                continue
            else:
                return("sad")
                break

num = x[0]
print(num)
start = x[2]
end = x[5]
print("vals being printsed")
em = emotion(x , num)
print(em)

