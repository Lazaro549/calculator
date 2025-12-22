import math


def get_float(prompt):
    """Helper to safely get a float from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid number. Try again.")


def get_int(prompt):
    """Helper to safely get an integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid integer. Try again.")


def calculadora():
    # Idioma / Language selection
    idiom = ""
    while idiom not in ("english", "en", "eng", "español", "espanol", "es", "spanish"):
        idiom = input("🌐 english || español: ").lower()

    # Define mensajes dinámicos
    is_spanish = idiom in ("español", "espanol", "es", "spanish")

    # Diccionario de mensajes
    msg = {
        "exit": "Programa finalizado." if is_spanish else "Program ended.",
        "invalid_op": "Operación inválida. Intente de nuevo." if is_spanish else "Invalid operation. Try again.",
        "enter_num": "Ingrese número: " if is_spanish else "Enter number: ",
        "count_prompt": "Ingrese un número para contar hasta él: " if is_spanish else "Enter a number to count up to: ",
        "avg_prompt": "¿Cuántos números desea promediar?: " if is_spanish else "How many numbers do you want to average?: ",
        "no_avg": "No hay números para promediar." if is_spanish else "No numbers to average.",
        "zero_error": "Error: No se permite la división por cero." if is_spanish else "Error: Division by zero is not allowed.",
        "sqrt_neg": "Error: no se puede calcular la raíz cuadrada de un número negativo."
        if is_spanish
        else "Error: Cannot calculate the square root of a negative number.",
    }

    # Bucle principal
    while True:
        if is_spanish:
            op = input(
                "\nIngrese operación (+, -, *, /, contador, promedio, porcentaje, raíz, salir): "
            ).lower()
        else:
            op = input(
                "\nEnter operation (+, -, *, /, counter, average, percentage, root, exit): "
            ).lower()

        if op in ("salir", "exit"):
            print(msg["exit"])
            break

        # SUMA / ADDITION
        elif op in ("+", "sumar", "suma", "add", "plus", "a"):
            n = get_int("¿Cuántos números? " if is_spanish else "How many numbers? ")
            acc = 0
            for _ in range(n):
                num = get_float(msg["enter_num"])
                print(f"{acc} + {num} = {acc + num}")
                acc += num

        # RESTA / SUBTRACTION
        elif op in ("-", "restar", "resta", "subtract", "sub"):
            n = get_int("¿Cuántos números? " if is_spanish else "How many numbers? ")
            acc = get_float(msg["enter_num"])
            for _ in range(n - 1):
                num = get_float(msg["enter_num"])
                print(f"{acc} - {num} = {acc - num}")
                acc -= num

        # MULTIPLICACIÓN / MULTIPLICATION
        elif op in ("*", "multiplicar", "mul", "mult", "multiply"):
            n = get_int("¿Cuántos números? " if is_spanish else "How many numbers? ")
            acc = 1
            for _ in range(n):
                num = get_float(msg["enter_num"])
                print(f"{acc} * {num} = {acc * num}")
                acc *= num

        # DIVISIÓN / DIVISION
        elif op in ("/", "dividir", "div", "divide"):
            n = get_int("¿Cuántos números? " if is_spanish else "How many numbers? ")
            acc = get_float(msg["enter_num"])
            for _ in range(n - 1):
                num = get_float(msg["enter_num"])
                if num == 0:
                    print(msg["zero_error"])
                    continue
                print(f"{acc} / {num} = {acc / num}")
                acc /= num

        # CONTADOR / COUNTER
        elif op in ("contador", "count", "counter"):
            num = get_int(msg["count_prompt"])
            for i in range(num + 1):
                print(i)

        # PROMEDIO / AVERAGE
        elif op in ("promedio", "average", "avg"):
            n = get_int(msg["avg_prompt"])
            if n > 0:
                total = sum(get_float(msg["enter_num"]) for _ in range(n))
                avg = total / n
                print(("El promedio es: " if is_spanish else "The average is:"), avg)
            else:
                print(msg["no_avg"])

        # PORCENTAJE / PERCENTAGE
        elif op in ("porcentaje", "percentage", "percent"):
            total = get_float("Valor total: " if is_spanish else "Total value: ")
            part = get_float("Valor parcial: " if is_spanish else "Part value: ")
            if total != 0:
                print(f"{(part / total) * 100:.2f}%")
            else:
                print(msg["zero_error"])

        # RAÍZ / SQUARE ROOT
        elif op in ("raiz", "raíz", "sqrt", "root"):
            num = get_float(msg["enter_num"])
            if num >= 0:
                print(f"√{num} = {math.sqrt(num)}")
            else:
                print(msg["sqrt_neg"])

        else:
            print(msg["invalid_op"])


if __name__ == "__main__":
    calculadora()
# Fin del código de la calculadora bilingüe mejorada