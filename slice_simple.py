def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
    primeras_tres = texto[:3].lower()
    media_tres = texto[2:5].lower()
    primera_a_cuarta = texto[:].lower()
    
    print(primeras_tres)
    print(media_tres)
    print(primera_a_cuarta)
slice_simple()