#!/anaconda/bin/python                                                          

import numpy as np
import matplotlib.pyplot as plt

from scipy import integrate as inte

time, velocity=np.loadtxt('droptower_vdata.txt', unpack=True)

distanceArray=inte.cumtrapz(velocity,initial=0) +30

accelArray=np.diff(velocity)

x2=np.arange(10)

plt.plot(time,distanceArray)
plt.title('Displacement of Tower')
plt.xlabel('time')
plt.ylabel('Displacement')
plt.savefig('displacement.png')


plt.figure()
plt.plot(time,velocity)
plt.title('Velocity  of Tower')
plt.xlabel('time')
plt.ylabel('Velocity')
plt.savefig('velocity.png')

plt.figure()
plt.plot(x2,accelArray)
plt.title('Acceleration  of Tower')
plt.xlabel('time')
plt.ylabel('Acceleration')
plt.savefig('accel.png')

plt.figure()
plt.plot(time,distanceArray,label='displacement',marker='o')
plt.plot(time,velocity,label='velocity',marker='v')
plt.plot(x2,accelArray,label='acceleration',marker="8")
plt.xlabel('time')
plt.ylabel('y')
plt.legend()
plt.savefig('allLines.png')

plt.figure()
f,axarr = plt.subplots(3,sharex=True)
axarr[0].plot(time,distanceArray,color='r',marker='o')
axarr[1].plot(time,velocity,color='b',marker='v')
axarr[2].plot(x2,accelArray,color='g',marker="8")
axarr[0].set_title("Displacement")
axarr[1].set_title("Velocity")
axarr[2].set_title("Acceleration")
axarr[0].set_xlabel('time')
axarr[1].set_xlabel('time')
axarr[2].set_xlabel('time')
axarr[0].set_ylabel('displacement')
axarr[1].set_ylabel('velocity')
axarr[2].set_ylabel('acceleratione')
axarr[0].set_ylim([0,70])
axarr[1].set_ylim([-25,25])
axarr[2].set_ylim([-20,20])
f.subplots_adjust(hspace=1)
plt.savefig('subplots.png')

 
