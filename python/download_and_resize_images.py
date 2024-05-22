import os
from PIL import Image

# Função para redimensionar e cortar a imagem para o tamanho desejado
def resize_and_crop_image(image_path, output_folder, target_size=(1200, 630)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with Image.open(image_path) as img:
        img_width, img_height = img.size
        target_ratio = target_size[0] / target_size[1]
        
        # Verificar se a imagem é menor que o tamanho final
        if img_width < target_size[0] or img_height < target_size[1]:
            # Redimensionar mantendo a proporção
            img_ratio = img_width / img_height
            if img_ratio > target_ratio:
                img = img.resize((target_size[0], int(target_size[0] / img_ratio)), Image.Resampling.LANCZOS)
            else:
                img = img.resize((int(target_size[1] * img_ratio), target_size[1]), Image.Resampling.LANCZOS)
            
            # Criar uma nova imagem com o tamanho desejado e fundo branco
            new_img = Image.new("RGB", target_size, (255, 255, 255))
            new_img.paste(img, ((target_size[0] - img.width) // 2, (target_size[1] - img.height) // 2))
        else:
            # Cortar a imagem mantendo a proporção 1.91:1
            img_ratio = img_width / img_height
            if img_ratio > target_ratio:
                new_width = int(target_ratio * img_height)
                left = (img_width - new_width) / 2
                right = (img_width + new_width) / 2
                img = img.crop((left, 0, right, img_height))
            else:
                new_height = int(img_width / target_ratio)
                top = (img_height - new_height) / 2
                bottom = (img_height + new_height) / 2
                img = img.crop((0, top, img_width, bottom))
            
            img = img.resize(target_size, Image.Resampling.LANCZOS)
            new_img = img
        
        output_path = os.path.join(output_folder, os.path.basename(image_path))
        new_img.save(output_path)
        print(f'Resized and saved: {output_path}')

# Caminho para a pasta com as imagens baixadas
download_folder = 'downloaded_images'
# Pasta onde as imagens redimensionadas e cortadas serão salvas
output_folder = 'resized_images'
# Tamanho para o corte (largura, altura)
target_size = (1200, 630)

# Redimensionar e cortar as imagens existentes na pasta download_folder
for filename in os.listdir(download_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        image_path = os.path.join(download_folder, filename)
        resize_and_crop_image(image_path, output_folder, target_size)