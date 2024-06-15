from newspaper_segmentation_client import run_newspaper_segmentation
import json
import os

def process_images_to_json(image_paths, api_key, dpi=DPI):
    for image_path in image_paths:
        # Nombre del archivo JSON de salida
        base_name = os.path.splitext(image_path)[0]  # Obtiene el nombre del archivo sin extensión
        output_json = f"{base_name}_arcanum.json"
        
        # Procesar la imagen
        with open(image_path, "rb") as image_file:
            json_arcanum = json.dumps(run_newspaper_segmentation(image_file, api_key=api_key, dpi=dpi))
        
        # Guardar el JSON en un archivo
        with open(output_json, 'w') as json_file:
            json_file.write(json_arcanum)
