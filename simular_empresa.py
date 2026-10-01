import random 
import uuid
import pandas as pd
from faker import Faker as fk


#Escoger el pais y lenguaje para simular los datos : 

fake = fk("es_CO")

#Sembrar semilla 
fk.seed(42)
random.seed(42)

#Definir el dato y su tipo a simular
# id (texto (UUID)), 
# nombre (texto), 
# nit (texto), 
# sector (texto) ***************
# contacto (texto), 
# correo (texto), 
# telefono (texto), 
# activa (booleano).

#Definir el numero de datos simulados (DATASET)

FILAS = 300
SECTORES = ["Tecnología", "Salud", "Educación", "Finanzas", "Manufactura", "Comercio", "Transporte", "Turismo", "Agricultura", "Energía"]

def generar_datos_empresa():
    filas = []
    numero_datos = FILAS
    for _ in range(numero_datos):
        filas.append({
            "id": str(uuid.uuid4()),
            "nombre": fake.company(),
            "nit": fake.unique.numerify(text="#########-#"),
            "sector": random.choice(SECTORES),
            "contacto": fake.name(),
            "correo": fake.unique.email(),
            "telefono": fake.phone_number(),
            "activa": random.choice([True, False])
        })
        return filas

#Utilizaremos PANDAS para ordenar los datos simulados en un DATAFRAME

tabla_ordenada_empresas = pd.DataFrame(generar_datos_empresa())

#Ensuciar los datos
#Generar una funcion que nos muestre los datos
def generar_muestras(datos, porcentaje):
    return datos.sample(fraccion = porcentaje, random_state = random.ranint(0,9999)).index

def ensuciar(datos_df):
    datos_df = datos_df.copy

    subconjuntos_datos = generar_muestras(datos_df, 0.1)
    datos_df.loc[subconjuntos_datos, "nombre"] = " "+datos_df.loc[subconjuntos_datos, "nombre"]+" "

    subconjuntos_datos = generar_muestras(datos_df, 0.15)
    datos_df.loc[subconjuntos_datos, "nombre"] = datos_df.loc[subconjuntos_datos, "nombre"].str.upper()

    subconjuntos_datos = generar_muestras(datos_df, 0.5)
    datos_df.loc[subconjuntos_datos, "nit"] = datos_df.loc[subconjuntos_datos, "nit"].str.replace("#########-#" , "###.###.###-#")

    subconjuntos_datos = generar_muestras(datos_df, 0.5)
    datos_df.loc[subconjuntos_datos, "nit"] = datos_df.loc[subconjuntos_datos, "nit"].str.replace("#########-#" , "##########")

    def variantes(texto):
        return random.choice([texto.upper(), texto.capitalyze(), texto.lower()])

    subconjuntos_datos = generar_muestras(datos_df, 0.4)
    datos_df.loc[subconjuntos_datos, "sector"] = datos_df.loc[subconjuntos_datos, "sector"].map(variantes)

    subconjuntos_datos = generar_muestras(datos_df, 0.08)
    datos_df.loc[subconjuntos_datos, "contacto"] = None

    subconjuntos_datos = generar_muestras(datos_df, 0.06)
    datos_df.loc[subconjuntos_datos, "correo"] = datos_df.loc[subconjuntos_datos, "correo"].str.replace("@" , "", regex=False)
    