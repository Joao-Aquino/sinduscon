import os
import requests

# Função para baixar uma imagem a partir de uma URL
def download_image(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.join(folder, url.split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'Downloaded: {filename}')
    else:
        print(f'Failed to download: {url}')

# Ler URLs do arquivo de texto e baixar as imagens
def download_images_from_file(file_path, folder):
    with open(file_path, 'r') as file:
        urls = file.readlines()
        for url in urls:
            url = url.strip()
            if url:
                download_image(url, folder)

# Caminho para o arquivo com as URLs
file_path = 'image_urls.txt'
# Pasta onde as imagens serão salvas
folder = 'downloaded_images'

# Baixar as imagens
download_images_from_file(file_path, folder)