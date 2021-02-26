from bs4 import BeautifulSoup

#substitua o nome do arquivo para leitura
with open("Lorem Ipsum - All the facts - Lipsum generator.html", 'r') as file:
    data = file.read()

soup = BeautifulSoup(data, 'html.parser')

all_links = soup.find_all('a')

for link in all_links:
    print(link)
    
