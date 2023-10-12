import numpy as np
import control as cnt
import matplotlib.pyplot as plt



#considerando uma função de transferencia em malha aberta FT=k/(tau*s+1)
k=1.49
tau=2.98
Theta = 0.99 # atraso de propagação
num = np. array ([k])
den = np. array ([tau , 1])
H = cnt.tf(num , den)
n_pade = 20
( num_pade , den_pade ) = cnt.pade ( Theta , n_pade )
H_pade = cnt.tf( num_pade , den_pade )
Hs = cnt.series (H , H_pade)
Hmf = cnt.feedback(Hs, 1) # comentar essa parte para mudar a malha

t = np . linspace (0 ,40, 100)
(t , y ) = cnt.step_response ( 3*Hs, t )
(t , y1 ) = cnt.step_response ( 3*Hmf, t )# comentar essa parte para mudar a malha
plt.plot (t , y )
plt.plot (t , y1 )# comentar essa parte para mudar a malha
plt.xlabel ( ' t [ s ] ')
plt.ylabel('Amplitude')
plt.title('')

plt.grid ()
plt.show()