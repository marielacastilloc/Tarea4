#!/usr/bin/env python
# coding: utf-8

# In[1]:


# IE-0405: Modelos Probabilísticos de Señales y Sistemas
# Tarea 4: Procesos aleatorios
# Estudiante: Mariela Castillo Cabezas
# Carné: B61610
# Profesor: Fabian Abarca Calderón
# I Ciclo 2020

# Importamos los paquetes necesarios 
import numpy as np
from scipy import stats
from scipy import signal
from scipy import integrate
import matplotlib.pyplot as plt
import pandas as pd


# In[24]:


#1 (20 %) Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal
# normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

# Observaciones: 
# f = 5000 Hz 
# 00K = un bit por símbolo

# Lectura del archivo 
bits1 = pd.read_csv('bits10k.csv', header = None)
bits = np.array(bits1)

# Largo de la lista
N = len(bits)

# Frecuencia de operación
f = 5000 # Hz

# Período de cada símbolo
T = 1/f 

# Número de puntos de muestreo por período
p = 50

# Puntos de muestreo para cada período
tp = np.linspace(0, T, p)

# Creación de la onda portadora
seno = np.sin(2*np.pi * f * tp)

# Visualización de la onda
plt.plot(tp, seno)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud de la onda portadora')
plt.title('Onda portadora')
plt.ticklabel_format(axis="x", style = "sci",scilimits = (0,0))
plt.show()

# Frecuencia de muestreo
fm = p/T # 50 kHz

# Creación de la línea temporal para la señal Tx
t = np.linspace(0, N*T, N*p)

# Inicializar el vector de la señal modulada Tx
senal = np.zeros(t.shape)

    
# Creación de la señal modulada BPSK
for k, b in enumerate(bits):
    if b == 1:
        senal[k*p:(k+1)*p] = seno
    else: 
        senal[k*p:(k+1)*p] = -seno


# Visualización de los primeros bits modulados
pb_1 = 0
pb_2 = 10
plt.figure(1)
plt.plot(senal[pb_1*p:pb_2*p])
plt.xlabel('Tiempo / s')
plt.ylabel("Amplitud")
plt.title("Muestra de los primeros " + str(pb_2) + " periodos de la señal modulada")
plt.show()


# In[16]:


# 2. (10 %) Calcular la potencia promedio de la señal modulada generada.

from scipy import integrate

# Potencia instantánea
Pinst = senal**2

# Potencia promedio 
Ps = integrate.trapz(Pinst, t) / (N * T)

print("La potencia promedio de la señal modulada es:", Ps)


# In[17]:


# 3. # 3. Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación 
# señal a ruido (SNR) desde -2 hasta 3 dB.


# Relación señal-a-ruido deseada
SNR_rango = [-2, -1, 0, 1, 2, 3] # Valores de SNR

BER = np.zeros(6)

for i in range(6):  
    SNR = SNR_rango[i]
    
    # Potencia del ruido (Pn) para SNR y potencia de la señal (Ps) dadas
    Pn = Ps / (10**(SNR / 10))

    # Desviación estándar del ruido
    sigma = np.sqrt(Pn)

    # Crear ruido (Pn = sigma^2)
    ruido = np.random.normal(0, sigma, senal.shape)
    
    # Simular "el canal
    Rx = senal + ruido
    
    # Visualización de los primeros bits recibidos
    pb = 10
    plt.figure(2)
    plt.plot(Rx[0:pb*p])
    plt.xlabel('Tiempo / s')
    plt.title('Señales ruidosas para el rango SNR = [-2,3] dB')
    
#4. Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), 
    # antes y después del canal ruidoso.
    
    # Antes del canal ruidoso
    fw, PSD = signal.welch(senal, fm, nperseg=1024)
    plt.figure(3)
    plt.semilogy(fw, PSD)
    plt.xlabel('Frecuencia / Hz')
    plt.ylabel('Densidad espectral de potencia / V**2/Hz')
    
    # Después del canal ruidoso
    fw, PSD = signal.welch(Rx, fm, nperseg=1024)
    plt.figure(4)
    plt.semilogy(fw, PSD)
    plt.xlabel('Frecuencia / Hz')
    plt.ylabel('Densidad espectral de potencia / V**2/Hz')
    
# 5. Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.
    
    # Pseudo-energía de la onda original 
    Es = np.sum(seno**2)
    
    # Inicialización del vector de bits recibidos
    bitsRx = np.zeros(bits.shape)
    
    for k, b in enumerate(bits):
        Ep = np.sum(Rx[k*p:(k+1)*p] * seno)
        if Ep > Es/2:
            bitsRx[k] = 1
        else:
            bitsRx[k] = 0
        
    err = np.sum(np.abs(bits - bitsRx))
    BER[i] = err/N
    
    print('Cuando SNR = ', SNR, 'el ruido es ', BER[i])

    


# In[25]:


# 6. Graficar BER versus SNR

plt.figure(5)
plt.plot(BER, SNR_rango)
plt.xlabel('BER (bit rate error)')
plt.ylabel('SNR / dB') 
plt.title('BER Vs SRN')
plt.ticklabel_format(axis="x", style = "sci",scilimits = (0,0))


# In[ ]:




