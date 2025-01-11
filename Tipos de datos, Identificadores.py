# Programa de conversión de unidades de longitud
# Este programa permite al usuario convertir entre metros y pies.
# Utiliza diferentes tipos de datos y sigue la convención snake_case.

def convertir_metros_a_pies(metros):
    """Convierte una medida en metros a pies."""
    pies = metros * 3.28084  # 1 metro es aproximadamente 3.28084 pies
    return pies


def convertir_pies_a_metros(pies):
    """Convierte una medida en pies a metros."""
    metros = pies / 3.28084  # 1 pie es aproximadamente 0.3048 metros
    return metros


def main():
    """Función principal que ejecuta el programa."""
    # Solicitar al usuario la opción de conversión
    tipo_conversion = input("¿Qué tipo de conversión deseas realizar? (1: Metros a Pies, 2: Pies a Metros): ")

    # Validar la opción ingresada por el usuario
    if tipo_conversion not in ['1', '2']:
        print("Opción no válida. Por favor, elige 1 o 2.")
        return

    # Solicitar el valor a convertir
    valor = float(input("Introduce el valor a convertir: "))

    if tipo_conversion == '1':
        # Convertir de metros a pies
        resultado = convertir_metros_a_pies(valor)
        print(f"{valor} metros son {resultado:.2f} pies.")

    elif tipo_conversion == '2':
        # Convertir de pies a metros
        resultado = convertir_pies_a_metros(valor)
        print(f"{valor} pies son {resultado:.2f} metros.")


# Comprobar si este archivo es el programa principal
if __name__ == "__main__":
    main()
