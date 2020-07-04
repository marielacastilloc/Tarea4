# MPSS - Tarea4: Procesos aleatorios
## Mariela Castillo Cabezas B61610

1. (20 %) Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

Inicialmente se realiza la lectura del archivo bits10k.csv proporcionado mediante la librería pandas, se establece una frecuencia de operación de 5000 Hz y 50 puntos de muestreo. Se genera la forma de la onda portadora de los bits y seguidamente se realiza la modulación BPSK, para ello se crea una variable llamada senal la cual servirá para almacenar datos de la señal modulada y se utiliza seno que corresponde a la forma de onda sinusoidal. Las gráficas generadas para mostrar la onda portadora y el comportamiento de los primeros 10 bits de la modulación se muestran a continuación: 

![GitHub Logo](onda.png)          ![GitHub Logo](primerosbits.png)

Con la gráfica de la señal modulada se observan los cambios que ocurren en la fase de la onda sinusoidal cuando ocurren cambios en la secuencia de los bits, por lo que se confirma una modulación BPSK correcta. 

2. (10 %) Calcular la potencia promedio de la señal modulada generada.

Para este punto fue necesario importar el paquete integrate de la librería scipy ya que la potencia promedio se obtiene integrando la potencia instántanea y diviendo este valor entre el número de bits por el período. A continuación se muestran las ecuaciones necesarias para el cálculo: 

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=P_{inst} = senal^2">
</p>

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=\int \frac{P_{inst}}{N*T} dt">
</p>

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=P_{prom} = 0.49000098009997023">  
</p>

3. Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.
Se creó un arreglo de numpy con los valores entre -2 dB y 3 dB el cual corresponde a los valores de SNR, además se crearon las señales ruidosas utilizando la función generadora de muestras aleatorias de numpy (numpy.random.normal), para esto último fue necesario determinar en primera instancia los valores de mu y sigma, mu se designó igual a cero y sigma se calculó como se muestra a continuación: 

`<# Potencia del ruido (Pn) para SNR y potencia de la señal (Ps) dadas
    Pn = Ps / (10**(SNR / 10))

    # Desviación estándar del ruido
    sigma = np.sqrt(Pn)>`


    # Desviación estándar del ruido
    sigma = np.sqrt(Pn)
