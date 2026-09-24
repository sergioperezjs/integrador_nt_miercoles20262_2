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
#fecha_registro (fecha y hora)
#observacion (texto)
#estado (texto) **********
#id_usuario (texto (UUID))
#id_reto (texto (UUID)).

#4. definir el numero de datos simular (DATASET)
filas=250
ROLES=["Admin","Empresario","Profesor","Estudiante","Coord","Vigilante"]
CATEGORIAS=[ "Tecnología",
  "Educación",
  "Salud",
  "Finanzas",
  "Entretenimiento"]
AREAS=[ "Desarrollo",
  "Recursos Humanos",
  "Marketing",
  "Ventas",
  "Administración"]

#construir funcion generadora de datos
def generar_datos_usuarios(numero_registros=filas):

    filas=[]
    for _ in range(numero_registros):
        filas.append({
            "id":str (uuid.uuid4()),
            "nombre": ramdom.choice(CATEGORIAS),
            "descripcion": fake.sentence(nb_words=8),
            "area_responsable": random.choice(AREAS)        ,
    
        })
        return filas