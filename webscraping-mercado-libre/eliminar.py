import cloudinary
from cloudinary import api

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
            # Itera sobre cada recurso y elimina la imagen
            for resource in resources["resources"]:
                public_id = resource["public_id"]
                api.delete_resources([public_id])
                print(f"Imagen {public_id} eliminada correctamente.")
        else:
            print("No se pudieron obtener los recursos de Cloudinary.")
            break
        
        # Actualiza el cursor de paginación para la siguiente página
        next_cursor = resources.get("next_cursor")
        
        # Si no hay más páginas, salimos del bucle
        if not next_cursor:
            break
except Exception as e:
    print(f"Ocurrió un error al intentar eliminar los recursos de Cloudinary: {e}")
