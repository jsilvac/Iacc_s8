from funciones import cargaJson, muestraTabla, ingresaNewMedicamento, modificaMedicamento,validaInputStr, validaInputInt

medicamentos = cargaJson()

muestraTabla(medicamentos)

while True:

    print('\n       ***** MENU *****')
    op = validaInputStr('Si desea agregar(A) o modificar cantidad(M) inventario?\n:')
    resp = ''


    def switch_case(op):

        if op == 'm' or op == 'M':
            print('la opción que ha elegido es modificar\n')

            cod = validaInputStr('Ingresa el código de 4 dígitos del elemento a modificar\n:')

            cant = validaInputInt('Ingresa la nueva cantidad del producto\n:')

            print(f'Se ha modificado el elemento código ${cod}, cuya cantidad ahora es de ${cant} \n')

            modificaMedicamento(cod,cant)
            medi = cargaJson()
            muestraTabla(medi)

        elif op == 'a' or op == 'A':
            print('La opcion elegida es la de Agregar\n')

            cod = validaInputStr('Ingrese el codigo del producto\n:')
            nom = validaInputStr('Ingrese el nombre del Producto\n:')
            cant = validaInputInt('Ingrese la cantidad de medicamnetos almacenados\n:')

            ingresaNewMedicamento(cod,nom,cant)

            medi = cargaJson()
            muestraTabla(medi)
        else:
            print('La opción es incorrecta !')


    switch_case(op)

    resp = validaInputStr('Deseas continuar S/N\n:')
    if resp.lower() != 's':
        print('Programa finalizado...')
        break
