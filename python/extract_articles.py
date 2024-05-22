import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL do site que você quer fazer o scraping
url = 'https://sinduscon-nortepr.com.br/noticia'

# Fazer a requisição para o site
response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Failed to load page {url}")

# Parsear o conteúdo da página
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar os artigos (o seletor pode variar dependendo do site)
articles = soup.find_all('div', class_='card-body')

# Lista para armazenar os dados dos artigos
data = []

# Extrair informações de cada artigo
for article in articles:
    title = article.find('h5', class_='card-title').get_text(strip=True) if article.find('h5', class_='card-title') else 'No title'
    link = article.find('a')['href'] if article.find('a') else 'No link'
    date = article.find('p', class_='card-text').get_text(strip=True) if article.find('p', class_='card-text') else 'No date'
    summary = article.find('p', class_='card-text').get_text(strip=True) if article.find('p', class_='card-text') else 'No summary'
    
    # Adicionar os dados à lista
    data.append({
        'Title': title,
        'Link': f'https://sinduscon-nortepr.com.br{link}',
        'Date': date,
        'Summary': summary
    })

# Converter a lista de dados em um DataFrame do pandas
df = pd.DataFrame(data)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('articles.csv', index=False)

print("Scraping completed and data saved to articles.csv")