import random 
import uuid 
import pandas as pd
from faker import Faker

#1. Escoger el pais y lenguaje para simular los datos
fake=Faker("es_CO") 

#2. Sembrar semillas
Faker.seed(42)
random.seed(42)

#3. Definir el dato y su tipo a simular
#id (texto (UUID)), 
#nombre (texto), 
#correo (texto), 
#contrasena_hash (texto), 
#rol (texto), *****************
#activo (booleano), 
#fecha_registro (fecha y hora).

#4. Definir el numero de datos simulados (DATASET)
FILAS=400

ROLES=["administrador","empresario","profesor"]

#5. Construir funcion generadora de datos
def generar_datos_usuarios(numero_registros=FILAS):

    filas=[]
    for _ in range(numero_registros):
        filas.append({
            "id":str(uuid.uuid4()),
            "nombre":fake.name(),
            "correo":fake.email(),
            "contrasena_hash":fake.sha256(),
            "rol":random.choice(ROLES),
            "activo":random.choice([True,False]),
            "fecha_registro":fake.date_time_between(start_date="-2y", end_date="now")
        })
    return filas


tabla_ordenada_usuarios = pd.DataFrame(generar_datos_usuarios())

def generar_muestras(datos, porcentaje):
    return datos.sample(fraccion = porcentaje, random_state=random.randint(0,9999)).index

def ensuciar(datos_df):

    datos_df = datos_df.copy()

    #Ensuciando el 10% de los datos NOMBRES
    subconjunto_datos= generar_muestras(datos_df, 0.1)
    datos_df.loc[subconjunto_datos, "nombre"] = " "+datos_df.loc[subconjunto_datos, "nombre"]+" " 

    subconjunto_datos= generar_muestras(datos_df,0.08)
    datos_df.loc[subconjunto_datos, "nombre"] = datos_df.loc[subconjunto_datos,"nombre"].str.upper()

    subconjunto_datos = generar_muestras(datos_df, 0.12)
    datos_df.loc[subconjunto_datos, "correo"] = datos_df[subconjunto_datos, "correo"].str.upper()

    subconjunto_datos = generar_muestras(datos_df, 0.05)
    datos_df.loc[subconjunto_datos, "correo"] = datos_df[subconjunto_datos, "correo"].str.replace("@", "", regex=False)

    subconjunto_datos = generar_muestras(datos_df, 0.04)
    datos_df.loc[subconjunto_datos, "correo"] = None

    def escribir_mal(texto):
        variantes = [texto.lower(), f" {texto.title()}" , texto.capitalize()]
        return random.choice(variantes)


    subconjunto_datos = generar_muestras(datos_df, 0.09)
    datos_df.loc[subconjunto_datos, "rol"] = datos_df.loc[subconjunto_datos, "rol"].map(escribir_mal)