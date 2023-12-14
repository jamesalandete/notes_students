import main as Imain

Imain.add_header_to_file()
Imain.read_students_from_file()

# DECLARAMOS EXIT EN TRUE
exit = True
while exit:
    # LLAMAMOS FUNCION DE PRINT PARA EL MAIN
    Imain.main()
    # Capturamos la opcion seleccionada
    opcion = int(input("Ingrese la opcion a realizar: "))
    # Si la opcion es 1 se registra el estudiante
    if opcion == 1:
        # Se declara variable condicional el true
        valid = True
        # Se recorrera siempre y cuando "valid" sea True
        while valid:
            # Se utiliza funcion externa para requerir y validar tipo documento
            validOpcion = Imain.type_documents()
            if(validOpcion['return'] == False): continue
            number_document = input("\nIngrese numero de documento de estudiante: ")
            full_name = input("\nIngrese nombre completo de estudiante: ")
            phone_number = input("\nIngrese numero de celular de estudiante: ")
            full_name = ' '.join(word.capitalize() or ' ' for word in full_name.split(' '))
            Imain.new_student(str(validOpcion['type_document']), number_document, full_name, phone_number)
            enter = input("\nEscriba 'Salir' para terminar o 'Nuevo' para ir al inicio: ")
            if(enter.lower() == "salir"):
                valid = False

    elif opcion == 2:
        Imain.print_student_table(0)
        Imain.updateStudent()
    elif opcion == 3:
        Imain.new_note_student()
    elif opcion == 4:
        Imain.average_student('max')
    elif opcion == 5:
        Imain.average_student('min')
    elif opcion == 6:
        Imain.average_general()
    else:
        print("Escoja una opcion valida")
        enter = input("Escriba 'Salir' para terminar o 'Volver' para ir al inicio: ")
        if(enter.lower() == "salir"):
            exit = False
        else:
            continue
