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
#nombre (texto)
#corroreo (texto)
#contrasena (texto)
#rol (texto) ***********
#activo (booleano)
#fecha_registro (fecha y hora)

#4. definir el numero de datos simular (DATASET)
filas=400
ROLES=["admin", "empresarios", "profesor"]

#5. construir funcion generadora de datos
def generar_datos_usuarios(numero_registros=FILAS):

    filas=[]
    for _ in range(numero_registros):
        filas.append({
            "id": str (uuid.uuid4()),
            "nombre": fake.name(),
            "correo": fake.email(),
            "contrasena": fake.sha256(),
            "rol": random.choice(ROLES),
            "activo": random.choice([True, False]),
            "fecha_registro": fake.date_time_between(start_date="-2y", end_date='now')
        })

    return filas
#6 . utilizaremos pandas para ordenar  los datos simulados en un dataframe
tabla_ordenada_usuarios=pd.DataFrame(generar_datos_usuarios())


#7. ensuciar los datos
#1 generar una funcion que muestre los datos
def generar_muestra(datos, porcentaje):
    return datos.sample(fraccion=porcentaje, random_state=random.randint(0, 9999)).index

#7,2 funcion que ensucia los datos
def ensuciar_datos(datos_df):
    datos_df=datos_df.copy()

    #para el atributo nombre generar un 10%  con espacios sobrantes 
    subconjuntos_datos=generar_muestra(datos_df, 0.1)
    datos_df.loc[subconjuntos_datos, "nombre"]=" "+datos_df.loc[subconjuntos_datos, "nombre"]+"  "


    #para el atributo nombre generar el 8% en Mayusculas
    subconjuntos_datos=generar_muestra(datos_df, 0.08)
    datos_df.loc[subconjuntos_datos, "nombre"]=datos_df.loc[subconjuntos_datos, "nombre"].upper()

    #para el atributo correo generar el 12% de los datos en mayuscula 

    subconjuntos_datos=generar_muestra(datos_df, 0.12)
    datos_df.loc[subconjuntos_datos, "correo"]=datos_df.loc[subconjuntos_datos, "correo"].upper()

    # para el atributo correo generar el 5% de los datos sin @
    subconjuntos_datos=generar_muestra(datos_df, 0.05)
    datos_df.loc[subconjuntos_datos, "correo"]=datos_df.loc[subconjuntos_datos, "correo"].str.replace("@", "", regex=False)

    #para el atributo correo generar el 4% de los datos en nome
    subconjuntos_datos=generar_muestra(datos_df, 0.04)
    datos_df.loc[subconjuntos_datos, "correo"]=None

    # para el atributo rol para la palabra administrador y las otras generar variantes de escritura (Mayusculas, capital,espaciado)
    def escribir_mal(texto):
        variantes=[texto.lower(), f" {texto.title()} ", texto.capitalize()]
        return random.choice(variantes)
    subconjuntos_datos=generar_muestra(datos_df, 0.15)
    datos_df.loc[subconjuntos_datos, "rol"]=datos_df.loc[subconjuntos_datos, "rol"].map(escribir_mal)

    # Para el atributo fecha_registro: dos formatos mezclados ("2026-03-15 14:30:00" y "15/03/2026 14:30")
    # (si tu fecha es solo fecha, sin hora, usa "%Y-%m-%d" y "%d/%m/%Y")
    iso = datos_df["fecha_registro"].dt.strftime("%Y-%m-%d %H:%M:%S")               
    latino = datos_df["fecha_registro"].dt.strftime("%d/%m/%Y %H:%M")              
    datos_df["fecha_registro"] = iso                                               
    filas_elegidas = generar_muestra(datos_df, 0.40)
    datos_df.loc[filas_elegidas, "fecha_registro"] = latino.loc[filas_elegidas] 

