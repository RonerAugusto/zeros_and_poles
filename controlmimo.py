import control as con
import math as mat
import control.matlab as conmat
import matplotlib.pyplot as plt 
import numpy as np  

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

state_space = con.StateSpace(a,b,c,d)
time = np.arange(0,15, .5,  dtype = float)
[wn,zeta,poles]=con.damp(state_space)



#periodo das oscilaçaoes amortecidas 

time_a = (2*mat.pi)/wn
time_pico = time_a/2


#tempo de subida

time_rise = (mat.pi - zeta)/wn
print("tempo de subida", time_rise)
print("tempo de pico", time_pico)
print("frequencia",wn)
print("constante",zeta)
print("polos",poles)

"""
conmat.pzmap(state_space)
plt.grid(True)
plt.show()

"""

[xout, yout] = con.step_response((state_space * 5 ),time)


plt.figure()
plt.plot(xout, yout)
plt.title("resposta ao degrau")
plt.xlabel("tempo")
plt.ylabel("saida")

plt.show()  
