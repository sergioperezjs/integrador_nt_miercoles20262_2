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
