# Asistente de Clima - Código Actualizado

def ejecutar_asistente():
    # Iniciamos el bucle para que el programa no se cierre solo
    while True:
        print("\n=== CONSULTA DE CLIMA Y VESTIMENTA ===")
        
        try:
            # 1. Pedir la temperatura y convertirla a número ENTERO
            temperatura_actual = int(input("Ingrese la temperatura actual en grados Celsius (número entero): "))

            # --- VALIDACIÓN DE COHERENCIA ---
            if temperatura_actual > 42:
                print(f"Error: El valor {temperatura_actual}°C no es coherente. Por favor, verifique el dato.")
                continue # Reinicia el bucle para pedir el dato de nuevo
            
            if temperatura_actual > 35:
                print(f"¡Aviso! La temperatura de {temperatura_actual}°C es muy alta.")
                print("¿Es seguro que es esa temperatura? Se sugiere comprobar realmente la medición.")
            # --------------------------------

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

        except ValueError:
            print("Error: Por favor, ingrese solo números válidos.")
            continue

        # 5. Opción para repetir o salir
        continuar = input("\n¿Desea realizar otra consulta? (si/no): ").lower()
        
        if continuar != 'si':
            print("Saliendo del programa... ¡Que tenga un excelente día!")
            break

# Ejecución del programa
if __name__ == "__main__":
    ejecutar_asistente()
