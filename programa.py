def validar_codigo(codigo):
    return bool(codigo.strip()) and len(codigo.strip()) >= 8


def validar_texto(texto):
    return bool(texto.strip())


def mostrar_resumen(codigo, nombre, tipo, descripcion, prioridad):
    print("\n----- RESUMEN DE SOLICITUD -----")
    print(f"Código: {codigo}")
    print(f"Nombre: {nombre}")
    print(f"Tipo de consulta: {tipo}")
    print(f"Descripción: {descripcion}")
    print(f"Prioridad: {prioridad}")
    print("--------------------------------")


def validar_tipo(tipo, lista_permitida):
    tipo_limpio = tipo.strip().lower()

    if tipo_limpio in lista_permitida:
        return True
    else:
        return False


def calcular_prioridad(tipo):
    tipo = tipo.strip().lower()

    if tipo == "matrícula" or tipo == "plataforma":
        return "Alta"
    elif tipo == "pagos":
        return "Media"
    else:
        return "Baja"


def registrar_solicitud():
    tipos_consulta = [
        "matrícula",
        "pagos",
        "constancia",
        "plataforma",
        "otro"
    ]

    codigo = input("Código del estudiante: ")

    if validar_codigo(codigo):
        print("Código válido.")
    else:
        print("Error: el código debe tener al menos 8 caracteres.")
        return None

    nombre = input("Nombre del estudiante: ")

    if validar_texto(nombre):
        print("Nombre válido.")
    else:
        print("Error: el nombre no puede estar vacío.")
        return None

    print("Opciones de consulta: matrícula, pagos, constancia, plataforma, otro")
    tipo = input("Tipo de consulta: ")

    if validar_tipo(tipo, tipos_consulta):
        print("Tipo de consulta válido.")
        prioridad = calcular_prioridad(tipo)
    else:
        print("Error: tipo de consulta no válido.")
        return None

    descripcion = input("Descripción: ")

    if validar_texto(descripcion):
        print("Descripción válida.")
    else:
        print("Error: la descripción no puede estar vacía.")
        return None

    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "descripcion": descripcion,
        "prioridad": prioridad
    }

    print("\nSolicitud registrada.")
    mostrar_resumen(codigo, nombre, tipo, descripcion, prioridad)

    return solicitud


def menu_principal():
    solicitudes = []

    while True:
        print("\n=== SOPORTE ACADÉMICO ===")
        print("1. Registrar solicitud")
        print("2. Mostrar solicitudes")
        print("3. Salir")

        opcion = input("Elige una opción (1, 2 o 3): ")

        if opcion == "1":
            solicitud = registrar_solicitud()

            if solicitud is not None:
                solicitudes.append(solicitud)

        elif opcion == "2":
            print("\n=== SOLICITUDES REGISTRADAS ===")

            if len(solicitudes) == 0:
                print("No hay solicitudes registradas.")
            else:
                for i, solicitud in enumerate(solicitudes, start=1):
                    print(f"\nSolicitud #{i}")

                    mostrar_resumen(
                        solicitud["codigo"],
                        solicitud["nombre"],
                        solicitud["tipo"],
                        solicitud["descripcion"],
                        solicitud["prioridad"]
                    )

        elif opcion == "3":
            print("Saliendo del sistema... ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, ingresa 1, 2 o 3.")


if __name__ == "__main__":
    menu_principal()