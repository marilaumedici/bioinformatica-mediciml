**Introducción al Command Line Interface**

**Desafío I y III**

#!/usr/bin/env python3
import argparse


parser = argparse.ArgumentParser(description='Este es un saludador personalizado: ¡Toma tu nombre y apellido y te responde!')
parser.add_argument('-n', '--name', type=str, help='user name', required=True)
parser.add_argument('-l', '--lastname', type=str, help='user lastname')

args = parser.parse_args()

print(f"¡Hola "+str(args.name)+" "+str(args.lastname)+"! ¡Bienvenido o nose!")


**Desafío II**

Al ejecutar --help aparecen los datos que el programa necesita para funcionar

usage: hola.py [-h] -n NAME [-l LASTNAME]

Este es un saludador personalizado: ¡Toma tu nombre y apellido y te responde!

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  user name
  -l LASTNAME, --lastname LASTNAME
                        user lastname
						
**Desafío IV**

El parametro required lanzara un error indicando que necesita que el usuario le provea ese argumento.
Lanza error si no le pasan por argumento el dato que necesita.
						



