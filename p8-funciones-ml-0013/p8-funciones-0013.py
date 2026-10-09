# Meredith Aguirre NC = 0013

# Lista de nombres base (hombres y mujeres del 31 al 60)
personas = [
    "Carlos", "Ana", "Roberto", "Laura", "Diego", "María", "Javier", "Elena", "Fernando", "Patricia",
    "Gonzalo", "Sofia", "Andrés", "Lucía", "Manuel", "Carmen", "Alejandro", "Isabel", "Rafa", "Marta",
    "David", "Paula", "Sergio", "Beatriz", "Marcos", "Raquel", "Hugo", "Nuria", "Daniel", "Alba"
]


print("-+-+-+-Parámetros con nombre-+-+-+-+")
def Usuario(nombre, edad, ciudad):
    return f"{nombre}, {edad} años, de {ciudad}"

# Usando nombres de la lista con parámetros posicionales y nombrados
usuario1 = Usuario(personas[0], 25, "Madrid")                      # Carlos
usuario2 = Usuario(nombre=personas[1], edad=30, ciudad="Barcelona") # Ana
usuario3 = Usuario(ciudad="Valencia", nombre=personas[3], edad=28) # Laura

print(usuario1)  # Carlos, 25 años, de Madrid
print(usuario2)  # Ana, 30 años, de Barcelona
print(usuario3)  # Laura, 28 años, de Valencia


print("-#-#- *args-Argumentos posicionales variables -#-#-")
def listar_asistentes(*nombres):
    """Muestra cualquier cantidad de nombres recibidos"""
    print(f"Total de personas: {len(nombres)}")
    for nombre in nombres:
        print(f"- {nombre}")

# Pasando diferentes cantidades de nombres de la lista
listar_asistentes(personas[0], personas[1], personas[2])
listar_asistentes(personas[3], personas[5], personas[7], personas[9])


print("-1-1-1- **kwargs-Argumentos con nombre variables -1-1-1-")
def crear_perfil(**datos):
    """Crea un perfil con metadatos variables"""
    print("Perfil registrado:")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")

# Generando perfiles dinámicos para personas de la lista
crear_perfil(nombre=personas[4], edad=32, ciudad="Sevilla")  # Diego
crear_perfil(nombre=personas[5], profesion="Ingeniera", pais="España", status="Activo")  # María


print("-0-0-0-Funciones anidadas-0-0-0-")
def crear_filtrador_por_letra(letra_fin):
    """Retorna una función que filtra nombres que terminan con cierta letra"""
    def filtrar(lista_nombres):
        return [nombre for nombre in lista_nombres if nombre.lower().endswith(letra_fin)]
    return filtrar

# Funciones especializadas para filtrar por terminación de nombre
filtrar_femeninos = crear_filtrador_por_letra("a")
filtrar_masculinos = crear_filtrador_por_letra("o")

print("Nombres que terminan en 'a':", filtrar_femeninos(personas[:10]))
print("Nombres que terminan en 'o':", filtrar_masculinos(personas[:10]))


print("-0-0-0-0-Funciones como objetos de primera clase-0-0-0-0-")
def elegir_formateador(tipo):
    """Retorna una función de formato según la opción seleccionada"""
    def mayusculas(nombre):
        return nombre.upper()

    def minusculas(nombre):
        return nombre.lower()

    if tipo == "MAYUS":
        return mayusculas
    elif tipo == "MINUS":
        return minusculas

# Obtener la función deseada y aplicarla a nombres de la lista
formatear = elegir_formateador("MAYUS")
resultado1 = formatear(personas[6])  # Javier
resultado2 = formatear(personas[7])  # Elena

print(resultado1)  # JAVIER
print(resultado2)  # ELENA


print("-=-=-=-Return múltiple (Tuplas)-=-=-=-")
def clasificar_y_contar(lista_nombres):
    """Clasifica nombres por terminación 'a' (femeninos habituales) y devuelve conteos"""
    femeninos = [n for n in lista_nombres if n.lower().endswith("a")]
    masculinos = [n for n in lista_nombres if not n.lower().endswith("a")]
    return len(femeninos), len(masculinos), femeninos

# Desempaquetado del retorno múltiple
cant_fem, cant_masc, lista_fem = clasificar_y_contar(personas)
print(f"Total mujeres aprox: {cant_fem} | Total hombres aprox: {cant_masc}")
print("Primeras mujeres identificadas:", lista_fem[:3])

print("Meredith Aguirre NC 0013")