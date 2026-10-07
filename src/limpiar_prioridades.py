import os
import sys
import pandas as pd

# 1. Mapeos de negocio para estandarización e imputación
MAPA_PALABRAS_A_NUM = {
    "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5
}

NIVELES_REGLA = {
    "Urgente": 1,
    "Alta": 2,
    "Media": 3,
    "Baja": 4,
    "Planificada": 5,
}

DIAS_REGLA = {
    1: 1,    # Urgente -> 1 día
    2: 3,    # Alta -> 3 días
    3: 7,    # Media -> 7 días
    4: 15,   # Baja -> 15 días
    5: 30,   # Planificada -> 30 días
}

def limpiar_datos():
    # Definir rutas
    DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
    CARPETA_RAIZ = os.path.dirname(DIRECTORIO_ACTUAL)
    
    ruta_entrada = os.path.join(CARPETA_RAIZ, "data", "crudo", "prioridades_sucio.csv")
    carpeta_salida = os.path.join(CARPETA_RAIZ, "data", "limpio")
    ruta_salida = os.path.join(carpeta_salida, "prioridades_limpio.csv")

    if not os.path.exists(ruta_entrada):
        print(f"❌ Error: No se encontró el archivo de entrada en '{ruta_entrada}'. Ejecuta exportar_prioridades.py primero.")
        return

    # Cargar dataset sucio
    df = pd.read_csv(ruta_entrada)
    filas_iniciales = len(df)
    print(f"📊 Cargado dataset sucio: {df.shape}")

    # A. Eliminar duplicados
    df = df.drop_duplicates()
    duplicados_eliminados = filas_iniciales - len(df)

    # B. Estandarizar columna 'nombre'
    df["nombre"] = df["nombre"].astype(str).str.strip().str.title()

    # C. Homogeneizar columna 'nivel'
    def corregir_nivel(row):
        val = row["nivel"]
        if pd.isna(val) or str(val).strip().lower() in ["none", "nan", ""]:
            # Imputar desde el nombre de prioridad si el nivel es nulo
            return NIVELES_REGLA.get(row["nombre"], None)
        
        val_str = str(val).strip().lower()
        if val_str in MAPA_PALABRAS_A_NUM:
            return MAPA_PALABRAS_A_NUM[val_str]
        try:
            val_int = int(float(val_str))
            if 1 <= val_int <= 5:
                return val_int
        except ValueError:
            pass
        
        return NIVELES_REGLA.get(row["nombre"], None)

    df["nivel"] = df.apply(corregir_nivel, axis=1)

    # D. Corregir y deducir 'dias_max_respuesta'
    def corregir_dias(row):
        val = row["dias_max_respuesta"]
        # Si es nulo o es un valor absurdo (ej. 999), se calcula según la regla del nivel
        try:
            val_float = float(val)
            if pd.isna(val) or val_float >= 100 or val_float <= 0:
                return DIAS_REGLA.get(row["nivel"], None)
            return int(val_float)
        except (ValueError, TypeError):
            return DIAS_REGLA.get(row["nivel"], None)

    df["dias_max_respuesta"] = df.apply(corregir_dias, axis=1)

    # Convertir tipos a enteros limpios
    df["nivel"] = df["nivel"].astype(int)
    df["dias_max_respuesta"] = df["dias_max_respuesta"].astype(int)

    # E. Guardar dataset limpio
    os.makedirs(carpeta_salida, exist_ok=True)
    df.to_csv(ruta_salida, index=False, encoding="utf-8")

    # Muestra de resultados
    print("\n✅ LIMPIEZA COMPLETADA CON ÉXITO")
    print(f"  • Filas iniciales: {filas_iniciales}")
    print(f"  • Duplicados eliminados: {duplicados_eliminados}")
    print(f"  • Nulos / Inconsistencias corregidas en nivel y días: {df.isna().sum().sum()}")
    print(f"  • Ruta guardada: '{ruta_salida}'")
    print(f"  • Dimensiones finales: {df.shape}")

if __name__ == "__main__":
    limpiar_datos()