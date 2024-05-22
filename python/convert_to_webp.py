import os
from PIL import Image

def convert_to_webp(input_folder, output_folder, quality=85):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_path = os.path.join(input_folder, filename)
            with Image.open(image_path) as img:
                webp_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")
                img.save(webp_path, 'webp', quality=quality)
                print(f'Converted {filename} to {webp_path} with quality={quality}')

# Pastas de entrada e saída
input_folders = ['downloaded_images', 'resized_images']
output_folders = ['webp_downloaded_images', 'webp_resized_images']
# Qualidade para compressão lossy (0-100)
quality = 85

# Converter imagens para WebP com compressão lossy
for input_folder, output_folder in zip(input_folders, output_folders):
    convert_to_webp(input_folder, output_folder, quality)