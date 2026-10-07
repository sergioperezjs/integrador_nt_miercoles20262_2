import uuid
import random
import pandas as pd
from faker import Faker

# 1. Escoger el país y lenguaje para simular los datos
fake = Faker("es_CO")

# 2. Sembrar semillas para reproducibilidad exacta
Faker.seed(42)
random.seed(42)

# 3. Definir constantes del dominio (5 prioridades reales y sus días de respuesta)
NIVELES = {
    "Urgente": 1,
    "Alta": 2,
    "Media": 3,
    "Baja": 4,
    "Planificada": 5,
}

DIAS = {
    1: 1,    # Urgente -> 1 día
    2: 3,    # Alta -> 3 días
    3: 7,    # Media -> 7 días
    4: 15,   # Baja -> 15 días
    5: 30,   # Planificada -> 30 días
}

# MAPEO AUXILIAR PARA LA OPCIÓN DE "NIVEL EN PALABRAS"
NIVEL_A_PALABRA = {
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
}

# 4. Definir el número de datos simulados (DATASET)
FILAS = 200

def generar_muestra(datos, porcentaje):
    return datos.sample(frac=porcentaje, random_state=random.randint(0, 9999)).index

def escribir_mal(texto):
    variantes = [texto.upper(), f" {texto.lower()} ", texto.capitalize()]
    return random.choice(variantes)

def ensuciar(datos_df):
    datos_df = datos_df.copy()

    # CONVERSIÓN CLAVE: Convertir columnas a 'object' para permitir mezclar tipos (str, None, int)
    datos_df["nivel"] = datos_df["nivel"].astype(object)
    datos_df["dias_max_respuesta"] = datos_df["dias_max_respuesta"].astype(object)

    # --- A. Ensuciar 'nombre' ---
    subconjunto_nombre = generar_muestra(datos_df, 0.20)
    datos_df.loc[subconjunto_nombre, "nombre"] = datos_df.loc[subconjunto_nombre, "nombre"].map(escribir_mal)

    # --- B. Ensuciar 'nivel' ---
    # Convertir algunos enteros a texto (ej. '3')
    subconjunto_nivel_str = generar_muestra(datos_df, 0.15)
    datos_df.loc[subconjunto_nivel_str, "nivel"] = datos_df.loc[subconjunto_nivel_str, "nivel"].astype(str)

    # Convertir algunos enteros a palabras (ej. 'tres')
    subconjunto_nivel_palabra = generar_muestra(datos_df, 0.10)
    datos_df.loc[subconjunto_nivel_palabra, "nivel"] = datos_df.loc[subconjunto_nivel_palabra, "nivel"].map(
        lambda x: NIVEL_A_PALABRA.get(int(x), str(x)) if str(x).isdigit() else x
    )

    # 7% de valores en None
    subconjunto_nivel_null = generar_muestra(datos_df, 0.07)
    datos_df.loc[subconjunto_nivel_null, "nivel"] = None

    # --- C. Ensuciar 'dias_max_respuesta' ---
    # 5% de valores en None
    subconjunto_dias_null = generar_muestra(datos_df, 0.05)
    datos_df.loc[subconjunto_dias_null, "dias_max_respuesta"] = None

    # 3% con valor absurdo (999)
    subconjunto_dias_absurdo = generar_muestra(datos_df, 0.03)
    datos_df.loc[subconjunto_dias_absurdo, "dias_max_respuesta"] = 999

    # --- D. Inyectar 8% de duplicados exactos ---
    filas_duplicadas = datos_df.sample(frac=0.08, random_state=42)
    datos_df = pd.concat([datos_df, filas_duplicadas], ignore_index=True)

    return datos_df

def generar_prioridades(n=FILAS):
    filas = []
    
    Faker.seed(42)
    random.seed(42)

    for _ in range(n):
        nombre_prioridad = random.choice(list(NIVELES.keys()))
        nivel_prioridad = NIVELES[nombre_prioridad]
        dias_respuesta = DIAS[nivel_prioridad]

        filas.append({
            "id": str(uuid.uuid4()),
            "nombre": nombre_prioridad,
            "nivel": nivel_prioridad,
            "dias_max_respuesta": dias_respuesta
        })

    df_limpio = pd.DataFrame(filas)
    df_sucio = ensuciar(df_limpio)

    return df_sucio

if __name__ == "__main__":
    df = generar_prioridades()
    print("=== SHAPE DEL DATAFRAME ===")
    print(df.shape)
    print("\n=== PRIMERAS FILAS ===")
    print(df.head(10))
    print("\n=== VALORES NULOS POR COLUMNA ===")
    print(df.isna().sum())


