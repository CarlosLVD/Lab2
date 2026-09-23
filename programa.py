TIPOS_CONSULTA = [
    "matrícula",
    "pagos",
    "constancia",
    "plataforma",
    "otro"
]

def validar_codigo(codigo):
    return bool(codigo.strip()) and len(codigo.strip()) >= 8

def validar_tipo(tipo):
    tipo_limpio = tipo.strip().lower()
    
    if tipo_limpio in TIPOS_CONSULTA:
        return True
    else:
        return False

def registrar_solicitud():
    codigo = input("Código del estudiante: ")
    
    if validar_codigo(codigo):
        print("Código válido.")
    else:
        print("Código inválido. Debe tener al menos 8 caracteres.")
        return 
    
    nombre = input("Nombre del estudiante: ")
    
    print("Opciones de consulta: matrícula, pagos, constancia, plataforma, otro")
    tipo = input("Tipo de consulta: ")
    
    if validar_tipo(tipo):
        print("Tipo válido.")
    else:
        print("Tipo de consulta inválido. Debes elegir una opción de la lista.")
        return
        
    descripcion = input("Descripción: ")

    print("\nSolicitud registrada.")
    print(f"Código: {codigo}")
    print(f"Nombre: {nombre}")
    print(f"Tipo: {tipo}")
    print(f"Descripción: {descripcion}")

registrar_solicitud()