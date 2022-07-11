##TALLER "PROGRAMACIÓN ORIENTADA A LA BIOLOGÍA"

**RETO I: ¿Podés descubrir y anotar el orden en que se ha ejecutado cada operación?  ((4+5)*2)/5**

Primero se ejecuto el (4+5), despues (9*2) y por ultimo se dividio por 5

**RETO II: Creá una variable llamada doble, que sea el doble de la suma entre a y b.**      

a = 5
b = 3
c = 'hola'

doble = (a+b) *  2

print(doble)

**RETO III: Digamos que el ADN no es más que un mensaje en clave, que debe ser descifrado o interpretado**

Para la síntesis de proteínas. El mensaje está escrito por una secuencia determinada de 4 nucleótidos distintos
representados por las letras A, T, G y C. Dentro de la célula, el mensaje es transportado por otra molécula, 
el ARN, muy similar al ADN pero con U en vez de T. En este mensaje, cada triplete o grupo de tres letras del 
ARN se denomina codón, y cada aminoácido de las proteínas está codificado por uno o varios codones. Así por 
ejemplo el codón ‘AUG’ codifica para el aminoácido Metionina , el codón ‘AAA’ para Lisina, el codón ‘CUA’ para 
Leucina, etc. ¿Podrías escribir una cadena de ARN que codifique para el péptido (una cadena corta de aminoácidos) 
‘Met-Lis-Lis-Lis-Leu-Leu-Met’ combinando las variables met = ‘AUG’, lis = ‘AAA’ y leu = ‘CUA’ utilizando operadores matemáticos?

met = 'AUG'
lis = 'AAA' 
leu = 'CUA'

peptido = met + lis + lis + leu + leu + met

print(peptido)

**RETO IV: ¿Cadenas?¿letras? Si hablamos de cadenas y letras en Biología, lo primero que se nos viene a la cabeza son las macromoléculas.** 
**Como bien sabemos, el ADN es un mensaje en clave que guía la síntesis de proteínas. Este** 
**mensaje está escrito por una secuencia determinada de 4 nucleótidos distintos representados por las letras A, T, G** 
**y C. El contenido de C y G (es decir el porcentaje de CG) presente en el ADN de un organismo es una característica** 
**distintiva: por ejemplo las Actinobacterias tienen un contenido característicamente más alto de CG que otros organismos.** 
**Ahora, contar la cantidad de C y G en una cadena de ADN larguísima a mano puede ser un verdadero tedio ¿Podrías crear un** 
**programa que calcule el porcentaje de C y G de una cadena dada de ADN?**

adn = 'TGATAAGAGTACCCAGAATAAAATGAATAACTTTTTAAAGACAAAATCCTCTGTTATAATATTGCTAAAATTATTCAGAGTAATATTGTGGATTAAAGCCACAATAAGATTTATAATCTTAAATGATGGGACTACCATCCTTACTCTCTCCATTTCAAGGCTGACGATAAGGAGACCTGCTTTGCCGAGGAGGTACTACAGTTCTCTTCACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTTTTAATATGTCCAGTATTCATTTTTGCATGTTTGGTTAGGCTAGGGCTTAGGGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTAGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTCTATTGTGCCATACTGTTGAATGTTTATAATGCATGTTCTGTTTCCAAATTTCATGAAATCAAAACATTAATTTATTTAAACATTTACTTGAAATGTTCACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTTTTAATATGTCCAGTATTCATTTTTGCATGTTTGGTTAGGCTAGGGCTTAGGGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTAGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTCTATTGTGCCATACTGTTGAATGTTTATAATGCATGTTCTGTTTCCAAATTTCATGAAATCAAAACATTAATTTATTTAAACATTTACTTGAAATGTGGTGGTTTGTGATTTAGTTGATTTTATAGGCTAGTGGGAGAATTTACATTCAAATGTCTAAATCACTTAAAATTTCCCTTTATGGCCTGACAGTAACTTTTTTTTATTCATTTGGGGACAACTATGTCCGTGAGCTTCCATCCAGAGATTATAGTAGTAAATTGTAATTAAAGGATATGATGCACGTGAAATCACTTTGCAATCAT'

def calcularPorcentaje(cadena, valor):
    total = len(cadena)
    apariciones = cadena.count(valor)
    return round(apariciones * 100 / total)

print(calcularPorcentaje(adn, 'C'))
print(calcularPorcentaje(adn, 'G'))
print(calcularPorcentaje(adn, 'A'))
print(calcularPorcentaje(adn, 'T'))

**RETO V: La Asombrosa Maravillosa es nuestra valiente superheroína. Sus poderes son producto de mutaciones en un gen muy común,** 
**cuya secuencia en la mayoría de las personas es 'ATGGAACTTGCAATCGAAGTTGGC'. A diferencia de nosotros, el gen mutado de la Asombrosa** 
**Maravillosa incluye la secuencia 'GTTTGTGGTTG' en su interior. La Asombrosa Maravillosa adquirió sus poderes al beber Jugo Vencido.**
**El primer sorbo de esta poción prohibida causa el cambio de todas las citosinas (C) por timinas (T). El siguiente sorbo cambia** 
**todas las adeninas (A) por guaninas (G). El tercer sorbo cambia las citosinas (C) por adeninas (A). El cuarto sorbo... puede ser**
**mortal. ¿Podés escribir un programa que nos diga cuántos sorbos de Jugo Vencido debe beber un portador del gen normal, para** 
**ganar los poderes de la Asombrosa Maravillosa?**


def sorbosNecesarios(secuencia, oportunidades):
    
    mutado = 'GTTTGTGGTTG'
    contador = 0
    sorbos = 0
    chances = 0
    
    while (mutado not in secuencia) and (chances <= oportunidades):

        if contador == 0:
            secuencia = secuencia.replace("C", "T")
            contador = 1
            sorbos = sorbos + 1
        elif contador == 1:
            secuencia = secuencia.replace("A", "G")
            contador = 2
            sorbos = sorbos + 1
        else:
            secuencia = secuencia.replace("C", "A")
            contador = 0
            sorbos = sorbos + 1
            
        chances = chances + 1
        
    if mutado in secuencia:
        print("Necesito "+ str(sorbos)+" sorbos para mutar "+ secuencia)
    else:
        print("No muto "+ secuencia)
        
    
secuencia = 'ATGGAACTTGCAATCGAAGTTGGC'

sorbosNecesarios(secuencia, 5)


**RETO VI: ¿Se te ocurre qué operadores podrías usar para las listas?**

1. append añade un elemento final a la lista
2. clear vacia todos los elementos de una lista
3. extend une una lista con otra
4. count cuenta cuantas veces aparece un elemento en la lista
5. index da el indice donde esta un elemento
6. insert agrega un elemento en la lista en un indice
7. pop saca un elemento de la lista y lo borra
8. remove saca un elemento de la lista con ciertas caracteristicas
9. reverse da vuelta la lista
10. sort ordena los elementos


**RETO VII: Ya que encontramos el espécimen de rana con pelo en marte, nos gustaría contrastar sus características con las ranas** 
**terrestres. Sabiendo que el gen de la proteína diminuta es ‘ATGGAAGTTGGAATCCAAGTTGGA’ y el gen de una proteína similar de rana** 
**terrestre es ‘ATGGAAGTTAATGGAAGTTGGAGGAGA’ ¿podés crear un programa que compare la longitud de ambos genes y según cuál sea más** 
**grande nos imprima un mensaje informándonos el resultado?**

terrestre = 'ATGGAAGTTGGAATCCAAGTTGGA'

marciana = 'ATGGAAGTTAATGGAAGTTGGAGGAGA'

def genMasLargo(gen1,gen2):
    lenGen1 = len(gen1)
    lenGen2 = len(gen2)
    if  lenGen1 == lenGen2:
        print("Ambos genes tienen la misma medida: "+str(lenGen1))
    else:
        if  lenGen1 > lenGen2:
            print(gen1 + " es mas largo: "+ str(lenGen1))
        else:
            print(gen2 + " es mas largo: "+ str(lenGen2))
        
genMasLargo(terrestre, marciana)


**RETO VIII: Si nos ponemos un poco más estrictos, y siguiendo con el tema de los clones de bacterias, el programa que creamos** 
**antes tiene algunas fallas ‘numéricas’: en cada vuelta de división celular binaria se generarán dos clones, no uno. ¿Podrías** 
**escribir un programa que imprima ‘¡Somos 2 clones nuevos!’ en cada una de 20 vueltas?**

def divisionBacteriana(vueltas):
    for i in range(0,vueltas):
        print('¡Somos 2 clones nuevos! '+ 'vuelta: '+ str(i))
        

divisionBacteriana(3)

**RETO IX: Si ahora queremos hacer nuestro programa un poco más estricto, por cada vuelta deberíamos sumar el total de** 
**células que tenemos e imprimir ese número en el mensaje. Entonces, por ejemplo, como en la primer vuelta tenemos dos** 
**células, imprimimos como mensaje ‘¡Somos 2 clones!’ , pero en la segunda vuelta serán en total 4 células y el mensaje a** 
**imprimir debería ser ‘¡Somos 4 clones!’. ¿Podrías escribir esta modificación del programa?**

def divisionBacterianaEstricta(vueltas):
    clones = 2
    for i in range(0,vueltas):
        print('¡Somos '+str(clones)+' clones nuevos >:D!! '+ 'Vuelta: '+ str(i + 1))
        clones = clones * 2
        
divisionBacterianaEstricta(3)

