# Segmentación de Periódicos

Este script procesa imágenes de periódicos y genera archivos JSON que contienen la segmentación de los elementos de las páginas. Utiliza la función `run_newspaper_segmentation` del cliente `newspaper_segmentation_client`.

## Descripción

El script toma una lista de rutas de imágenes de periódicos, las procesa a través de una API de segmentación y guarda los resultados en archivos JSON. Cada imagen se convierte en un archivo JSON que describe la segmentación de la página.

## Uso

1. Clona el repositorio y navega al directorio del proyecto.
2. Instala las dependencias necesarias.
3. Asegúrate de tener una clave API válida para el servicio de segmentación.
4. Edita la lista de rutas de imágenes y la clave API según tus necesidades.
5. Ejecuta el script para procesar las imágenes.

## Ejemplo de Uso

```
API_KEY = "api_key_arcanum"
DPI=150
IMAGE_PATHS = [
    "imagen1.jpg", 
    "imagen2.jpg"
]
process_images_to_json(IMAGE_PATHS, API_KEY, DPI)
```

### Parámetros
- `image_paths`: Lista de rutas a las imágenes de periódicos que se desean procesar.
- `api_key`: Clave API para acceder al servicio de segmentación.
- `dpi`: Resolución de la imagen en puntos por pulgada (DPI). El valor predeterminado es 150.

### Salida
El script genera un archivo JSON por cada imagen procesada, con el mismo nombre que la imagen original y un sufijo `_arcanum`.
