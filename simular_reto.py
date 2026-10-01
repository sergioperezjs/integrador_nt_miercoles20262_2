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
#descripcion (texto), 
#fecha_inicio (fecha), 
#fecha_fin (fecha), 
#estado (texto), *************
#id_empresa (texto (UUID)), 
#id_categoria (texto (UUID)), 
#id_prioridad (texto (UUID))

#4. Definir el numero de datos simulado (DATASET)
FILAS=500

ESTADOS=["Pendiente","En_proceso","Completado","Cancelado"]
IDS_EMPRESA=[1,2,3,4]
IDS_CATEGORIA=["Hardware","Software","Redes","Soporte"]
IDS_PRIORIDAD=["Baja","Media","Alta","Critica"]

#5. Construir funcion generadora de datos
def generar_datos_retos(numero_registros=FILAS):

    filas=[]
    for _ in range(numero_registros):
        filas.append({
            "id":str(uuid.uuid4()),
            "nombre":fake.sentence(nb_words=6).rstrip("."),
            "descripcion":fake.sentence(nb_words=12),
            "fecha_inicio":fake.date_between(start_date="-1y", end_date="+3m"),
            "fecha_fin":fecha_inicio + timedelta(days=random.randint(15, 180)),
            "estado":random.choice(ESTADOS),
            "id_empresa":random.choice(IDS_EMPRESA),
            "id_categoria":random.choice(IDS_CATEGORIA),
            "id_prioridad":random.choice(IDS_PRIORIDAD)
        })
    return filas

#6. Utilizaremos Pandas para ordenar los datos simulados en un Dataframe
tabla_ordenada_reto=pd.DataFrame(generar_datos_retos())

#7.1. Generar una funcion que muestre los datos
def generar_muestra(datos,porcentaje):
    return datos.sample(fraccion=porcentaje,random_state=random.randint(0,9999)).index

#7.2 Funcion que ensucia los datos
def ensuciar(datos_df):
    datos_df=datos_df.copy()

    # Se ensucia `nombre`: 10% con espacios sobrantes.
    subconjunto_datos=generar_muestra(datos_df,0.1)
    datos_df.loc[subconjunto_datos,"nombre"]=" " + datos_df.loc[subconjunto_datos,"nombre"] + " "

    # Se ensucia `descripcion`: 12% en None (nulos).
    subconjunto_datos=generar_muestra(datos_df,0.12)
    datos_df.loc[subconjunto_datos,"descripcion"]=None

    # Se ensucia `fecha_inicio`: dos formatos mezclados: "2026-03-02" y "02/03/2026".
    iso = datos_df["fecha_inicio"].dt.strftime("%2026-%03-%02")               
    latino = datos_df["fecha_inicio"].dt.strftime("%02/%03/%2026")              
    datos_df["fecha_inicio"] = iso                                               
    subconjunto_datos = generar_muestra(datos_df, 0.30)
    datos_df.loc[subconjunto_datos, "fecha_inicio"] = latino.loc[subconjunto_datos]

