import requests
import mysql.connector
import os

# Función para descargar una imagen y guardarla localmente
def descargar_imagen(url, nombre_archivo):
    response = requests.get(url)
    with open(nombre_archivo, 'wb') as f:
        f.write(response.content)

# Configuración de la conexión a la base de datos MySQL
conexion_mysql = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3308,
    password="toor",
    database="doremi_db"
)
cursor_mysql = conexion_mysql.cursor()

# Función para guardar datos en la base de datos
def guardar_en_db(nombre, descripcion, precio_dia, categoria_id, imagenes):
    # Insertar el instrumento en la tabla instrumento
    cursor_mysql.execute("""
        INSERT INTO instrumento (nombre, descripcion, precio_dia, categoria_id)
        VALUES (%s, %s, %s, %s)
    """, (nombre, descripcion, precio_dia, categoria_id))
    conexion_mysql.commit()
    instrumento_id = cursor_mysql.lastrowid
    
    # Insertar las imágenes en la tabla imagen
    for i, imagen in enumerate(imagenes):
        titulo = f"Imagen {i+1}"
        url = imagen['url']
        
        # Guardar la imagen localmente
        nombre_archivo = f"imagen_{instrumento_id}_{i+1}.jpg"
        descargar_imagen(url, nombre_archivo)
        
        # Insertar la imagen en la tabla imagen
        cursor_mysql.execute("""
            INSERT INTO imagen (instrumento_id, titulo, url)
            VALUES (%s, %s, %s)
        """, (instrumento_id, titulo, nombre_archivo))
        conexion_mysql.commit()

# Obtener datos de la API de Mercado Libre
url_api = "https://api.mercadolibre.com/sites/MCO/search?q=instrumentos%20musicales"
response = requests.get(url_api)
data = response.json()

# Procesar los datos obtenidos
for item in data['results']:
    item_id = item['id']
    url_item_api = f"https://api.mercadolibre.com/items/{item_id}"
    response_item = requests.get(url_item_api)
    data_item = response_item.json()
    
    nombre = data_item['title']
    imagenes = data_item['pictures'][:5]
    
    descripcion = ", ".join([f"{attr['name']}: {attr['value_name']}" for attr in data_item['attributes'][:5]])
    precio_dia = 0.0  # No hay información sobre el precio por día en los datos de la API
    categoria_id = 1  # Supongamos que todos los instrumentos pertenecen a la categoría 1
    
    # Guardar en la base de datos y tabla imagen
    guardar_en_db(nombre, descripcion, precio_dia, categoria_id, imagenes)

# Cerrar la conexión a la base de datos
cursor_mysql.close()
conexion_mysql.close()
