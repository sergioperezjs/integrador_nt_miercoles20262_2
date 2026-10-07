import random
import uuid
import pandas as pd
from faker import Faker
from datetime import timedelta

# 1. Escoger el pais y lenguaje para simular los datos
fake = Faker("es_CO")

# 2. Sembrar semillas
Faker.seed(42)
random.seed(42)

# 3. Definir el dato y su tipo a simular
# id (texto (UUID)),
# nombre (texto),
# descripcion (texto),
# fecha_inicio (fecha),
# fecha_fin (fecha),
# estado (texto),
# id_empresa (texto (UUID)),
# id_categoria (texto (UUID)),
# id_prioridad (texto (UUID))

# 4. Definir el numero de datos simulado (DATASET)
FILAS = 500

ESTADOS = ["Pendiente", "En_proceso", "Completado", "Cancelado"]
IDS_EMPRESA = [1, 2, 3, 4]
IDS_CATEGORIA = ["Hardware", "Software", "Redes", "Soporte"]
IDS_PRIORIDAD = ["Baja", "Media", "Alta", "Critica"]

# 5. Construir funcion generadora de datos
def generar_datos_retos(numero_registros=FILAS):

    filas = []

    for _ in range(numero_registros):

        fecha_inicio = fake.date_between(
            start_date="-1y",
            end_date="+3m"
        )

        filas.append({
            "id": str(uuid.uuid4()),
            "nombre": fake.sentence(nb_words=6).rstrip("."),
            "descripcion": fake.sentence(nb_words=12),
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_inicio + timedelta(days=random.randint(15, 180)),
            "estado": random.choice(ESTADOS),
            "id_empresa": random.choice(IDS_EMPRESA),
            "id_categoria": random.choice(IDS_CATEGORIA),
            "id_prioridad": random.choice(IDS_PRIORIDAD)
        })

    return filas


# 6. Utilizaremos Pandas para ordenar los datos simulados en un Dataframe
tabla_ordenada_reto = pd.DataFrame(generar_datos_retos())

# Convertimos las fechas a formato fecha
tabla_ordenada_reto["fecha_inicio"] = pd.to_datetime(
    tabla_ordenada_reto["fecha_inicio"]
)

tabla_ordenada_reto["fecha_fin"] = pd.to_datetime(
    tabla_ordenada_reto["fecha_fin"]
)


# 7.1. Generar una funcion que muestre los datos
def generar_muestra(datos, porcentaje):
    return datos.sample(
        frac=porcentaje,
        random_state=random.randint(0, 9999)
    ).index


# 7.2. Funcion que ensucia los datos
def ensuciar(datos_df):

    datos_df = datos_df.copy()

    # Se ensucia `nombre`: 10% con espacios sobrantes.
    subconjunto_datos = generar_muestra(datos_df, 0.10)

    datos_df.loc[subconjunto_datos, "nombre"] = (
        " " + datos_df.loc[subconjunto_datos, "nombre"] + " "
    )



    # Se ensucia `descripcion`: 12% en None (nulos).
    subconjunto_datos = generar_muestra(datos_df, 0.12)

    datos_df.loc[subconjunto_datos, "descripcion"] = None


    # Se ensucia `fecha_inicio`:
    # dos formatos mezclados:
    # "2026-03-02" y "02/03/2026".
    iso = datos_df["fecha_inicio"].dt.strftime("%Y-%m-%d")
    latino = datos_df["fecha_inicio"].dt.strftime("%d/%m/%Y")

    datos_df["fecha_inicio"] = iso

    subconjunto_datos = generar_muestra(datos_df, 0.30)

    datos_df.loc[subconjunto_datos, "fecha_inicio"] = (
        latino.loc[subconjunto_datos]
    )

    # Se ensucia `fecha_fin`:
    # 8% en None (nulos).
    subconjunto_datos = generar_muestra(datos_df, 0.08)

    datos_df.loc[subconjunto_datos, "fecha_fin"] = None

    # Se ensucia `fecha_fin`:
    # 5% queda ANTERIOR a `fecha_inicio`.
    # Esto genera un error lógico que posteriormente
    # puede ser detectado.
    subconjunto_datos = generar_muestra(datos_df, 0.05)

    for indice in subconjunto_datos:

        # Ponemos fecha_fin unos días antes de fecha_inicio
        datos_df.loc[indice, "fecha_fin"] = (
            pd.to_datetime(
                datos_df.loc[indice, "fecha_inicio"],
                dayfirst=True,
                errors="coerce"
            ) - timedelta(days=random.randint(1, 30))
        )

    # Se ensucia `estado`:
    # se agregan diferentes variantes.
    subconjunto_datos = generar_muestra(datos_df, 0.05)

    variantes_estado = ["en_curso", "EN CURSO", " Cerrado "]

    datos_df.loc[subconjunto_datos, "estado"] = [
        random.choice(variantes_estado)
        for _ in subconjunto_datos
    ]

    # 5% de las filas se repiten tal cual.
    # Esto genera duplicados exactos.
    cantidad_duplicados = int(len(datos_df) * 0.05)

    filas_duplicadas = datos_df.sample(
        n=cantidad_duplicados,
        random_state=42
    )

    datos_df = pd.concat(
        [datos_df, filas_duplicadas],
        ignore_index=True
    )


    return datos_df


# 8. Aplicar la funcion para ensuciar los datos
tabla_sucia_reto = ensuciar(tabla_ordenada_reto)


# 9. Mostrar resultado
print(tabla_sucia_reto.head())

# Cantidad total de registros después de agregar duplicados
print("\nCantidad total de registros:", len(tabla_sucia_reto))

# Cantidad de duplicados exactos
print(
    "Cantidad de duplicados exactos:",
    tabla_sucia_reto.duplicated().sum()
)

