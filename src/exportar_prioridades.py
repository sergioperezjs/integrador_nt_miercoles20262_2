import os
import sys
import pandas as pd

# Ajustar ruta para importar simular_prioridades correctamente
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
if DIRECTORIO_ACTUAL not in sys.path:
    sys.path.append(DIRECTORIO_ACTUAL)

# Importar la función directamente del script hermano
from simular_prioridades import generar_prioridades

def exportar_datos():
    # 1. Crear la ruta data/crudo desde la raíz
    CARPETA_RAIZ = os.path.dirname(DIRECTORIO_ACTUAL)
    CARPETA_SALIDA = os.path.join(CARPETA_RAIZ, "data", "crudo")
    os.makedirs(CARPETA_SALIDA, exist_ok=True)

    # 2. Generar DataFrame
    df = generar_prioridades()

    # 3. Rutas de archivos
    ruta_csv = os.path.join(CARPETA_SALIDA, "prioridades_sucio.csv")
    ruta_xlsx = os.path.join(CARPETA_SALIDA, "prioridades_sucio.xlsx")
    ruta_json = os.path.join(CARPETA_SALIDA, "prioridades_sucio.json")

    # 4. Exportar en los 3 formatos
    df.to_csv(ruta_csv, index=False, encoding="utf-8")
    print(f"✅ Exportado CSV  -> Ruta: '{ruta_csv}' | Dimensiones: {df.shape}")

    df.to_excel(ruta_xlsx, index=False, sheet_name="prioridades")
    print(f"✅ Exportado XLSX -> Ruta: '{ruta_xlsx}' | Dimensiones: {df.shape}")

    df.to_json(ruta_json, orient="records", force_ascii=False, indent=2)
    print(f"✅ Exportado JSON -> Ruta: '{ruta_json}' | Dimensiones: {df.shape}")

if __name__ == "__main__":
    exportar_datos()