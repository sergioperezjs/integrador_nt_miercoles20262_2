import random
import uuid
import pandas as pd

from faker import Faker

#1. Escoger el pais y leguaje de la simulacion los datos
fake=Faker("es_CO")

#2. simular semillas;
Faker.seed(42)
random.seed(42)

#3. definir el dato y su tipo a simular
#id (texto (UUID))
#fecha_registro (fecha y hora)
#observacion (texto)
#estado (texto) **********
#id_usuario (texto (UUID))
#id_reto (texto (UUID)).

#4. definir el numero de datos simular (DATASET)

filas=800
ESTADOS=["pendiente", "aprobado", "rechazado"]

#5. construir funcion generadora de datos
def generar_datos_registro(numero_registros=filas):

    filas=[]
    for _ in range(numero_registros):
        filas.append({
            "id": str (uuid.uuid4()),
            "fecha_registro": fake.date_time_between(start_date="-1y", end_date='now'),
            "observacion": fake.sentence(nb_words=10),
            "estado": random.choice(ESTADOS),
            "id_usuario": random.choice(IDS_USUARIO),
            "id_reto": random.choice(IDS_RETO)
        })

    return filas
#Se ensucia `fecha_registro`: dos formatos mezclados: "2026-03-15 14:30:00" y "15/03/2026 14:30".

tabla_ordenada_registro=pd.DataFrame(generar_datos_registro())

def generar_muestra(datos, porcentaje):
    return datos.sample(fraccion=porcentaje, random_state=random.randint(0, 9999)).index

def ensuciar_datos(datos_df):
    datos_df=datos_df.copy()

#ensuciar las fechas de registro
    iso = datos_df["fecha_registro"].dt.strftime("%Y-%m-%d %H:%M:%S")               
    latino = datos_df["fecha_registro"].dt.strftime("%d/%m/%Y %H:%M")              
    datos_df["fecha_registro"] = iso                                               
    filas_elegidas = generar_muestra(datos_df, 0.1)
    datos_df.loc[filas_elegidas, "fecha_registro"] = latino.loc[filas_elegidas]

#ensuciar observacion: 20% de las observaciones con none
    subconjuntos_datos=generar_muestra(datos_df, 0.20)
    datos_df.loc[subconjuntos_datos, "observacion"]=None

#Se ensucia estado: variantes: 'inscrito', 'EN PROCESO', ' Finalizado '
    def escribir_mal(texto):
       variantes=['inscrito', 'EN PROCESO', 'Finalizado']
       return random.choice(variantes)   
    subconjuntos_datos=generar_muestra(datos_df, 0.15)
    datos_df.loc[subconjuntos_datos, "rol"]=datos_df.loc[subconjuntos_datos, "rol"].map(escribir_mal)  

#                           

   