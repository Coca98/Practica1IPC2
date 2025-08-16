from LibroDigital import LibroDigital
from LibroFisico import LibroFisico

def informacion(materialbiblioteca):
    print(materialbiblioteca.informacion())




#libros_fisicos = []
#libros_digitales = []

if __name__ == "__main__":
    
    i = 0
    j = 0
    while(True):
        print("Biblioteca")
        print("Seleccione una opcion")
        print("1. Registrar Libro")
        print("2. Gestionar Libro")
        print("3. Salir")
        entrada = input("Ingrese una opcion: ")
        if entrada == "1":
            print("Registrar Libro")
            print("1. Libro Fisico")
            print("2. Libro Digital")
            print("3. Regresar")
            print("Seleccione una Opcion")
            entrada_libro = input("Ingrese tipo de libro: ")
            while (True):
                if entrada_libro == "1":
                    print("Registrar Libro Fisico")
                    titulo= input("Ingrese el titulo del libro: ")
                    autor= input("Ingrese el autor del libro: ")
                    codigo= i+1
                    ejemplar=j+1
                    estado="disponible"
                    libro_fisico = LibroFisico(titulo, autor,codigo, ejemplar, estado)
                    print("Libro Creado")
                    break
                elif entrada_libro == "2":
                    print("Registrar Libro Digital")
                    titulo= input("Ingrese el titulo del libro: ")
                    autor= input("Ingrese el autor del libro: ")
                    codigo= i+1
                    tamano=input("Ingrese el tamaño del libro en MB: ")                   
                    estado="disponible"
                    libro_digital = LibroDigital(titulo, autor, codigo, tamano, estado)
                    print("Libro Digital Creado con exito")
                    break
                elif entrada_libro == "3":
                    break
                else:
                    print("Opcion no valida")
                    entrada_libro = input("Ingrese tipo de libro: ") 
        elif entrada == "2":
            print("Gestionar Libro")
            print("1. Informacion del libro  ")
            print("2. Modificar el estado del libro")
            print("3. Regresar")
            entrada_gestion=input("Ingrese una opcion: ")
            while True:
                if entrada_gestion == "1":
                    print("Informacion del libro")
                    print("Ingrese el titulo del libro")
                    aux_titulo = input("Titulo: ")
                    print("Ingrese el autor del libro")
                    aux_autor = input("Autor: ")
                    # Mostrar informacion del libro
                    if isinstance(libro_fisico, LibroFisico) and libro_fisico.getTitulo() == aux_titulo and libro_fisico.getAutor() == aux_autor:
                        informacion(libro_fisico)
                        break
                    elif isinstance(libro_digital, LibroDigital) and libro_digital.getTitulo() == aux_titulo and libro_digital.getAutor() == aux_autor:
                        informacion(libro_digital)
                        break
                    else:
                        print("Libro no encontrado")
                elif entrada_gestion == "2":
                    print("Modificar el estado del libro")
                    print("1. Prestar Libro")
                    print("2. Devolver Libro")
                    print("3. Regresar")
                    entrada_prestamo_libro=input("seleccione una opcion")
                    if entrada_prestamo_libro == "1":
                        print("Desea prestar un libro..?")
                        print("1. Si")
                        print("2. No")
                        entrada_confirmacion=input("Seleccione una opcion")
                        if entrada_confirmacion == "1":
                            print("Informacion del libro")
                            print("Ingrese el titulo del libro")
                            aux_titulo = input("Titulo: ")
                            print("Ingrese el autor del libro")
                            aux_autor = input("Autor: ")
                            if isinstance(libro_fisico, LibroFisico) and libro_fisico.getTitulo() == aux_titulo and libro_fisico.getAutor() == aux_autor:
                                #informacion(libro_fisico)
                                print("Ingrese el nuevo estado del libro")
                                nuevo_estado = "Ocupado"
                                libro_fisico.setEstado(nuevo_estado)
                                print( "Libro prestado con exito")
                                break
                            elif isinstance(libro_digital, LibroDigital) and libro_digital.getTitulo() == aux_titulo and libro_digital.getAutor() == aux_autor:
                                #informacion(libro_digital)
                                print("Ingrese el nuevo estado del libro")
                                nuevo_estado = "Ocupado"
                                libro_digital.setEstado(nuevo_estado)
                                print("Libro prestado con exito")
                                break
                            else:
                                print("Libro no encontrado")
                        elif entrada_confirmacion == "2":
                            print("Prestamo cancelado")
                        else:
                            print("Opcion no valida")
                            break
                    elif entrada_prestamo_libro == "2":
                        print("Desea devolver un libro..?")
                        print("1. Si")
                        print("2. No")
                        entrada_confirmacion=input("Seleccione una opcion:")
                        if entrada_confirmacion == "1":
                            print("Informacion del libro")
                            print("Ingrese el titulo del libro")
                            aux_titulo = input("Titulo: ")
                            print("Ingrese el autor del libro")
                            aux_autor = input("Autor: ")
                            if isinstance(libro_fisico, LibroFisico) and libro_fisico.getTitulo() == aux_titulo and libro_fisico.getAutor() == aux_autor:
                                #informacion(libro_fisico)
                                #print("Ingrese el nuevo estado del libro")
                                nuevo_estado = "Disponible"
                                libro_fisico.setEstado(nuevo_estado)
                                break
                            elif isinstance(libro_digital, LibroDigital) and libro_digital.getTitulo() == aux_titulo and libro_digital.getAutor() == aux_autor:
                                #informacion(libro_digital)
                                print("Ingrese el nuevo estado del libro")
                                nuevo_estado = "Disponible"
                                libro_digital.setEstado(nuevo_estado)
                                break
                            else: 
                                print("Libro no encontrado")
                        elif entrada_confirmacion == "2":
                            print("Devolucion cancelada")
                            
                        else:
                            print("Opcion no valida")
                            break
                    else:
                        break
                    # Modificar estado del libro
                elif entrada_gestion == "3":
                    break
                else:
                    print("Opcion no valida")
        elif entrada == "3":
            print("Salir")
            break
        else:
            print("Opcion no valida")