# MPSS - Tarea4: Procesos aleatorios
## Mariela Castillo Cabezas B61610

1. (20 %) Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

Inicialmente se realiza la lectura del archivo bits10k.csv proporcionado mediante la librería pandas, se establece una frecuencia de operación de 5000 Hz y 50 puntos de muestreo. Se genera la forma de la onda portadora de los bits y seguidamente se realiza la modulación BPSK, para ello se crea una variable llamada senal la cual servirá para almacenar datos de la señal modulada y se utiliza seno que corresponde a la forma de onda sinusoidal. Las gráficas generadas para mostrar la onda portadora y el comportamiento de los primeros 10 bits de la modulación se muestran a continuación: 

![GitHub Logo](onda.png)          ![GitHub Logo](primerosbits.png)

Con la gráfica de la señal modulada se observan los cambios que ocurren en la fase de la onda sinusoidal cuando ocurren cambios en la secuencia de los bits, por lo que se confirma una modulación BPSK correcta. 

2. (10 %) Calcular la potencia promedio de la señal modulada generada.

Para este punto fue necesario importar el paquete integrate de la librería scipy ya que la potencia promedio se obtiene integrando la potencia instántanea y diviendo este valor entre el número de bits por el período. 
<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=P_{prom} = 0.49000098009997023">  
</p>
