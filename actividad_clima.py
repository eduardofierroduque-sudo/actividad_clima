# Asistente de Clima - Código Completo

def ejecutar_asistente():
    # Iniciamos el bucle para que el programa no se cierre solo
    while True:
        print("\n=== CONSULTA DE CLIMA Y VESTIMENTA ===")
        
        # 1. Pedir al usuario que ingrese la temperatura actual
        # Usamos float por si se ingresan decimales
        temperatura_actual = float(input("Ingrese la temperatura actual en grados Celsius: "))

        # 2. Pedir al usuario la probabilidad de lluvia
        probabilidad_lluvia = float(input("Ingrese la probabilidad de lluvia (en porcentaje): "))

        # 3. Evaluar condiciones y mostrar recomendaciones
        print("\nRECOMENDACIONES:")
        
        if temperatura_actual >= 30:
            print("- Recomendación: Use ropa ligera.")
        elif 15 <= temperatura_actual <= 29:
            print("- Recomendación: Use ropa cómoda.")
        else:
            # Para temperaturas menores a 15
            print("- Recomendación: Use abrigo.")

        # 4. Manejar condiciones de lluvia
        if probabilidad_lluvia >= 50:
            print("- Nota adicional: El cielo está amenazante, ¡lleve paraguas!")

        # 5. Opción para repetir o salir
        continuar = input("\n¿Desea realizar otra consulta? (si/no): ").lower()
        
        if continuar != 'si':
            print("Saliendo del programa... ¡Que tenga un excelente día!")
            break

# Ejecución del programa
if __name__ == "__main__":
    ejecutar_asistente()