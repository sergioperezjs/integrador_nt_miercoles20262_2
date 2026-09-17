import random 
import uuid
from faker import Faker as fk

#Escoger el pais y lenguaje para simular los datos : 

fake = fk("es_CO")

#Sembrar semilla 
fk.seed(42)
random.seed(42)

#Definir el dato y su tipo a simular
# id (texto (UUID)), 
# nombre (texto),
# correo (texto),
# contrasena_hash (texto),
# rol (texto) ***********************
# activo (boolean),
# fecha_registro (fecha y hora).

#Definir el numero de datos simulados (DATASET)

FILAS = 400