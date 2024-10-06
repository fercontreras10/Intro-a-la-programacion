# Tarea 3
# Fernanda Contreras Carrasco

# Apertura correcta en una mano de Bridge

import random

# objeto de clase Carta
# Carta
# valor: str
# palo: str
class Carta:

   valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
   palos = ['P','C','D','T']

   # Constructor 
   def __init__(self, valor, palo):
       # Inicializacion de campos
       self.valor = valor
       self.palo = palo
       
   # getValor: None -> str
   # devuelve un string del campo valor       
   def getValor(self):
      return self.valor
   
   # getPalo: None -> str
   # devuelve un string del campo palo
   def getPalo(self):
      return self.palo

   # string: None -> str
   # devuelve un string del campo valor con el el campo palo
   def string(self):
      return str(self.valor) +  str(self.palo)

   # muestra los atributos escondidos
   # devuelve un string del campo valor con el el campo palo
   def __repr__(self):
      return str(self.valor) + str(self.palo)
   
# crear_mazo: None -> list
# devuelve una lista con el mazo de 52 cartas
# ejemplo: crear_mazo() devuelve [2P, 2C, 2D, 2T, 3P, 3C, 3D, 3T, 4P, 4C, 4D, 4T, 5P, 5C, 5D, 5T, 6P, 6C, 6D, 6T, 7P, 7C,
# 7D, 7T, 8P, 8C, 8D, 8T, 9P, 9C, 9D, 9T, 10P, 10C, 10D, 10T, JP, JC, JD, JT, QP, QC, QD, QT, KP, KC, KD, KT, AP, AC, AD, AT]
def crear_mazo():
    mazo = []
    for valor in Carta.valores:
        for palo in Carta.palos:
            mazo.append(Carta(valor,palo))
    return mazo

# crear_piques: None -> list
# devuelve una lista con 13 cartas de piques
# ejemplo: crear_piques() devuelve [2P, 3P, 4P, 5P, 6P, 7P, 8P, 9P, 10P, JP, QP, KP, AP]
def crear_piques():
    piques = []
    for valor in Carta.valores:
        for palo in Carta.palos[0]:
            piques.append(Carta(valor,palo))
    return piques
   
# crear_corazones: None -> list
# devuelve una lista con 13 cartas de corazones
# ejemplo: crear_corazones devuelve [2C, 3C, 4C, 5C, 6C, 7C, 8C, 9C, 10C, JC, QC, KC, AC]
def crear_corazones():
    corazones = []
    for valor in Carta.valores:
        for palo in Carta.palos[1]:
            corazones.append(Carta(valor,palo))
    return corazones

# crear_diamantes: None -> list
# devuelve una lista con 13 cartas de diamantes
# ejemplo: crear_diamantes() devuelve [2D, 3D, 4D, 5D, 6D, 7D, 8D, 9D, 10D, JD, QD, KD, AD]
def crear_diamantes():
    diamantes = []
    for valor in Carta.valores:
        for palo in Carta.palos[2]:
            diamantes.append(Carta(valor,palo))
    return diamantes

# crear_treboles: None -> list
# devuelve una lista con 13 cartas de treboles
# ejemplo: crear_treboles() devuelve [2T, 3T, 4T, 5T, 6T, 7T, 8T, 9T, 10T, JT, QT, KT, AT]
def crear_treboles():
    treboles = []
    for valor in Carta.valores:
        for palo in Carta.palos[3]:
            treboles.append(Carta(valor,palo))
    return treboles

# crear_mano: None -> list
# devuelve una lista de 13 cartas random
# ejemplo: crear_mano() devuelve [6P, 7P, 7T, 5T, 2D, 3C, QT, 3P, 2P, AP, 2C, 9T, 4C]
def crear_mano():
   mazo = crear_mazo()
   return random.sample(mazo,13)

# mano = crear_mano()

# separar_mano_valores: list -> list
# devuelve una lista de los valores de una mano
# ejemplo: separar_mano_valores([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T])
# devuelve ['A', 'Q', '8', '5', 'J', '7', '6', 'K', '9', '3', 'A', 'J', '8']
def separar_mano_valores(mano):
   listavalores = []
   for n in (range(0,13)):
         listavalores.append(mano[n].valor)
   return listavalores

# separar_mano_palos: list -> list
# devuelve una lista de los palos de una mano
# ejemplo: separar_mano_valores([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T])
# devuelve ['P', 'P', 'P', 'P', 'C', 'C', 'C', 'D', 'D', 'D', 'T', 'T', 'T']
def separar_mano_palos(mano):
   listavalores = []
   for n in (range(0,13)):
         listavalores.append(mano[n].palo)
   return listavalores
 
# frecuencia_valor: list -> dict
# devuelve un diccionario con la frecuencia de los valores de una lista
# ejemplo: frecuencia_valor([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T])
# devuelve {'A': 2, 'Q': 1, '8': 2, '5': 1, 'J': 2, '7': 1, '6': 1, 'K': 1, '9': 1, '3': 1}
def frecuencia_valor(mano):
   valor = separar_mano_valores(mano)
   frecuencias = {}
   for n in valor:
      if n in frecuencias:
         frecuencias[n] += 1
      else:
         frecuencias[n] = 1
   return frecuencias

# frecuencia_palo: list -> dict
# devuelve un diccionario con la frecuencia de los palos de una lista
# ejemplo: frecuencia_palo([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T])
# devuelve {'P': 4, 'C': 3, 'D': 3, 'T': 3}
def frecuencia_palo(mano):
   valor = separar_mano_palos(mano)
   frecuencias = {}
   for n in valor:
      if n in frecuencias:
         frecuencias[n] += 1
      else:
         frecuencias[n] = 1
   return frecuencias
   
# puntosH: list -> int
# devuelve los puntos honores de una mano
# distribucion de puntos honores para los valores A, K, Q y J
# Valet (J) = 1 puntos honores
# Dama (Q)  = 2 puntos honores
# Rey (K)   = 3 puntos honores
# As (A)    = 4 puntos honores
# ejemplo: puntosH([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve 15
def puntosH(mano):
   contador = 0
   valor = frecuencia_valor(mano)
   especiales = {'A':0,'K':0,'Q':0,'J':0}
   nuevo=dict(list(especiales.items()) + list(valor.items()))
   for n in nuevo:
      A = 4 * nuevo['A']
      K = 3 * nuevo['K']
      Q = 2 * nuevo['Q']
      J = 1 * nuevo['J']
      contador = A + K + Q + J
   return contador

# Puntos de distribucion

# fallo: list -> int
# devuelve los puntos de fallo de una mano
# un fallo ocurre cuando no se tiene ninguna carta de un palo en la mano
# se suman 3 puntos de distribucion (por cada palo que este fallo) 
# ejemplo: fallo([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve 0
def fallo(mano):
   contador = 0
   palo = frecuencia_palo(mano)
   for n in palo:
      if palo[n] == 0:
         return 3
      else:
         return 0 
   contador = palo['P'] + palo['C'] + palo['D'] + palo['T'] 
   return contador

# semi_fallo: list -> int
# devuelve los puntos de semi-fallo de una mano
# un semi-fallo ocurre cuando solo se tiene una carta de un palo en la mano
# se suman 2 puntos de distribucion (por cada palo que este semi-fallo)
# ejemplo: semi_fallo([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve 0
def semi_fallo(mano):
   contador = 0
   palo = frecuencia_palo(mano)
   for n in palo:
      if palo[n] == 1:
         return 2
      else:
         return 0 
   contador = palo['P'] + palo['C'] + palo['D'] + palo['T'] 
   return contador

# doubleton: list -> int
# devuelve los puntos de doubleton de una mano
# un doubleton ocurre cuando se tiene solo dos cartas de un palo en la mano
# se suma 1 punto de distribucion (por cada palo que este doubleton)
# ejemplo: doubleton([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve 0
def doubleton(mano):
   palo = frecuencia_palo(mano)
   condicion = sum(1 for n in palo if palo[n] == 2)
   if condicion:
      return condicion
   else:
      return 0

# ases: list -> int
# cuando una mano tiene los cuatro Ases del mazo se suma 1 punto de ditribucion (devuelve 1)
# cuando una mano no tiene ningun As del mazo se resta 1 punto de distribucion (devuelve -1)
# en los otros casos, si tiene de uno a tres Ases del mazo devuelve 0
# ejemplo: ases([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve 0
def ases(mano):
   valor = frecuencia_valor(mano)
   especiales = {'A':0}
   nuevo=dict(list(especiales.items()) + list(valor.items()))
   for n in nuevo:
      if nuevo['A'] == 4:
         return 1
      elif nuevo['A'] == 0:
         return -1
      else:
         return 0
      
# mas_de_cinco_en_un_palo: list -> int
# condicion = si un palo en la mano tiene mas de 5 cartas
# se suma 1 punto de distribucion por cada carta adicional.
# la funcion suma 1 por cada vez que se cumple la condicion
# si la condicion no se cumple devuelve 0
# ejemplo: mas_de_cinco_en_un_palo([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve 0
def mas_de_cinco_en_un_palo(mano):
   palo = frecuencia_palo(mano)
   condicion = sum(1 for k in palo.values() if k > 5)
   if condicion:
      return condicion
   else:
      return 0

# puntosD: list -> int
# devuelve los puntos de puntos de distribucion
# ejemplo: puntosD([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve 0
def puntosD(mano):
   return fallo(mano) + semi_fallo(mano) + doubleton(mano) + ases(mano) + mas_de_cinco_en_un_palo(mano)   

# puntosHD: list -> int
# devuelve la suma de los puntos honores mas los puntos de puntos de distribucion
# ejemplo: puntosHD([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T])
# devuelve 15
def puntosHD(mano):
   return puntosH(mano) + puntosD(mano)

# Palo quinto

# palo_mayor_quinto: list -> int
# Palos Mayores: Pique y Corazon (P y C)
# condicion: cuando una mano tiene algun palo con cinco o mas cartas
# devuelve 0 si no cumple la condicion ni para piques ni corazones
# devuelve 1 si tiene la misma cantidad de cartas de piques que de corazones, ambos cumplen la condicion
# devuelve 2 si tiene mas cartas de piques que de corazones, ambos cumplen la condicion
# devuelve 3 si tiene mas cartas de corazones que de piques, ambos cumplen la condicion
# devuelve 4 si tiene mas cartas de piques, solo piques cumple la condicion
# devuelve 5 si tiene mas cartas de corazones, solo corazones cumple la condicion
# ejemplo: palo_mayor_quinto([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve 0
def palo_mayor_quinto(mano):
   palo = frecuencia_palo(mano)
   # misma cantidad de piques que de corazones
   if (palo['P'] >=5) and (palo['C'] >= 5) and (palo['P'] == palo['C']):
      return 1
   # mas cartas de piques que de corazones
   elif (palo['P'] >= 5) > (palo['C'] >= 5):
      return 2
   # mas cartas de corazones que de piques
   elif (palo['C']>= 5) > (palo['P'] >= 5):
      return 3
   # palo mayor quinto piques
   elif palo['P'] >=5:
      return 4
   # palo mayor quinto corazones
   elif palo['C'] >=5:
      return 5
   # ni piques ni corazones tiene palo mayor quinto
   else:
      return 0
    
# convertir_a_string_cada_elemento_de_la_mano: list -> list
# devuelve una lista con cada elemento en un string 
# ejemplo: convertir_a_string_cada_elemento_de_la_mano([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T])
# devuelve ['AP', 'QP', '8P', '5P', 'JC', '7C', '6C', 'KD', '9D', '3D', 'AT', 'JT', '8T']
def convertir_a_string_cada_elemento_de_la_mano(mano):
   manostr = []
   for n in range(0,13):
      manostr.append(str(mano[n]))
   return manostr

# frecuencia_mano: list -> dict
# devuelve un diccionario con la frecuencia de una mano
# utilidad: para poder calcular los puntos honores de un palo con el mismo metodo de la funcion puntosH(mano)
# ejemplo: frecuencia_mano([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T])
# devuelve {'AP': 1, 'QP': 1, '8P': 1, '5P': 1, 'JC': 1, '7C': 1, '6C': 1, 'KD': 1, '9D': 1, '3D': 1, 'AT': 1, 'JT': 1, '8T': 1}
def frecuencia_mano(mano):
   mano = convertir_a_string_cada_elemento_de_la_mano(mano)
   frecuencias = {}
   for n in mano:
      if n in frecuencias:
         frecuencias[n] += 1
      else:
         frecuencias[n] = 1
   return frecuencias

# puntosH_diamantes_de_una_mano: list -> int
# devuelve los puntos honores de un palo, en este caso para los diamantes
# distribucion de puntos honores para los valores A, K, Q y J
# Valet (J) = 1 puntos honores
# Dama (Q)  = 2 puntos honores
# Rey (K)   = 3 puntos honores
# As (A)    = 4 puntos honores
# ejemplo: puntosH_diamantes_de_una_mano([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve 3
def puntosH_diamantes_de_una_mano(mano):
   contador = 0
   mano = frecuencia_mano(mano)
   especiales = {'AP':0,'KP':0,'QP':0,'JP':0,'AC':0,'KC':0,'QC':0,'JC':0,'AD':0,'KD':0,'QD':0,'JD':0,'AT':0,'KT':0,'QT':0,'JT':0}
   nuevo=dict(list(especiales.items()) + list(mano.items()))
   for n in nuevo:
         AD = 4 * nuevo['AD']
         KD = 3 * nuevo['KD']
         QD = 2 * nuevo['QD']
         JD = 1 * nuevo['JD']
   contador = AD + KD + QD + JD
   return contador

# puntosH_treboles_de_una_mano: list -> int
# devuelve los puntos honores de un palo, en este caso para los treboles
# distribucion de puntos honores para los valores A, K, Q y J
# Valet (J) = 1 puntos honores
# Dama (Q)  = 2 puntos honores
# Rey (K)   = 3 puntos honores
# As (A)    = 4 puntos honores
# ejemplo: puntosH_treboles_de_una_mano([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve 5
def puntosH_treboles_de_una_mano(mano):
   contador = 0
   mano = frecuencia_mano(mano)
   especiales = {'AP':0,'KP':0,'QP':0,'JP':0,'AC':0,'KC':0,'QC':0,'JC':0,'AD':0,'KD':0,'QD':0,'JD':0,'AT':0,'KT':0,'QT':0,'JT':0}
   nuevo=dict(list(especiales.items()) + list(mano.items()))
   for n in nuevo:
         AT = 4 * nuevo['AT']
         KT = 3 * nuevo['KT']
         QT = 2 * nuevo['QT']
         JT = 1 * nuevo['JT']
   contador = AT + KT + QT + JT
   return contador

# palo_menor_quinto: list -> int
# Palos Menores: Diamante y Trebol (D y T)
# condicion: cuando una mano tiene algun palo con cinco o mas cartas
# devuelve 0 si no cumple la condicion ni para diamantes ni treboles
# si no cumple con la condicion pero tiene 3 cartas de diamante y 3 cartas de trebol, se miran los puntos honores de cada palo:
   # devuelve 1 si tiene la misma cantidad de puntos honores de diamantes que de treboles
   # devuelve 2 si tiene mas puntos honores de diamante
   # devuelve 3 si tiene mas puntos honores de treboles
# devuelve 4 si tiene la misma cantidad de cartas de diamante que de trebol, ambos cumplen la condicion
# devuelve 5 si tiene mas cartas de diamante que de trebol, ambos cumplen la condicion
# devuelve 6 si tiene mas cartas de treboles que de diamantes, ambos cumplen la condicion
# devuelve 7 si tiene mas cartas de diamantes, solo diamantes cumplen la condicion
# devuelve 8 si tiene mas cartas de treboles, solo treboles cumplen la condicion
# ejemplo: palo_mayor_quinto([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve 3
def palo_menor_quinto(mano):
   Hdiamantes = puntosH_diamantes_de_una_mano(mano)
   Htreboles = puntosH_treboles_de_una_mano(mano)
   palo = frecuencia_palo(mano)
   # si diamantes y treboles tienen tres cartas
   if (palo['D'] == 3) and (palo['T'] == 3):
      # misma cantidad de puntos honores para diamantes y treboles
      if Hdiamantes == Htreboles:
         return 1
      # mas puntos honores para diamantes que treboles
      elif Hdiamantes > Htreboles:
         return 2
      # mas puntos honores para treboles que diamantes
      elif Htreboles > Hdiamantes:
         return 3
   # misma cantidad de diamantes que de treboles
   elif (palo['D']>= 5) and (palo['T']>= 5) and (palo['D'] == palo['T']):
      return 4
   # mas cartas de diamantes que de treboles
   elif (palo['D']>= 5) > (palo['T']>= 5):
      return 5
   # mas cartas de treboles que de diamantes
   elif (palo['T']>= 5) > (palo['D']>= 5):
      return 6
   # palo menor quinto diamantes
   elif (palo['D']>= 5):
      return 7
   # palo menor quinto treboles
   elif (palo['T']>= 5):
      return 8
   # ni diamantes ni treboles tienen palo menor quinto
   else:
      return 0
   
# Palo Protegido

# piques_protegido: list -> bool
# devuelve True si cumple con alguna de las condiciones de palo protegido para piques, si no cumple devuelve False
# es palo protegido si algun palo tiene:
# As o el Rey y al menos una carta adicional
# Dama y al menos dos cartas adicionales
# Valet y al menos tres cartas adicionales
# ejemplo: piques_protegido([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve True
def piques_protegido(mano):
   piques = crear_piques()
   palo = frecuencia_palo(mano)
   A = str(piques[12])
   K = str(piques[11])
   Q = str(piques[10])
   J = str(piques[9])
   for n in range(0,12):
      if str(mano[n]) == ((A or K) and (palo['P'] > 1)) or (Q and (palo['P'] > 2)) or (J and (palo['P'] > 3)):
         return True
      else:
         False
         
# corazones_protegido: list -> bool
# devuelve True si cumple con alguna de las condiciones de palo protegido para corazones, si no cumple devuelve False
# es palo protegido si algun palo tiene:
# As o el Rey y al menos una carta adicional
# Dama y al menos dos cartas adicionales
# Valet y al menos tres cartas adicionales
# ejemplo: piques_protegido([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve True 
def corazones_protegido(mano):
   corazones = crear_corazones()
   palo = frecuencia_palo(mano)
   A = str(corazones[12])
   K = str(corazones[11])
   Q = str(corazones[10])
   J = str(corazones[9])
   for n in range(0,12):
      if str(mano[n]) == ((A or K) and (palo['C'] > 1)) or (Q and (palo['C'] > 2)) or (J and (palo['C'] > 3)):
         return True
      else:
         False
   
# diamantes_protegido: list -> bool
# devuelve True si cumple con alguna de las condiciones de palo protegido para diamantes, si no cumple devuelve False
# es palo protegido si algun palo tiene:
# As o el Rey y al menos una carta adicional
# Dama y al menos dos cartas adicionales
# Valet y al menos tres cartas adicionales
# ejemplo: piques_protegido([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve True
def diamantes_protegido(mano):
   diamantes = crear_diamantes()
   palo = frecuencia_palo(mano)
   A = str(diamantes[12])
   K = str(diamantes[11])
   Q = str(diamantes[10])
   J = str(diamantes[9])
   for n in range(0,12):
      if str(mano[n]) == ((A or K) and (palo['D'] > 1)) or (Q and (palo['D'] > 2)) or (J and (palo['D'] > 3)):
         return True
      else:
         False
   
# treboles_protegido: list -> bool
# devuelve True si cumple con alguna de las condiciones de palo protegido para treboles, si no cumple devuelve False
# es palo protegido si algun palo tiene:
# As o el Rey y al menos una carta adicional
# Dama y al menos dos cartas adicionales
# Valet y al menos tres cartas adicionales
# ejemplo: piques_protegido([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve True
def treboles_protegido(mano):
   treboles = crear_treboles()
   palo = frecuencia_palo(mano)
   A = str(treboles[12])
   K = str(treboles[11])
   Q = str(treboles[10])
   J = str(treboles[9])
   for n in range(0,12):
      if str(mano[n]) == ((A or K) and (palo['T'] > 1)) or (Q and (palo['T'] > 2)) or (J and (palo['T'] > 3)):
         return True
      else:
         False
         
# protegido: list -> int
# devuelve 4 si tiene los cuatro palos protegidos
# devuelve 0 si no tiene los cuatro palos protegidos
# ejemplo: protegido([AP, QP, 8P, 5P, JC, 7C, 6C, KD, 9D, 3D, AT, JT, 8T]) devuelve 4
def protegido(mano):
   P = piques_protegido(mano)
   C = corazones_protegido(mano)
   D = diamantes_protegido(mano)
   T = treboles_protegido(mano)
   if P and C and D and T == True:
      return 4
   else:
      return 0
   
# Apertura
# declaraciones de apertura
# H : puntos honores; H+D : puntos honores + puntos de distribucion

# pass = si la mano del jugador no cumple con las condiciones de apertura, el jugador pasa (pass)

# apertura de 1 a palo: 1T,1D,1C,1P; entre 13 puntos H o 14 puntos H+D, hasta 20 puntos H+D
   # si no tiene ningun As, igual cumple con la condicion para la apertura de 1 a palo:
      # si la mano tuviese 13 puntos H y solo 12 puntos H+D (porque no tiene ningún As)
      # o 14 puntos H y śolo 13 puntos H+D (porque no tiene ningun As)
      
# apertura de 1 sin triunfo: 1ST; entre 16 y 18 puntos H, no se consideran los puntos H+D
      # ademas no debe tener ni palo mayor quinto, ni fallo, ni semi-fallo, ni dos o mas doubleton(puede tener uno)

# apertura de 2 a palo: 2T; 21 o mas puntos H+D
      # convencion es abrir siempre 2 Treboles (2T)
      # si la mano tuviese 21 puntos H y solo 20 puntos H+D(porque no tiene ningun As) no cumple con la condicion de 2 a palo y pasa

# apertura de 2 sin triunfo: 2ST;entre 21 y 23 puntos H, no se condideran los puntos H+D
      # ademas no debe tener palo mayor quinto, ni fallo, ni semi-fallo, ni dos o mas doubleton(puede tener uno) y debe tener los cuatro palos protegidos

# apertura 3 sin triunfo: 3ST; entre 24 y 26 puntos H, no se consideran los puntos H+D
      # ademas, no debe tener palo mayor quinto, ni fallo, ni semi-fallo, ni dos o mas doubleton(puede tener uno) y debe tener los cuatro palos protegidos
           
# apertura: list(Carta) -> str
# la funcion recibe una mano de un mazo y devuelve un string con la apertura correspondiente
# ya sea pass, '1T', '1D', '1C', '1P', '1ST', '2T', '2ST' o '3ST'
# ejemplo: apertura([AP, KP, QP, AC, QC, JC, AD, 3D, 2D, AT, 10T, 9T, 8T]) devuelve '1T'
def apertura(mano):
   H = puntosH(mano)
   HD = puntosHD(mano)
   valor = frecuencia_valor(mano)
   especiales = {'A':0,'K':0,'Q':0,'J':0}
   nuevo=dict(list(especiales.items()) + list(valor.items()))
   # Apertura de 3 Sin Triunfo
   if H >= 24 and H <= 26 and palo_mayor_quinto(mano) == 0 and fallo(mano) == 0 and semi_fallo(mano) == 0 and doubleton(mano) < 2 and protegido(mano) == 4:
      return '3ST'

   # Apertura de 2 Sin Triunfo
   elif H >= 21 and H <= 23 and palo_mayor_quinto(mano) == 0 and fallo(mano) == 0 and semi_fallo(mano) == 0 and doubleton(mano) < 2 and protegido(mano) == 4:
      return '2ST'
   
   # Apertura de 2 a palo
   if HD >= 21:
      return '2T'
   elif H == 21 and HD == 20 and nuevo['A'] == 0:
      pass
   
   # Apertura de 1 Sin Triunfo
   if (H >= 16 and H <= 18) and palo_mayor_quinto(mano) == 0 and fallo(mano) == 0 and semi_fallo(mano) == 0 and doubleton(mano) < 2:
      return '1ST'
   
   #Apertura de 1 a palo
   elif ((H >= 13 and H < 16) or (HD >= 14 and HD <= 20)) or (((H == 13 and HD == 12) or (H == 14 and HD == 13)) and nuevo['A'] == 0):
      if palo_mayor_quinto(mano) == 1:         # palo mayor quinto y misma cantidad de piques que de corazones, apertura '1P'
         return '1P'
      elif palo_mayor_quinto(mano) == 2:       # palo mayor quinto y mas cartas de piques que de corazones, apertura '1P'
         return '1P'
      elif palo_mayor_quinto(mano) == 4:       # palo mayor quinto y mas cartas de corazones que de piques, apertura '1C' 
         return '1P'
      elif palo_mayor_quinto(mano) == 3:       # palo mayor quinto para piques, apertura '1P'  
         return '1C'
      elif palo_mayor_quinto(mano) == 5:       # palo mayor quinto para corazones, apertura '1C'
         return '1C'
      elif palo_mayor_quinto(mano) == 0:       # no tiene palo mayor quinto, evalua para palo menor quinto
         if palo_menor_quinto(mano) == 1:      # si D = T = 3 cartas, misma cantidad de puntos honores para diamantes y treboles, apertura '1D'
            return '1D'
         elif palo_menor_quinto(mano) == 2:    # si D = T = 3 cartas, mas puntos honores para diamantes que treboles, apertura '1D'
            return '1D'
         elif palo_menor_quinto(mano) == 3:    # si D = T = 3 cartas, mas puntos honores para treboles que diamantes, apertura '1T'
            return '1T'
         elif palo_menor_quinto(mano) == 4:    # palo menor quinto y misma cantidad de diamantes que de treboles, apertura '1D'
            return '1D'
         elif palo_menor_quinto(mano) == 5:    # palo menor quinto y mas cartas de diamantes que de treboles, apertura '1D'
            return '1D'
         elif palo_menor_quinto(mano) == 6:    # palo menor quinto y mas cartas de treboles que de diamantes, apertura '1T'
            return '1T'
         elif palo_menor_quinto(mano) == 7:    # palo menor quinto para diamantes, apertura '1D'
            return '1D'
         elif palo_menor_quinto(mano) == 8:    # palo menor quinto para treboles, apertura '1T'
            return '1T'
   
   # No cumple condiciones Apertura
   else:
      pass
   
# procesarArchivo: str -> str
# la funcion recibe un string con el nombre de un archivo de texto
# y devuelve un string con la apertura correcta para cada mano en el archivo, una linea por mano
# cada linea del archivo contiene la informacion de una mano(mismo formato de los ejemplos)
# QP,8P,6P,4P,7C,3C,6D,4D,KT,QT,JT,10T,9T
# AP,QP,JP,10P,4P,2P,JC,6C,3C,KD,9D,AT,6T
# AP,10P,5P,QC,6C,AD,QD,10D,KT,JT,10T,9T,8T
# KP,QP,JP,9P,3P,QC,4C,2C,JD,8D,6D,KT,QT
# AP,AC,KC,8C,7C,6C,3C,QD,5D,AT,JT,9T,5T
# AP,KP,QP,AC,QC,JC,AD,3D,2D,AT,10T,9T,8T        
# para el archivo del ejemplo la funcion devuelve
# PASS\n1P\n1ST\n1P\n2T\n3ST\n
def procesarArchivo(lector):
   for linea in lector:
      linea = apertura(mano)
      lector = apertura(mano)
      return ('\n' + linea)

# leer y mostrar lineas de archivo
lector = open('procesarmano.txt','r')

# Test para apertura
mano = [Carta('A','P'),Carta('Q','P'),Carta('8','P'),Carta('5','P'),Carta('J','C'),Carta('7','C'),Carta('6','C'),Carta('K','D'),Carta('9','D'),Carta('3','D'),Carta('A','T'),Carta('J','T'),Carta('8','T')]
assert apertura(mano) == '1T'

mano = [Carta('Q','P'),Carta('8','P'),Carta('6','P'),Carta('4','P'),Carta('7','C'),Carta('3','C'),Carta('6','D'),Carta('4','D'),Carta('K','T'),Carta('Q','T'),Carta('J','T'),Carta('10','T'),Carta('9','T')]
assert apertura(mano) == None 

mano = [Carta('A','P'),Carta('Q','P'),Carta('J','P'),Carta('10','P'),Carta('4','P'),Carta('2','P'),Carta('J','C'),Carta('6','C'),Carta('3','C'),Carta('K','D'),Carta('9','D'),Carta('A','T'),Carta('6','T')]
assert apertura(mano) == '1P'

mano = [Carta('A','P'),Carta('10','P'),Carta('5','P'),Carta('Q','C'),Carta('6','C'),Carta('A','D'),Carta('Q','D'),Carta('10','D'),Carta('K','T'),Carta('J','T'),Carta('10','T'),Carta('9','T'),Carta('8','T')]
assert apertura(mano) == '1ST'

mano = [Carta('K','P'),Carta('Q','P'),Carta('J','P'),Carta('9','P'),Carta('3','P'),Carta('Q','C'),Carta('4','C'),Carta('2','C'),Carta('J','D'),Carta('8','D'),Carta('6','D'),Carta('K','T'),Carta('Q','T')]
assert apertura(mano) == '1P'

mano = [Carta('A','P'),Carta('A','C'),Carta('K','C'),Carta('8','C'),Carta('7','C'),Carta('6','C'),Carta('3','C'),Carta('Q','D'),Carta('5','D'),Carta('A','T'),Carta('J','T'),Carta('9','T'),Carta('5','T')]
assert apertura(mano) == '2T'

mano = [Carta('A','P'),Carta('K','P'),Carta('Q','P'),Carta('A','C'),Carta('Q','C'),Carta('J','C'),Carta('A','D'),Carta('3','D'),Carta('2','D'),Carta('A','T'),Carta('10','T'),Carta('9','T'),Carta('8','T')]        
assert apertura(mano) == '3ST'

mano = [Carta('4','D'),Carta('7','T'),Carta('Q','C'),Carta('8','C'),Carta('K','D'),Carta('A','D'),Carta('Q','D'),Carta('J','P'),Carta('10','P'),Carta('7','C'),Carta('J','C'),Carta('3','C'),Carta('J','T')] 
assert apertura(mano) == '1C'

# test clase carta
class TestCarta:

   def __init__(self):
      self.testcarta = Carta('10','P')

   def test(self):
      assert self.testcarta.getValor() == '10'
      assert self.testcarta.getPalo() == 'P'
      assert self.testcarta.string() == '10P'

# ejecucion del test
test = TestCarta()
test.test()

# Test para funciones auxiliares

mano = [Carta('A','P'),Carta('Q','P'),Carta('8','P'),Carta('5','P'),Carta('J','C'),Carta('7','C'),Carta('6','C'),Carta('K','D'),Carta('9','D'),Carta('3','D'),Carta('A','T'),Carta('J','T'),Carta('8','T')]
assert separar_mano_valores(mano) == ['A', 'Q', '8', '5', 'J', '7', '6', 'K', '9', '3', 'A', 'J', '8']
assert separar_mano_palos(mano) == ['P', 'P', 'P', 'P', 'C', 'C', 'C', 'D', 'D', 'D', 'T', 'T', 'T']
assert frecuencia_valor(mano) == {'A': 2, 'Q': 1, '8': 2, '5': 1, 'J': 2, '7': 1, '6': 1, 'K': 1, '9': 1, '3': 1}
assert frecuencia_palo(mano) == {'P': 4, 'C': 3, 'D': 3, 'T': 3}
assert puntosH(mano) == 15
assert fallo(mano) == 0
assert semi_fallo(mano) == 0
assert doubleton(mano) == 0
assert ases(mano) == 0
assert mas_de_cinco_en_un_palo(mano) == 0
assert puntosD(mano) == 0
assert puntosHD(mano) == 15
assert palo_mayor_quinto(mano) == 0
assert convertir_a_string_cada_elemento_de_la_mano(mano) == ['AP', 'QP', '8P', '5P', 'JC', '7C', '6C', 'KD', '9D', '3D', 'AT', 'JT', '8T']
assert frecuencia_mano(mano) == {'AP': 1, 'QP': 1, '8P': 1, '5P': 1, 'JC': 1, '7C': 1, '6C': 1, 'KD': 1, '9D': 1, '3D': 1, 'AT': 1, 'JT': 1, '8T': 1}
assert puntosH_diamantes_de_una_mano(mano) == 3
assert puntosH_treboles_de_una_mano(mano) == 5
assert palo_menor_quinto(mano) == 3
assert piques_protegido(mano) 
assert corazones_protegido(mano) 
assert diamantes_protegido(mano) 
assert treboles_protegido(mano) 
assert protegido(mano) == 4
assert apertura(mano) == '1T'

mano = [Carta('Q','P'),Carta('8','P'),Carta('6','P'),Carta('4','P'),Carta('7','C'),Carta('3','C'),Carta('6','D'),Carta('4','D'),Carta('K','T'),Carta('Q','T'),Carta('J','T'),Carta('10','T'),Carta('9','T')]
assert separar_mano_valores(mano) == ['Q', '8', '6', '4', '7', '3', '6', '4', 'K', 'Q', 'J', '10', '9']
assert separar_mano_palos(mano) == ['P', 'P', 'P', 'P', 'C', 'C', 'D', 'D', 'T', 'T', 'T', 'T', 'T']
assert frecuencia_valor(mano) == {'Q': 2, '8': 1, '6': 2, '4': 2, '7': 1, '3': 1, 'K': 1, 'J': 1, '10': 1, '9': 1}
assert frecuencia_palo(mano) == {'P': 4, 'C': 2, 'D': 2, 'T': 5}
assert puntosH(mano) == 8
assert fallo(mano) == 0
assert semi_fallo(mano) == 0
assert doubleton(mano) == 2
assert ases(mano) == -1
assert mas_de_cinco_en_un_palo(mano) == 0
assert puntosD(mano) == 1
assert puntosHD(mano) == 9
assert palo_mayor_quinto(mano) == 0
assert convertir_a_string_cada_elemento_de_la_mano(mano) == ['QP', '8P', '6P', '4P', '7C', '3C', '6D', '4D', 'KT', 'QT', 'JT', '10T', '9T']
assert frecuencia_mano(mano) == {'QP': 1, '8P': 1, '6P': 1, '4P': 1, '7C': 1, '3C': 1, '6D': 1, '4D': 1, 'KT': 1, 'QT': 1, 'JT': 1, '10T': 1, '9T': 1}
assert puntosH_diamantes_de_una_mano(mano) == 0
assert puntosH_treboles_de_una_mano(mano) == 6
assert palo_menor_quinto(mano) == 6
assert piques_protegido(mano) 
#assert corazones_protegido(mano) 
#assert diamantes_protegido(mano)
assert treboles_protegido(mano) 
assert protegido(mano) == 0
assert apertura(mano) == None

mano = [Carta('A','P'),Carta('Q','P'),Carta('J','P'),Carta('10','P'),Carta('4','P'),Carta('2','P'),Carta('J','C'),Carta('6','C'),Carta('3','C'),Carta('K','D'),Carta('9','D'),Carta('A','T'),Carta('6','T')]
assert separar_mano_valores(mano) == ['A', 'Q', 'J', '10', '4', '2', 'J', '6', '3', 'K', '9', 'A', '6']
assert separar_mano_palos(mano) == ['P', 'P', 'P', 'P', 'P', 'P', 'C', 'C', 'C', 'D', 'D', 'T', 'T']
assert frecuencia_valor(mano) == {'A': 2, 'Q': 1, 'J': 2, '10': 1, '4': 1, '2': 1, '6': 2, '3': 1, 'K': 1, '9': 1}
assert frecuencia_palo(mano) == {'P': 6, 'C': 3, 'D': 2, 'T': 2}
assert puntosH(mano) == 15
assert fallo(mano) == 0
assert semi_fallo(mano) == 0
assert doubleton(mano) == 2
assert ases(mano) == 0
assert mas_de_cinco_en_un_palo(mano) == 1
assert puntosD(mano) == 3
assert puntosHD(mano) == 18
assert palo_mayor_quinto(mano) == 2
assert convertir_a_string_cada_elemento_de_la_mano(mano) == ['AP', 'QP', 'JP', '10P', '4P', '2P', 'JC', '6C', '3C', 'KD', '9D', 'AT', '6T']
assert frecuencia_mano(mano) == {'AP': 1, 'QP': 1, 'JP': 1, '10P': 1, '4P': 1, '2P': 1, 'JC': 1, '6C': 1, '3C': 1, 'KD': 1, '9D': 1, 'AT': 1, '6T': 1}
assert puntosH_diamantes_de_una_mano(mano) == 3
assert puntosH_treboles_de_una_mano(mano) == 4
assert palo_menor_quinto(mano) == 0
assert piques_protegido(mano) 
assert corazones_protegido(mano) 
#assert diamantes_protegido(mano)
#assert treboles_protegido(mano) 
assert protegido(mano) == 0
assert apertura(mano) == '1P'

mano = [Carta('A','P'),Carta('10','P'),Carta('5','P'),Carta('Q','C'),Carta('6','C'),Carta('A','D'),Carta('Q','D'),Carta('10','D'),Carta('K','T'),Carta('J','T'),Carta('10','T'),Carta('9','T'),Carta('8','T')]
assert separar_mano_valores(mano) == ['A', '10', '5', 'Q', '6', 'A', 'Q', '10', 'K', 'J', '10', '9', '8']
assert separar_mano_palos(mano) == ['P', 'P', 'P', 'C', 'C', 'D', 'D', 'D', 'T', 'T', 'T', 'T', 'T']
assert frecuencia_valor(mano) == {'A': 2, '10': 3, '5': 1, 'Q': 2, '6': 1, 'K': 1, 'J': 1, '9': 1, '8': 1}
assert frecuencia_palo(mano) == {'P': 3, 'C': 2, 'D': 3, 'T': 5}
assert puntosH(mano) == 16
assert fallo(mano) == 0
assert semi_fallo(mano) == 0
assert doubleton(mano) == 1
assert ases(mano) == 0
assert mas_de_cinco_en_un_palo(mano) == 0
assert puntosD(mano) == 1
assert puntosHD(mano) == 17
assert palo_mayor_quinto(mano) == 0
assert convertir_a_string_cada_elemento_de_la_mano(mano) == ['AP', '10P', '5P', 'QC', '6C', 'AD', 'QD', '10D', 'KT', 'JT', '10T', '9T', '8T']
assert frecuencia_mano(mano) == {'AP': 1, '10P': 1, '5P': 1, 'QC': 1, '6C': 1, 'AD': 1, 'QD': 1, '10D': 1, 'KT': 1, 'JT': 1, '10T': 1, '9T': 1, '8T': 1}
assert puntosH_diamantes_de_una_mano(mano) == 6
assert puntosH_treboles_de_una_mano(mano) == 4
assert palo_menor_quinto(mano) == 6
assert piques_protegido(mano)
#assert corazones_protegido(mano)
assert diamantes_protegido(mano)
assert treboles_protegido(mano)
assert protegido(mano) == 0
assert apertura(mano) == '1ST'

#assert separar_mano_valores(mano) == 
#assert separar_mano_palos(mano) ==
#assert frecuencia_valor(mano) ==
#assert frecuencia_palo(mano) ==
#assert puntosH(mano) == 
#assert fallo(mano) ==
#assert semi_fallo(mano) == 
#assert doubleton(mano) ==
#assert ases(mano) ==
#assert mas_de_cinco_en_un_palo(mano) ==
#assert puntosD(mano) ==
#assert puntosHD(mano) ==
#assert palo_mayor_quinto(mano) ==
#assert convertir_a_string_cada_elemento_de_la_mano(mano) ==
#assert frecuencia_mano(mano) ==
#assert puntosH_diamantes_de_una_mano(mano) == 
#assert puntosH_treboles_de_una_mano(mano) ==
#assert palo_menor_quinto(mano) ==
#assert piques_protegido(mano) ==
#assert corazones_protegido(mano) ==
#assert diamantes_protegido(mano) ==
#assert treboles_protegido(mano) ==
#assert protegido(mano) ==
#assert apertura(mano) ==
