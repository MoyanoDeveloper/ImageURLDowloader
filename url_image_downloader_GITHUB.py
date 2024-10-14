import os
import requests
import re
from time import sleep


def limpiar_nombre(nombre):
    # Reemplazar caracteres inválidos por un guion bajo
    nombre_limpio = re.sub(r'[<>:"/\\|?*]', '_', nombre)
    return nombre_limpio

lista_nombres=['']

lista_imagenes=['']

base_dir = "imagenes_soportepublicitario"

# Crear el directorio base si no existe
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# Iterar sobre las listas
for index, (nombre, url) in enumerate(zip(lista_nombres, lista_imagenes)):
    # Limpiar el nombre de la carpeta
    nombre_limpio = limpiar_nombre(nombre)
    
    # Si el nombre ya existe, añadir un sufijo para hacer el nombre de la carpeta único
    carpeta_path = os.path.join(base_dir, nombre_limpio)
    if os.path.exists(carpeta_path):
        carpeta_path = os.path.join(base_dir, f"{nombre_limpio}_{index}")

    os.makedirs(carpeta_path, exist_ok=True)
    
    # Descargar la imagen
    try:
        response = requests.get(url)
        response.raise_for_status()  # Para lanzar una excepción si la descarga falla

        # Guardar la imagen en la carpeta correspondiente, añadiendo un sufijo al nombre del archivo si ya existe
        imagen_nombre = f"{nombre_limpio}.jpg"
        imagen_path = os.path.join(carpeta_path, imagen_nombre)
        if os.path.exists(imagen_path):
            imagen_nombre = f"{nombre_limpio}_{index}.jpg"
            imagen_path = os.path.join(carpeta_path, imagen_nombre)
        
        with open(imagen_path, "wb") as file:
            file.write(response.content)
        
        print(f"Imagen descargada y guardada en: {imagen_path}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar {url}: {e}")
    
    sleep(2)

print("Proceso de descarga completado.")
