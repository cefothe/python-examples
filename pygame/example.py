from turtle import *

shape("turtle")

print("how many direction you want?")
number_of_angles = int(input())

for x in range(0,number_of_angles):
    forward(50)
    right(360/number_of_angles)

done()