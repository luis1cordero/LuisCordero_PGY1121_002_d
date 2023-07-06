import numpy as np

def llenar(arreglo):
    x=0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if len(str(x))<2:
                arreglo[f][c]='0'+str(x)
            else:
                arreglo[f][c] = str(x)

def mostrar(arreglo):
    for f in range(10):
        fila = ''
        for c in range(10):
            if c == 2:
                fila = fila +' | | '+arreglo[f][c]
            else:
                fila = fila + ' | ' + arreglo[f][c]
        print(fila)

def comprar(arreglo,num_asiento):
    x =0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if str(x) == str(num_asiento):
                arreglo[f][c]='XX'
def comprobarLugar(arreglo,num_asiento):
    x =0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if str(x) == str(num_asiento):
                if arreglo[f][c]=='XX':
                    return False
    return True