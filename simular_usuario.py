
import random
import uuid

from faker import Faker

#1. Escoger el pais y leguaje de la simulacion los datos
fake=Faker("es_CO")

#2. simular semillas;
Faker.seed(42)
random.seed(42)

#3. definir el dato y su tipo a simular
#id (texto (UUID))
#nombre (texto)
#corroreo (texto)
#contrasena (texto)
#rol (texto) ***********
#activo (booleano)
#fecha_registro (fecha y hora)

#4. definir el numero de datos simular (DATASET)
filas=400

ROLES=["Admin","Empresario","Profesor","Estudiante","Coord","Vigilante"]

#construir funcion generadora de datos
def generar_datos_usuarios(numero_registros=filas):

    filas=[]
    for _ in range(numero_registros):
        filas.append({
            "id":str (uuid.uuid4()),
            "nombre": fake.name(),
            "correo": fake.email(),
            "contraseña_hash": fake.sha256(),
            "rol":random.choice(ROLES),
            "activo":random.choice([True,False]),
            "fecha_registro":fake.date_time_between(start_date="-2y",end_date="now")
        })
        return filas