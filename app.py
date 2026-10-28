from datetime import datetime

print("========================================")
print("     SISTEMA DE ASISTENCIA SENA")
print("========================================")

while True:
    print("--- MENÚ PRINCIPAL ---")
    print("1. Registrar estudiante")
    print("2. Ver lista de asistencia")
    print("3. Salir")
    
    opcion = input("Elige una opción (1, 2 o 3): ")
    
    if opcion == "1":
        print("--- REGISTRO ---")
        nombre = input("Ingresa el nombre del estudiante: ")
        ficha = input("Ingresa el número de ficha: ")
        
        
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        
        with open("usuarios.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"Fecha/Hora: {fecha_hora} | Nombre: {nombre} | Ficha: {ficha}")
            
        print(f"¡Estudiante {nombre} de la ficha {ficha} registrado con éxito!")
        
    elif opcion == "2":
        print("\n--- LISTA DE ASISTENCIAS ---")
        try:
            with open("usuarios.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                if contenido == "":
                    print("Todavía no hay registros guardados.")
                else:
                    print(contenido)
        except FileNotFoundError:
            print("Todavía no hay registros guardados.")
                
    elif opcion == "3":
        print("Saliendo del sistema... ¡Chao, Pipe!")
        break
        
    else:
        print("Opción inválida, intenta de nuevo.")