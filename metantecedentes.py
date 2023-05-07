import os
from tabulate import tabulate
from colorama import Fore, init
from  random import randrange, choice
init(autoreset=True) 
os.system('cls')

def opciones():
    correcto=False
    num=0
    while correcto == False:
        try:
            num = int(input("Introduce tu opción: "))
            correcto=True
        except:
            print('¡¡ERROR!!: Solo introduce números')   
    return num
pass

def Prueba():
    InPrueba = True
    while InPrueba:
        print('opciones 1 y 2')
        op = opciones()
        if op == 1:
            print('puto1')
        elif op ==2:
            print('correcto')
            InPrueba = False


usuarios = [ 
        ["Rober Gomez", 'Matanza', "No","NO","NO"],
        ["Rober", 'Matanza', "No","NO","NO"]
    ]

def computer():
    print('_______________________________________________________________________  ')
    print('                                                                       \ ')
    print(' __________________________________________________________________     |')
    print('|                                                                  |    |')
    print('|   C:\ Users\ FBI\ Agentes \Jimmy007> Antecedentes_               |    |')
    print('|                                                                  |    |')
    print(tabulate(usuarios,headers=["NOMBRE"," DELITO","EN BUSQUEDA","VIVO","EN CARCEL  "],tablefmt='fancy_grid'),'   |')
    print('|                                                                  |    |')
    print('|                                                                  |    |')
    print('|                                                                  |    |')
    print('|                                                                  |    |')
    print('|__________________________________________________________________|    |')
    print('                                                                        |')
    print('_______________________________________________________________________/')
    print('                  \___________________________________/')
    print('               ___________________________________________')
    print('           _- .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_')
    print('         _- .-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_')
    print('      _- .-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_')
    print('   _- .-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_')
    print('  _- .-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_')
    print(':-------------------------------------------------------------------------:')
    print('`---._.-------------------------------------------------------------._.---- ')

inventario = [
        ['Cuchillo', 10],          #inventario[0] Cuchillo
        ['Martillo', 0],          #inventario[1] Martillo
        ['Balas', 0],             #inventario[2] Balas
        ['Revolver', 0],          #inventario[3] Revolver
        ['Tenedor', 0]            #inventario[4] Ácido
]

alo = randrange(3)
print(alo)
"""
contador = -1
name = input('nombre: ')
for x in usuarios:
    contador += 1   
    if name in usuarios[contador]:
        print('funciona')
        break
    else:
        print('none')"""

    
"""
usuario = input('Ingrese su nombre de Usuario: ')
if usuario in usuarios:
    print('correcto')
else:
    print('mmm')"""
        

"""print(inventario[7][1])
nombre = input('nombre sujeto: ')
razon = input('razon: ')
encontrado = input('en busqueda?: ')"""
"""
#listaxatrapar.append([nombre,razon,encontrado])
nombre=input('agrega: ')
if nombre in inventario[0]:
    print('hola')
else:
    print('Usuario no encontrado!\n')

print(tabulate(listaxatrapar, headers=["NOMBRE","DELITO","EN BUSQUEDA","VIVO","ENCARCELADO"],tablefmt='fancy_grid'))
print(tabulate(inventario, headers=["OBJETO","CANTIDAD"],tablefmt='fancy_grid'))

if inventario[0][0] == 'Cuchillo':
    print('funciona')

InPRUEBA2 = True
while InPRUEBA2:
    Prueba()
    print('BACAN')
    InPRUEBA2 = False"""