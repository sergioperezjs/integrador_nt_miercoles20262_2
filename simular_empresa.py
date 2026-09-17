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
# nit (texto), 
# sector (texto) ***************
# contacto (texto), 
# correo (texto), 
# telefono (texto), 
# activa (booleano).

#Definir el numero de datos simulados (DATASET)

FILAS = 300
