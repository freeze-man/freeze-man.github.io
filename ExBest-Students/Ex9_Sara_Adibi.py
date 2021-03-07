#Name family:sara adibi
#Execise_9
#Date:2/15/2021
#Subject:Python Pure

salary = [100000,1500000,879000,50000,206000,50000,126000,785300,159000,123000,453000,1555000]
sum = 0
s=0

for val in salary:
    sum += val
    s+=1

print("salary is: %4i " % sum)
print("average salary: %f " %(sum/s))