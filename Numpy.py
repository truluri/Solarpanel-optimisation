import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
figurstr = (15, 7)

t = np.linspace(0, 2 * np.pi, 1000)
f = np.cos(t)

plt.figure(figsize=figurstr)
plt.plot(t, f, color='b', linestyle='-')
plt.xlabel('t')
plt.ylabel('cos(t)')
#plt.show()

#print(t,f)

idx = (f < 0.05) & (f > -0.05)
print(f[idx], t[idx])

tegnSkift = np.where(np.diff(np.sign(f))!=0)
#print(tegnSkift)
#print(f[tegnSkift])

nulpunkter = np.interp(f[tegnSkift[0]], f[tegnSkift[0]+1], t[tegnSkift[0]])

print(nulpunkter)

#Hejsas