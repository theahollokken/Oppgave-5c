import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

g = 9.81 #m/s**2
h = 10

x = np.linspace(0,10,70)
t_verdier = np.linspace(1,5,3) #tidspunktene

    
def partiellderiverte(x,t):
    a = -np.sin(x-np.sqrt(g*h*t))
    b = (g*h*np.sin(x-np.sqrt(g*h*t)))/(2*np.sqrt(g*h*t))
    return a, b

def zeta_fun(x, t):
    return np.cos(x - np.sqrt(g * h * t))

for t in t_verdier:
    zeta = zeta_fun(x, t)
    

# Plott for retningsdiagram
X, T = np.meshgrid(x,t_verdier)

a_derivert, b_derivert = partiellderiverte(X,T)

fig, ax = plt.subplots(figsize=(20,10))
q = ax.quiver(X,T,a_derivert, b_derivert, color = 'blue', headaxislength=5, headlength=7)
ax.set_title('Strømlinjer: bølgens bevegelse ved h=10m', fontsize = 20)

plt.xlabel('Bølgens posisjon/m', fontsize = 20)
plt.ylabel('Tid/s', fontsize = 20)
plt.ylim(0, 6)  # Justerer y-aksen
plt.grid(True)
plt.show()