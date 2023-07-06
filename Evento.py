import numpy as np
from funciones import *
from espectador import *

arreglo = np.full((10, 10), '---')
lista_asistentes = []
ciclo = True


def agregarAsistente(lista_asistentes,num_asiento):
    a = espectador()

    a.rut = int(input("Ingrese rut:"))
    a.nombre = input("Ingrese nombre:")
    a.apellido = input("Ingrese apellido:")
    a.edad = int(input("Ingrese Edad:"))
    a.num_asiento = num_asiento
    if num_asiento>=1 and num_asiento<=20:
        a.valor=120000
    if num_asiento>=21 and num_asiento<=50:
        a.valor=80000
    if num_asiento>=51 and num_asiento<=100:
        a.valor=50000
    print("Operacion realizada exitosamente")
    lista_asistentes.append(a)



def comprarEntrada(arreglo,lista_asistentes):
    try:
        lugar = int(input("Ingrese cantidad de asistentes (1-3)"))
        if lugar>=1 and lugar<=3:
            compra=0
            while compra<lugar:
                print("|                    ESCENARIO                      |")
                mostrar(arreglo)
                num_asiento = int(input("Numero de Asiento:"))
                if num_asiento >= 1 and num_asiento <= 100:
                    disponible = comprobarLugar(arreglo, num_asiento)
                    if disponible == True:
                        agregarAsistente(lista_asistentes, num_asiento)
                        comprar(arreglo,num_asiento)
                        compra = compra + 1
                    else:
                        print("Asiento no disponible,seleccione otro")
                else:
                    print("solo asientos del 1 al 100")
        else:
            print("ubicaciones entre 1 y 3")
    except BaseException as error:
        print(f"Error:{error}")


def salir():
    print("Gracias por su uso")
    return False


llenar(arreglo)


def lstadoAsistent(lista_asistentes):
    for a in lista_asistentes:
        print(f"Nombre:{a.nombre} {a.apellido}\n Valor: ${a.valor} Lugar:{a.num_asiento}")


def Gtotales(lista_asistentes):
    platino=0
    gold=0
    silver=0
    tot_p=0
    tot_g=0
    tot_s=0
    for asi in lista_asistentes:
        if int(asi.valor) == 120000:
            platino = platino + 1
            tot_p = tot_p +  120000
        if int(asi.valor) == 80000:
            gold = gold + 1
            tot_g = tot_g + 80000
        if int(asi.valor) == 50000:
            silver = silver + 1
            tot_s = tot_s + 50000
    print(f"Vip: Cantidad:{platino} Total: ${tot_p}")
    print(f"Med: Cantidad:{gold} Total: ${tot_g}")
    print(f"Bas: Cantidad:{silver} Total: ${tot_s}")
    print(f"Total: ${tot_s+tot_g+tot_p}")


while ciclo:
    print("Eventos 'Creativos.cl'")
    print("1) Comprar entradas")
    print("2) Mostrar ubicaciones disponibles")
    print("3) Ver lsitado de asistentes")
    print("4) Mostrar ganancias totales")
    print("5) Salir")
    op = int(input("Ingrese su seleccion: "))
    try:
        match op:
            case 1:
                comprarEntrada(arreglo,lista_asistentes)
            case 2:
                mostrar(arreglo)
            case 3:
                lstadoAsistent(lista_asistentes)
            case 4:
                Gtotales(lista_asistentes)
            case 5:
                ciclo = salir()
    except BaseException as error:
        print(f"Error:{error}")