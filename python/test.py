import matplotlib.pyplot as plt
from distance import Distance
import time

left_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
right_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dist = Distance()

plt.ion()
plt.plot(left_values)
plt.plot(right_values)
plt.show()

while True:
    left_average = sum(left_values) / len(left_values)
    right_average = sum(right_values) / len(right_values)
    left_values.pop(0)
    right_values.pop(0)
    new_left_value = round(dist.get_distance_left(),1)
    new_right_value = round(dist.get_distance_right(),1)
    if abs(new_left_value - left_average) >
    
    left_values.append(new_left_value)
    right_values.append(new_right_value)
    
    plt.cla()
    plt.plot(left_values)
    plt.plot(right_values)
    plt.draw()
    
    time.sleep(0.05)
    plt.pause(0.05)
    