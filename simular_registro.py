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
filas=800