import os
from tabulate import tabulate
listStudents = {}
newCode = 1
student_selected=0
 # Se mantiene en un diccionario los tipos de documentos
types = {
    1: "CEDULA DE CIUDADANIA",
    2: "TARJETA DE IDENTIDAD"
}
headers = ['Code', 'Type Document', 'Number Document', 'Full Name', 'Phone Number', 'Note 1', 'Note 2', 'Note 3', 'Average']

# ----->    initial load
def add_header_to_file():
  global headers
  file_exists = os.path.isfile('students.txt')
  if not file_exists or os.stat('students.txt').st_size == 0:
    with open('students.txt', 'w') as f:
      f.write(','.join(headers)+'\n')

def read_students_from_file():
  """
  Lee los estudiantes del archivo de texto y los carga en el diccionario.
  """
  global newCode
  lastCode = 0
  row = 0
  with open('students.txt', 'r') as f:
    for line in f:
        if(row == 0):
            row += 1
            continue
        student_data = line.strip().split(',')
        student_key = int(student_data[0])
        student_info = {
            'code': student_key,
            'type_document': student_data[1],
            'number_document': student_data[2],
            'full_name': student_data[3],
            'phone_number': student_data[4],
            'note_1': student_data[5],
            'note_2': student_data[6],
            'note_3': student_data[7],
            'average':  student_data[8]
        }
        listStudents[student_key] = student_info
        lastCode = int(student_data[0])
    newCode = lastCode + 1
    print(listStudents)


def main():
  print('*****************************************************')
  print('***************** MENÚ PRINCIPAL ********************\n')
  print('\t1 - REGISTRAR ESTUDIANTE	        ')
  print('\t2 - CONSULTAR ESTUDIANTES        ')
  print('\t3 - ASIGNAR NOTA A ESTUDIANTE    ')
  print('\t4 - PROMEDIO MAS ALTO    ')
  print('\t5 - PROMEDIO MAS BAJO    ')
  print('\t6 - PROMEDIO GENERAL    ')
  print('\t7 - ELIMINAR ESTUDIANTE    ')
  print('\n*****************************************************')
  print('*****************************************************')

# ----->    Type documents
def type_documents():
    # Se lista los tipos de documentos
    print('*****************************************************')
    print('***************** TIPOS DE DOCUMENTOS ********************\n')
    print('\t1 - CEDULA DE CIUDADANIA       ')
    print('\t2 - TARJETA DE IDENTIDAD       ')
    print('\n*****************************************************')
    print('*****************************************************')
    # Se requiere ingresar el tipo documento
    documento = int(input("Ingrese la opcion del tipo de documento: "))
    # Se utiliza funcion para validar el tipo documento ingresado
    return {"return": validate_type_documents(documento), "type_document": documento}

def type_document_description(id):
    global types
    description = types[id]
    return description

def validate_type_documents(clave):
    global types
    # Se valida si el documento recibido por parametro existe en el diccionario
    if clave in types:
        return True
    else:
        print('\nEl tipo documento {clave} no existe')
        return False

# ----->    students information
def new_student(type_document, number_document, full_name, phone_number):
    global newCode
    # student_key = type_document + '_' + number_document
    student_data = {
        'code': int(newCode),
        'type_document': type_document,
        'number_document': number_document,
        'full_name': full_name,
        'phone_number': phone_number,
        'note_1': 0,
        'note_2': 0,
        'note_3': 0,
        'average': 0
    }
    listStudents[newCode] = student_data
    saveStudents(newCode, student_data)
    print_student_table(0)
    newCode = newCode + 1

def updateStudent():
    global student_selected
    enter = input('\nDesea editar algun estudiante ?, Ingrese "Si" para editar o presine "Enter" para continuar: ')
    if(enter.lower() == 'si'):
        code = int(input('\nIngrese Codigo "Code" del estudiante a editar, solo numeros: '))
        if code in listStudents:
            for k in listStudents.keys():
                if(int(k) == code): student_selected = int(k)
            student = listStudents[code]
            print_student_table(code)
            print('\n*************** Modificacion de estudiante *******************')
            print('Se mostrara informacion del estudiante por cada campo.')
            print('Solo si desea modificar la informacion existe, ingrese nueva informacion y presione "Enter".')
            print('Si no desea modificar ninguna informacion de ese campo, presionar solamente "Enter" y pasara a la siguiente.')
            print('*************** Modificacion de estudiante *******************\n')
            name = input('Nombre de estudiante actual : '+student['full_name']+ ' ')
            if name != '': listStudents[code]['full_name'] = name

            phone_number = input('Celular del estudiante actual : '+student['phone_number']+ ' ')
            if phone_number != '': listStudents[code]['phone_number'] = phone_number

            line_modify(student_selected, listStudents[code])
            input('Modificado con exito, presione "Enter" para continuar...')

def new_note_student():
    global student_selected
    print_student_table(0)
    codeStudent = int(input('\nIngrese el "Code" del estudiante, solo numeros: '))
    if codeStudent in listStudents:
        for k in listStudents.keys():
            if(int(k) == codeStudent): student_selected = int(k)

        print_student_table(codeStudent)
        note1 = float(input("\nIngrese la nota #1: "))
        note2 = float(input("\nIngrese la nota #2: "))
        note3 = float(input("\nIngrese la nota #3: "))
        average = round((note1 + note2 + note3) / 3, 2)
        print("\nEl promedio del estudiante es: ", average)
        listStudents[codeStudent]['note_1'] = note1
        listStudents[codeStudent]['note_2'] = note2
        listStudents[codeStudent]['note_3'] = note3
        listStudents[codeStudent]['average'] = average
        print(student_selected)
        line_modify(student_selected, listStudents[codeStudent])
        print_student_table(codeStudent)
        input('\nPresione "Enter" para continuar...')
    else:
        print('\nEl estudiante no se encuentra registrado')
        input("\nEnter para realizar nueva busqueda")

def saveStudents(student_key, student_data):
      # Save student data to a text file
  with open('students.txt', 'a') as f:
      f.write(f"{student_key},{student_data['type_document']},{student_data['number_document']},{student_data['full_name']},{student_data['phone_number']},{student_data['note_1']},{student_data['note_2']},{student_data['note_3']},{student_data['average']}\n")

# -----> Promedio
def average_student(option):
    if option.lower() == 'max':
        student = max(listStudents.values(), key=lambda x: x['average'])
    else:
        student = min(listStudents.values(), key=lambda x: x['average'])
    print_student_table(student['code'])
    input("\nEste es el estudiante requerido, presione enter para continuar")

def average_general():
    promedios = [float(student['average']) for student in listStudents.values() if student['average'].replace('.', '', 1).isdigit()]

    general_average = sum(promedios) / len(promedios) if len(promedios) > 0 else 0

    print("\nPromedio general de todos los estudiantes:", round(general_average,2))
    input("\nPresione Enter para continuar...")
# ----->    utils
def print_student_table(filter):
    global headers
    table_data = []
    if(filter == 0):
        for student_key, student_info in listStudents.items():
            typeDocument = type_document_description(int(student_info['type_document']))
            row_data = [student_info['code'], typeDocument,  student_info['number_document'], student_info['full_name'], student_info['phone_number'],student_info['note_1'],student_info['note_2'],student_info['note_3'],student_info['average']]
            table_data.append(row_data)
    else:
        student = listStudents[filter]
        typeDocument = type_document_description(int(student['type_document']))
        row_data = [student['code'], typeDocument, student['number_document'], student['full_name'], student['phone_number'],student['note_1'],student['note_2'],student['note_3'], student['average']]
        table_data.append(row_data)

    print(tabulate(table_data, headers=headers, tablefmt='fancy_grid'))

def line_modify(number_line, student_data):
    number_line = int(number_line) - 1
    if(number_line == 0): number_line = 1
    new_information = f"{student_data['code']},{student_data['type_document']},{student_data['number_document']},{student_data['full_name']},{student_data['phone_number']},{student_data['note_1']},{student_data['note_2']},{student_data['note_3']},{student_data['average']}\n"
    with open('students.txt', 'r') as file:
        lines = file.readlines()
    number_line = int(number_line)
    lines[number_line] = new_information

    with open('students.txt', 'w') as file:
        file.writelines(lines)

def deleteStudent():
    global student_selected

    print_student_table(0)
    codeStudent = int(input("Ingrese codigo del estudiante a eliminar: "))
    if codeStudent in listStudents:
        for k in listStudents.keys():
            if(int(k) == codeStudent): student_selected = int(k)
    new_file = "temp.txt"
    try:
        student_data = listStudents[codeStudent]
        line_delete = f"{student_data['code']},{student_data['type_document']},{student_data['number_document']},{student_data['full_name']},{student_data['phone_number']},{student_data['note_1']},{student_data['note_2']},{student_data['note_3']},{student_data['average']}\n"
        # Lee el archivo y escribe las líneas que no deseas eliminar en el nuevo archivo
        with open('students.txt', 'r') as original_file, open(new_file, 'w') as file_new:
            for line in original_file:
                print(line)
                if line != line_delete:
                    file_new.write(line)

        # Renombra el nuevo archivo para que tenga el mismo nombre que el original
        os.replace(new_file, 'students.txt')
        del listStudents[codeStudent]
        print(f" Estudiante eliminado.")
        input('Presione "Enter" para continuar...')
    except FileNotFoundError:
        print(f"El archivo 'students.txt' no existe.")
    except Exception as e:
        print(f"Error al intentar eliminar la línea: {e}")