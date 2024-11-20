class Empleado:
    def __init__(self, nombre, id_empleado):
        self.__nombre = nombre
        self.__id_empleado = id_empleado

    def __str__(self):
        return (f'El nombre del empleado es: {self.__nombre}  \n'
                f'El Id del empleado es: {self.__id_empleado}')




def main():
    try:
        nombre_empleado_1 = input('Ingrese el nombre del empleado: ')
        Id_empleado = int(input('Ingrese el Id del empleado: '))

        empleado_1 = Empleado(nombre_empleado_1, Id_empleado)

        print(empleado_1)

    except ValueError:
        print('Error: Entrada inválida para alguno de los datos solicitados.')



if __name__ == '__main__':
    main()


