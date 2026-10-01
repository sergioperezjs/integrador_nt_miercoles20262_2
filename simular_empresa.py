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
def generar_muestras():