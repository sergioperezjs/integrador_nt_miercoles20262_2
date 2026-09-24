import random
import uuid

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