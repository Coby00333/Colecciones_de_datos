import pandas as pd
import os

# Función para mostrar el menú principal
def mostrar_menu():
    print("¡Bienvenido al gestor de horarios de cursos!")
    print("\nPor favor, selecciona una opción:")
    print("1. Crear una nueva clase")
    print("2. Crea un nuevo curso")
    print("3. Eliminar clase de un curso")
    print("4. Mostrar horario de un curso")
    print("5. Salir")

# Función para agregar una nueva clase a un curso existente
def agregar_clase():
    nombre_curso = input("Ingresa el nombre del curso: ")
    nombre_archivo = nombre_curso
    
    # Verificar si el archivo del curso existe
    if not os.path.isfile(nombre_curso):
        print("El nombre del curso ingresado no existe. Por favor, intenta de nuevo.")
        return

    print("¡Vamos a crear una nueva clase!")
    nombre = input("Ingresa el nombre de la clase: ")
    while True:
        dia_numero = input("Ingresa el día de la semana (1 al 7): ")
        if dia_numero in ["1", "2", "3", "4", "5", "6", "7"]:
            break
        else:
            print("Número de día no válido. Por favor, ingresa un número del 1 al 7.")
            
    hora = input("Ingresa la hora de la clase: ")
    dias_semana = {
        "1": "Lunes",
        "2": "Martes",
        "3": "Miércoles",
        "4": "Jueves",
        "5": "Viernes",
        "6": "Sábado",
        "7": "Domingo"
    }
    dia = dias_semana.get(dia_numero)

    df = pd.read_csv(nombre_archivo)
    codigo = len(df) + 1
    
    nuevo_registro = pd.DataFrame({"codigo": [codigo], "nombre_clase": [nombre], "dia": [dia], "hora": [hora]})
    df = pd.concat([df, nuevo_registro])
    
    df.to_csv(nombre_archivo, index=False) 
    print("¡Nueva clase agregada exitosamente!")

# Función para crear un nuevo curso
def crear_nuevo_curso():
    print("¡Vamos a crear un nuevo curso!")
    nombre_curso = input("Ingresa el nombre del curso: ")
    
    # Crear el nombre del archivo a partir del nombre del curso
    nombre_archivo = f"{nombre_curso}.csv"
    
    # Crear un DataFrame (df) vacío con las columnas requeridas 
    df_dict = pd.DataFrame(columns=["codigo_curso", "nombre"])
   
    # Leer el archivo CSV existente
    df_dict = pd.read_csv("diccionario.csv")
    
    # Asignar automáticamente un valor único al código del curso
    codigo_curso = len(df_dict) + 1
    mensaje_codigo = f"Codigo del curso: {codigo_curso}"
    print(mensaje_codigo)
    
    # Agregar los nuevos datos al DataFrame del diccionario
    nuevo_registro_dict = pd.DataFrame({"codigo_curso": [mensaje_codigo], "nombre": [nombre_curso]})
    df_dict = pd.concat([df_dict, nuevo_registro_dict])
    
    # Guardar los cambios en el archivo CSV del diccionario
    df_dict.to_csv("diccionario.csv", index=False) 

   
    # Crear un DataFrame vacío con las columnas requeridas
    df_curso = pd.DataFrame(columns=["codigo", "nombre_curso", "dia", "hora"])
    
    # Agregar los nuevos datos al DataFrame del curso
    nuevo_registro_curso = pd.DataFrame({"codigo": [mensaje_codigo], "nombre_curso": [nombre_curso], "dia": [""], "hora": [""]})
    df_curso = pd.concat([df_curso, nuevo_registro_curso])
    
    # Guardar los cambios en el archivo CSV del curso
    df_curso.to_csv(nombre_archivo, index=False) 
    print("¡Nuevo curso creado exitosamente!")

# Función para eliminar una clase de un curso existente
def eliminar_clase():
    nombre_curso = input("Ingresa el nombre del curso: ")
    nombre_archivo = nombre_curso
    
    # Verificar si el archivo del curso existe
    if not os.path.isfile(nombre_curso):
        print("El nombre del curso ingresado no existe. Por favor, intenta de nuevo.")
        return

    df = pd.read_csv(nombre_archivo)
    
    print("¡Vamos a eliminar una clase!")
    codigo = input("Ingresa el código de la clase a eliminar: ")
    
    # Verificar si el código de la clase existe
    if codigo not in df['codigo'].values:
        print("El código de la clase ingresado no existe. Por favor, intenta de nuevo.")
        return
    
    # Eliminar la clase
    df = df[df['codigo'] != codigo]
    
    df.to_csv(nombre_archivo, index=False) 
    print("¡Clase eliminada exitosamente!")

# Función para mostrar el horario de un curso existente
def mostrar_horario():
    nombre_curso = input("Ingresa el nombre del curso: ")
    nombre_archivo = nombre_curso
    
    # Verificar si el archivo del curso existe
    if not os.path.isfile(nombre_curso):
        print("El nombre del curso ingresado no existe. Por favor, intenta de nuevo.")
        return

    df = pd.read_csv(nombre_archivo)
    
    print("¡Aquí está el horario del curso!")
    print(df)

# Función principal del programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            agregar_clase()
        elif opcion == "2":
            crear_nuevo_curso()
        elif opcion == "3":
            eliminar_clase()
        elif opcion == "4":
            mostrar_horario()
        elif opcion == "5":
            print("¡Gracias por usar el gestor de horarios de cursos!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
