from mpu9250 import Mpu9250
import matplotlib.pyplot as plt
from numpy import interp

mpu = Mpu9250()

plt.ion()
ax = plt.axes()

while True:
    plt.cla()
    x, y, z = mpu.get_gyro()
    x_value = interp(x,[-16000,16000],[-4,4])
    y_value = interp(y,[-16000,16000],[-4,4])
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.arrow(0, 0, x_value, y_value, head_width=0.05, head_length=0.1, fc='k', ec='k')
    plt.show() 
    plt.pause(0.05)

