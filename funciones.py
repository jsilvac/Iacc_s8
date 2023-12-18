
# se precisa para mejor visualizacion y ejecucion del programa
# instalkar e importar las librerias de prettytable y colorama

import json
from prettytable import PrettyTable
from colorama import Fore, Style

medicamentos = [
    {'codigo': 'M001', 'nombre': 'Paracetamol', 'cantidad': 432, 'pedir': 0},
    {'codigo': 'M002', 'nombre': 'Ibuprofeno', 'cantidad': 1432, 'pedir': 0},
    {'codigo': 'M003', 'nombre': 'Omeprazol', 'cantidad': 1002, 'pedir': 0},
    {'codigo': 'M004', 'nombre': 'Amoxicilina', 'cantidad': 876, 'pedir': 0},
    {'codigo': 'M005', 'nombre': 'Aspirina', 'cantidad': 1000, 'pedir': 0},
    {'codigo': 'M006', 'nombre': 'Atorvastatina', 'cantidad': 1121, 'pedir': 0},
    {'codigo': 'M007', 'nombre': 'Losartan', 'cantidad': 299, 'pedir': 0},
    {'codigo': 'M008', 'nombre': 'Metformina', 'cantidad': 998, 'pedir': 0},
    {'codigo': 'M009', 'nombre': 'Simvastatina', 'cantidad': 789, 'pedir': 0},
    {'codigo': 'M010', 'nombre': 'Diazepam', 'cantidad': 990, 'pedir': 0}
]


def cargaJson():
    nombre_archivo = 'medicamentos.json'

    try:
        with open(nombre_archivo, 'r') as archivo:
            medicamentos_cargados = json.load(archivo)
            print(medicamentos_cargados)
            return medicamentos_cargados
    except FileNotFoundError:
        with open(nombre_archivo, 'w') as archivo:
            json.dump(medicamentos, archivo, indent=2)
            print(medicamentos)
            return medicamentos


def muestraTabla(medicamentos):

    tabla_medicamentos = PrettyTable()

    tabla_medicamentos.field_names = ['Codigo', 'Nombre', 'Cantidad', 'A pedir']

    for med in medicamentos:
        codigo = med['codigo']
        nombre = med['nombre']
        cantidad = int(med['cantidad'])
        pedir = int(med['pedir'])

        color = Fore.BLUE if cantidad > 1000 else Fore.RED

        pedir = 0 if cantidad > 1000 else 1000 - cantidad

        tabla_medicamentos.add_row([color + codigo, color + nombre, color + str(cantidad), pedir])

    print(Style.BRIGHT + tabla_medicamentos.get_string(), '\n')


def ingresaNewMedicamento(cod, nom, cant):

    nombre_archivo = 'medicamentos.json'

    try:
        with open(nombre_archivo, 'r+') as archivo:

            medicamentos = json.load(archivo)

            nuevo_medicamento = {
                'codigo': cod,
                'nombre': nom,
                'cantidad': cant,
                'pedir': 0
            }
            medicamentos.append(nuevo_medicamento)

            archivo.seek(0)

            json.dump(medicamentos, archivo, indent=2)

            archivo.truncate()

    except FileNotFoundError:

        medicamentos = [{
            'codigo': cod,
            'nombre': nom,
            'cantidad': cant,
            'pedir': 0
        }]
        with open(nombre_archivo, 'w') as archivo:
            json.dump(medicamentos, archivo, indent=2)

    print("Medicamento agregado")


def modificaMedicamento(cod, valor):
    nombre_archivo = 'medicamentos.json'

    try:
        with open(nombre_archivo, 'r') as archivo:
            medicamentos = json.load(archivo)

        for medicamento in medicamentos:
            if medicamento['codigo'] == cod:
                medicamento['cantidad'] = valor
                print(f'Cantidad del medicamento con código {cod} ha sido modificada.')
                break  # Rompe el bucle después de la modificación
        else:
            print(f'No se encontró el medicamento con el código {cod}')
            return  # Sale de la función si el medicamento no se encuentra

        with open(nombre_archivo, 'w') as archi:
            json.dump(medicamentos, archi, indent=2)

    except FileNotFoundError:
        print('El archivo no pudo ser cargado')
    except json.JSONDecodeError:
        print('Error al decodificar el archivo JSON')


def validaInputStr(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada:
            return entrada
        else:
            print("¡Error! Debes ingresar un valor no vacío.")


def validaInputInt(mensaje):
    while True:
        entrada =input(mensaje)
        try:
            numero = int(entrada)
            return numero
        except ValueError:
                print("¡Error! Debes ingresar un valor no vacío.")