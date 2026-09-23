def registrar_solicitud():
    codigo = input("Código del estudiante: ")
    nombre = input("Nombre del estudiante: ")
    tipo = input("Tipo de consulta: ")
    descripcion = input("Descripción: ")

    print("\nSolicitud registrada.")
    print(f"Código: {codigo}")
    print(f"Nombre: {nombre}")
    print(f"Tipo: {tipo}")
    print(f"Descripción: {descripcion}")

registrar_solicitud()