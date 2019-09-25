# fa19-516-160
# E.Cloudmesh.Common.5
# Task :  Develop a program that demonstrates the use of cloudmesh.common.StopWatch.

from cloudmesh.common.StopWatch import StopWatch # import StopWatch
from time import sleep
import os

# Start timer
StopWatch.start("calculation_sw")
a=5
b=6
product = a*b
print(product)
sleep(1)

sum=a+b

print(sum)

# Stop timer
StopWatch.stop("calculation_sw")

# Print results
print(StopWatch.get("calculation_sw"))




#Code reference Introduction to python : Gregor von Laszewski.: section 6.6