import control as con
import numpy as np  
import matplotlib.pyplot as plt 
import scipy.signal as sci


r = 1
l = 1
c = 1 

a  = np.array([   [ 0 , 1 ],
                   [ -1/(l*c), (-r/l)]

])

b = np.array([  [ 0],
                [1/l]
])

c = np.array ([ [ 1/c , 0 ]

])

d = np.array([  [0 ]
     
])


state_space =  con.StateSpace(a,b,c,d)

sysd = con.sample_system(state_space,0.1, method='zoh')
con.pzmap(sysd)

"""
fig = plt.figure()
ax = fig.add_subplot(111, projection="polar")
ax.plot(plan)
"""
plt.grid(True)

plt.show()
