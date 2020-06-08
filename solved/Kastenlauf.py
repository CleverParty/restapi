import numpy as np 

x = [int(x) for x in input("Enter multiple value: ").split()] 
print("List of students: ", x)  # taking multiple inputs 
#test with 2 2 0 0 1000 0 1000 1000 2000 1000
global_num = x[0]
num = x[0]
index_x = index_y = 0
def emotion(x,num):
    for i in range(0,int(num)):
        print("value of i is: ",i)
        for index in range(0,x[1]):
            print("index value is ",(x[index]))
            index_x = index + 3 
            index_y = index + 1
            val_x = abs(x[index_x] - x[index_y])
            val_y = abs(x[index_x + 1] - x[index_y + 1])
            manhatten_dist = val_x + val_y
            index_x = index_x + 1 
            index_y = index_y + 1
            index = index_x +index_y
            print("manhatten distance is : ",manhatten_dist)
            if(manhatten_dist>=1000): # because for the students to be happy they should satisify the 50 meters for every beer so that comes about to 1000 meter for every crate of 20 beers
                return("happy",index_x,index_y)
                continue
            else:
                return("sad",index_x,index_y)
                break
# 2 3 0 0 1000 0 1000 1000 2000 1000 3000 2000
num = x[0]
print(num)
start = x[2]
end = x[5]
print("vals being printsed")
for ind in range(0,int(global_num)):
    em , val_x , val_y = emotion(x , int(num))
    print(val_x)
    print(em)

