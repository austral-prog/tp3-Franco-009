def check_vowels():
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
# Solicitar el nombre al usuario
# Solicitar input al usuario
    nombre = input("Ingresa un nombre: ")
    nombre = nombre.lower()
    contiene_a = nombre.count('a') > 0
    contiene_e = nombre.count('e') > 0
    contiene_i = nombre.count('i') > 0
    contiene_o = nombre.count('o') > 0
    contiene_u = nombre.count('u') > 0
    print(f"Contiene a: {contiene_a}")
    print(f"Contiene e: {contiene_e}")
    print(f"Contiene i: {contiene_i}")
    print(f"Contiene o: {contiene_o}")
    print(f"Contiene u: {contiene_u}")
check_vowels()