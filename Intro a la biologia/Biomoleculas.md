##Biomoléculas: una breve introducción al nuestro mundo interior

**DESAFÍO I: ¿Podrías buscar un ejemplo de macromoléculas que almacenen información sobre la 'identidad' de un organismo dado?**

Los ácidos nucleicos son macromoléculas compuestas por nucleótidos y existen de dos tipos, ácido desoxirribonucleico (ADN) y ácido ribonucleico (ARN). 
El ADN es el material genético de los organismos vivos, guarda información genética a largo plazo, 
transmite esa información de padres a hijos y proporciona las instrucciones sobre cómo (y cuándo) hacer proteínas necesarias para construir y mantener 
en funcionamiento células, tejidos y organismos.

**DESAFÍO II: Propone una forma de expresar la información contenida en la estructura primaria de las proteínas usando tipos de datos de los lenguajes de programación que conocés.**

Lenguaje: Python


´´´´
from abc import ABC, abstractmethod

class Elem(ABC):
    carga = None 
    enlaces = [] #Los enlaces serán otros átomos u otras moléculas

class Atomo(Elem):
    def __init__(self, n, letra):
        self.cantidad = n
        self.elemento = letra
        

class Molecula(Elem):
    def __init__(self, carga, atomos):
        self.atomos = atomos #Son los átomos de los que está compuesta la molécula
        self.carga = carga #Carga de la molécula de tenerla
        

class Aminoacido:
    def __init__(self, elem1, elem2, elem3, amin):
        self.r = elem1  #Podrá ser un átomo o una molécula
        self.amino = elem2 # Podrá ser un átomo de N o una molécula que indica el inicio de la proteína
        self.carboxilico = elem3 # Podrá ser una molécula de CO o COOH que indica el final de la proteína
        self.h = Atomo(1,"H")
        self.hijo = amin #Es el siguiente aminoácido en la cadena de la proteína
´´´´	

**DESAFÍO III: ¿ En qué tipo de datos podrías expresar la información de la estructura terciaria proteica?**

Siguiendo el modelo que hice anteriormente, habria que agregarle referencias a la posicion de cada atomo o molecula en el espacio, y asi saber con que
otros aminoacidos de esa misma cadena van a enlazar de algna forma para tomar esa forma terciaria.

**DESAFÍO IV: Rosalind Franklin es una científica muy relevante, que tuvo menos reconocimiento del merecido.**
**¿Cuáles fueron sus contribuciones en este campo?**

Rosalind Franklin empezó a experimentar con la difracción de rayos X (ella ya era experta en cristalografía)  para estudiar la molécula de ADN y 
gracias a eso consiguió datos muy precisos, como las distancias entre sus distintos elementos. También observó detalles que sugerían que la 
molécula del ADN constaba de dos partes iguales y complementarias. 
La "Foto 51" y los resultados de su investigación, se convirtieron en la pieza clave del trabajo de sus compañeros (que también investigaban el 
ADN), James Watson y Francis Crick y lograron construir el primer modelo correcto de la molécula de ADN, con una doble hélice. Ya para ese entonces 
Rosalind había dejado su investigación y cambiado de Universidad en donde trabajaba.

**¿Qué nos cuenta su historia acerca del mundo de la ciencia?**

En esa época el machismo abundaba y varios colegas desestimaron a Franklin. Cuando Rosalind trabajó en la Universidad donde hizo su mayor 
descubrimiento del ADN, no la dejaban ingresar a la sala de descanso por ser mujer, y ahí perdió toda oportunidad de relacionarse con sus colegas 
y de tener alguna charla más informal.
Luego de que cambió de Universidad por no soportar el ambiente laboral, sus ex compañeros hicieron uso de sus descubrimientos sin su permiso. 
La competitividad era evidente también ya que cuando Watson y Crick fueron premiados nunca hicieron mención de que Franklin aportó a la causa y 
se quedaron con todo el crédito. 

**DESAFÍO V: Escribí un script en Python que prediga la estructura secundaria que adoptará cada residuo (aminoácido) de la secuencia proteica** 
**dada, especificandola como H (si es una hélice), B (si es una hoja beta plegada) y L (si es un bucle o loop).**

´´´´

import argparse

parser = argparse.ArgumentParser(description='Predice la estructura secundaria de la proteina')
parser.add_argument('-s', '--secuencia', type=str, help='secuencia de aminoacidos', required=True)

args = parser.parse_args()

secuencia = args.secuencia

estructurasPercent = {
    'E':#GLU
        [
          1.59, 0.52,1.01
        ],
    'A':#ALA
        [
          1.41, 0.72, 0.82
        ],
    'L':#LEU
        [
          1.34, 1.22, 0.57
        ],
    'M':#MET
        [
          1.30, 1.14, 0.54
        ],
    'Q':#GLN
        [
          1.27, 0.98, 0.84
        ],
    'K':#LYS
        [
          1.23, 0.69, 1.07
        ],
    'R':#ARG
        [
          1.21, 0.84, 0.90
        ],
    'H':#HIS
        [
          1.05, 0.80, 0.81
        ],
    'V':#VAL
        [
          0.90, 1.87, 0.41
        ],
    'I':#ILE
        [
          1.09, 1.67, 0.47
        ],
    'Y':#TYR
        [
          0.74, 1.45, 0.76
        ],
    'C':#CYS
        [
          0.66, 1.40, 0.54
        ],
    'W':#TRP
        [
          1.02, 1.35, 0.65
        ],
    'F':#PHE
        [
          1.16, 1.33, 0.59
        ],
    'T':#THR
        [
          0.76, 1.17, 0.90
        ],
    'G':#GLY
        [
          0.43, 0.58, 1.77
        ],
    'N':#ASN
        [
          0.76, 1.17, 0.90
        ],
    'P':#PRO
        [
          0.34, 0.31, 1.32
        ],
    'S':#SER
        [
          0.57, 0.96, 1.22
        ],
    'D':#ASP
        [
          0.99, 0.39, 1.24
        ]
}

total = len(secuencia)
secuenciaPercents = {}

for i in secuencia:
    if secuenciaPercents.get(i) == None:
        apariciones = secuencia.count(i)
        secuenciaPercents[i] = round(apariciones * 100 / total)
        

#print(secuenciaPercents)

glu = secuenciaPercents.get('E') >= 5 if secuenciaPercents.get('E') != None else False
ala = secuenciaPercents.get('A') >= 5 if secuenciaPercents.get('A') != None else False
leu = secuenciaPercents.get('L') >= 5 if secuenciaPercents.get('L') != None else False
met = secuenciaPercents.get('M') >= 5 if secuenciaPercents.get('M') != None else False
gln = secuenciaPercents.get('Q') >= 5 if secuenciaPercents.get('Q') != None else False
lys = secuenciaPercents.get('K') >= 5 if secuenciaPercents.get('K') != None else False
arg = secuenciaPercents.get('R') >= 5 if secuenciaPercents.get('R') != None else False
his = secuenciaPercents.get('H') >= 5 if secuenciaPercents.get('H') != None else False

helice =  glu and ala and leu and met and gln and lys and arg and his

val = secuenciaPercents.get('V') >= 5 if secuenciaPercents.get('V') != None else False
ile = secuenciaPercents.get('I') >= 5 if secuenciaPercents.get('I') != None else False
tyr = secuenciaPercents.get('Y') >= 5 if secuenciaPercents.get('Y') != None else False
cys = secuenciaPercents.get('C') >= 5 if secuenciaPercents.get('C') != None else False
trp = secuenciaPercents.get('W') >= 5 if secuenciaPercents.get('W') != None else False
phe = secuenciaPercents.get('F') >= 5 if secuenciaPercents.get('F') != None else False
thr = secuenciaPercents.get('H') >= 5 if secuenciaPercents.get('H') != None else False

plegada = val and ile and tyr and cys and trp and phe and thr

gly = secuenciaPercents.get('G') >= 5 if secuenciaPercents.get('G') != None else False
asn = secuenciaPercents.get('N') >= 5 if secuenciaPercents.get('N') != None else False
pro = secuenciaPercents.get('P') >= 5 if secuenciaPercents.get('P') != None else False
ser = secuenciaPercents.get('S') >= 5 if secuenciaPercents.get('S') != None else False
asp = secuenciaPercents.get('D') >= 5 if secuenciaPercents.get('D') != None else False

loop = gly and asn and pro and ser and asp

if helice:
    print("La proteina tiende a ser helice alfa")
elif plegada:
    print("La proteina tiende a ser beta plegada")
elif loop:
    print("La proteina tiende a ser un loop")
else:
    print("No se logro predecir nada para esta proteina")

´´´´


**PREGUNTAS DISPARADORAS: ¿Qué inputs tendría tu programa? ¿De qué modo se te ocurre configurar el output?**
 
Debería como input recibir una proteína con toda su cadena de aminoácidos para predecir que plegamiento tendría y como output solo devolveremos una 
letra, H que indique hélice o P si es plegada. 
 
**PARA PENSAR: ¿Cuántas proteínas puede sintetizar un organismo? ¿De qué depende la cantidad y la característica de las proteínas que puede sintetizar un organismo?**

El humano tiene 20.000 genes, así que podríamos decir que se pueden crear esas proteínas.  La cantidad depende de los genes del ADN, y las 
características van a depender de la combinación de los nucleótidos que tienen cada gen.  
DESAFÍO VI: ¿Qué hace distintos a dos individuos de una especie? Propone una forma de corroborar tu respuesta realizando un diagrama de un 
posible método computacional para dicho fin.
El ADN es la información genética que tenemos los seres vivos y que nos hace ser lo que somos. Es lo que nos da nuestra individualidad.
La secuencia de bases ADENINA - CITOSINA - GUANINA - TIMINA es variable, determina que los genes sean variables también y esos cambios en la secuencia 
nos pueden hacer diferentes.
Como forma de validar que cada ser humano tiene genes únicos, bastaría con recorrer las cadenas de genes del ADN de 2 individuos y ver si son la misma 
persona.

**PREGUNTAS DISPARADORAS: ¿Qué información deberías tener? ¿De qué modo deberías expresar dicha información para el análisis?**
 
Deberíamos tener la secuencia ordenada de nucleótidos de 2 individuos y esa información podría ser representada en forma de listas de Strings.


