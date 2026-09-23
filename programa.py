def validar_codigo(codigo):
    return bool(codigo.strip()) and len(codigo.strip()) >= 8

def registrar_solicitud():
    codigo = input("Código del estudiante: ")
    
    if validar_codigo(codigo):
        print("Código válido.")
    else:
        print("Código inválido. Debe tener al menos 8 caracteres.")
        return 

    
    nombre = input("Nombre del estudiante: ")
    tipo = input("Tipo de consulta: ")
    descripcion = input("Descripción: ")

    print("\nSolicitud registrada.")
    print(f"Código: {codigo}")
    print(f"Nombre: {nombre}")
    print(f"Tipo: {tipo}")
    print(f"Descripción: {descripcion}")

registrar_solicitud()