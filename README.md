# Bienvenido a GamiHelper!

Este es un repositorio que alberga todos los programas que tienen relación con el entrenamiento y testeo del modelo encargado de convertir el habla en texto (Speech to Text) para el juego **GamiHelper**.

## Para empezar

Lo primero que haremos es instalar las dependencias necesarias para que podamos correr todos los programas sin ningún problema.

### Prerequisitos
* **SoundFile:** Si tiene problemas con la instalación, por favor ir a la documentación de la dependencia dando click [aquí](https://github.com/bastibe/python-soundfile#installation).
```sh
pip install soundfile
```
* **Numpy**
```sh
pip install numpy
```

### Instalación
1. Clone el repositorio
```sh
git clone https://github.com/u201322430/GamiHelper.git
 ```
 
### Uso
En esta sección se enseñará a usar 2 programas que ahora mismo este repositorio contiene:
1. **Add Noise**: Se encarga de agregarle ruido a audios.
2. **Reduce Volumen**: Se encarga de reducir el volumen a un audio ingreado:

## Add Noise
* **A tener en cuenta:** Todos los audios que se ingresen a este programa tendrán que ser **stereo** (tener 2 canales), debido a que el programa no soporta audios **mono** (1 canal).
* **Indicaciones**:
Lo primero que se debe de hacer es ingresar a la carpeta del programa:
```sh
cd noise_audio/
```
El programa es capaz de mostrar un panel de ayuda como este:
```sh
python add_noise.py -h
```
```sh
Uso: add_noise.py [-h] [-o OUTPUT] N A R

Argumentos obligatorios:
  N                     Directorio de los ruidos
  A                     Directorio de los audios a quienes se les agregará ruido
  R                     Directorio de los resultados

Argumentos opcionales:
  -h, --help            Muestra este mensaje
```
En el supuesto de que las carpetas, que contienen los audios a tratar, estén dentro del directorio donde se encuentra el programa como se muestra aquí:
```
./
-- add_noise.py
-- noises/
	-- ruido1.wav
	-- ruido2.wav
-- audios/
	-- audio1.wav
	-- audio2.wav
-- results/
```
Y luego usamos el siguiente comando para utilizar el programa:
```sh
python add_noise.py ./noises ./audios/ ./results
```
El resultado será el siguiente:
```sh
./
-- add_noise.py
-- noises/
	-- ruido1.wav
	-- ruido2.wav
-- audios/
	-- Name1
		-- comando1.wav
		-- comando2.wav
	-- Name2
		-- comando1.wav
		-- comando2.wav
-- results/
	-- comando1_Name1_0.wav
	-- comando1_Name1_1.wav
	-- comando2_Name1_0.wav
	-- comando2_Name1_1.wav
	-- comando1_Name2_0.wav
	-- comando1_Name2_1.wav
	-- comando2_Name2_0.wav
	-- comando2_Name2_1.wav
```
* **Conclusiones**: Notar que por cada audio se le ha agregado todos los ruidos que se encuentran en el directorio que se asignó.

## Reduce Volumen
* **Indicaciones**
Primero se debe de ingresar al directorio donde se encuentra el programa: 
```sh
cd noise_audio/
```
Ahora debemos recalcar que **este programa contiene 3 argumentos que deben de ser pasados de manera obligatoria**:
1. Cantidad en la que disminuirá el volumen (2 -> mitad del sonido).
2. **Dirección y nombre** del archivo que se creará como resultado.
3. **Dirección y nombre** del archivo al cual se le reducirá el volumen.

Si se tiene el siguiente directorio:
```sh
./
-- reduce_volu.py
-- noises/
	-- ruido.wav
```
Después de aplicar el programa de la siguiente manera:
```sh
py noise_audio/reduce_volu.py 2 ./noises/ruido_bajo_volumen.wav ./noises/ruido.wav
```
Obtendremos este resultado:
```sh
./
-- reduce_volu.py
-- noises/
	-- ruido.wav
	-- ruido_bajo_volumen.wav
```
## Generate CSV
* **Indicaciones**
Primero se debe de ingresar al directorio donde se encuentra el programa:
```sh
cd make_dataset
```
Este programa necesita de un argumento obligatorio, el cual es el directorio
donde se encuentran todos los audios.
Por ejemplo, si se tiene este directorio:
```sh
./
-- audios
	-- comando1_Name1_0.wav
	-- comando1_Name1_1.wav
	-- comando2_Name1_0.wav
	-- comando2_Name1_1.wav
	-- comando1_Name2_0.wav
	-- comando1_Name2_1.wav
	-- comando2_Name2_0.wav
	-- comando2_Name2_1.wav
```
El programa se encargará de crear un archivo *dataset.csv* dentro del directorio
raíz donde se está llamando al programa. Además, este archivo contendrá lo siguiente:
```sh
py generate_csv.py ./audios && cat dataset.csv

file,text
./dataset/comando1_Name1_0.wav,comando1
./dataset/comando1_Name1_1.wav,comando1
./dataset/comando2_Name1_0.wav,comando2
./dataset/comando2_Name1_1.wav,comando2
./dataset/comando1_Name2_0.wav,comando1
./dataset/comando1_Name2_1.wav,comando1
./dataset/comando2_Name2_0.wav,comando2
./dataset/comando2_Name2_1.wav,comando2
```
