import cloudinary
from cloudinary import uploader, api

# Configura las credenciales de Cloudinary
cloudinary.config(
  cloud_name = "djgwbcthz",
  api_key = "512485342798815",
  api_secret = "4a8N5GWpzbe7IIYm6hhFgq1n_kM"
)

try:
    # Inicializa el parámetro de paginación
    next_cursor = None
    
    # Continúa recorriendo las páginas hasta que no haya más recursos
    while True:
        # Obtiene la lista de recursos de Cloudinary
        resources = api.resources(next_cursor=next_cursor)

        # Verifica si se obtuvieron recursos correctamente
        if "resources" in resources:
            # Itera sobre cada recurso y cambia el nombre de la imagen
            for resource in resources["resources"]:
                antiguo_nombre = resource["public_id"]
                
                # Verifica si el nombre de la imagen sigue el formato "imagen_[int]_[int]_[string].jpg"
                partes_nombre = antiguo_nombre.split("_")
                if len(partes_nombre) == 4:
                    # Revisa si la última parte del nombre es una cadena de caracteres (presumiblemente una extensión)
                    if partes_nombre[-1].isalnum() or partes_nombre[-1].isalpha():
                        
                        # Construye el nuevo nombre eliminando la parte de la cadena
                        nuevo_nombre = "_".join(partes_nombre[:-1])
                        
                        # Renombra la imagen con el nuevo nombre
                        uploader.rename(antiguo_nombre, nuevo_nombre)
                        print(f"Imagen {antiguo_nombre} renombrada como {nuevo_nombre}")
                    else:
                        print(f"Imagen {antiguo_nombre} nO es alpha NO renombrada")
                else:
                    print(f"Imagen {antiguo_nombre} NO renombrada {len(partes_nombre)}")
                
                partes_nombre = antiguo_nombre.split('.')
                if len(partes_nombre) > 1:
                    print(f"partes_nombre jpgjpg {partes_nombre[-1]} y la parte 2 como {partes_nombre[-2]}")

                if len(partes_nombre) > 1 and partes_nombre[-1] == 'jpg' and partes_nombre[-2] == 'jpg':
                    nuevo_nombre = antiguo_nombre[:-8] + ".jpg"
                    
                    # Renombra la imagen con el nuevo nombre
                    uploader.rename(antiguo_nombre, nuevo_nombre)
                    print(f"Imagen jpgjpg {antiguo_nombre} renombrada como {nuevo_nombre}")
                else:
                    print(f"Imagen jpgjpg {antiguo_nombre} NO renombrada")

                        
        else:
            print("No se pudieron obtener los recursos de Cloudinary.")
            break
        
        # Actualiza el cursor de paginación para la siguiente página
        next_cursor = resources.get("next_cursor")
        
        # Si no hay más páginas, salimos del bucle
        if not next_cursor:
            break
except Exception as e:
    print(f"Ocurrió un error al intentar obtener los recursos de Cloudinary: {e}")
