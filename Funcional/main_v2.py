import requests
from bs4 import BeautifulSoup
import time
import webbrowser

# Função para verificar se o canal está online a partir da página da Twitch
def is_channel_online(channel_name):
    url = f"https://www.twitch.tv/{channel_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Verificar o status online nos meta tags
    meta_tags = soup.find_all('meta')
    for meta in meta_tags:
        if 'isLiveBroadcast' in str(meta):
            if 'true' in str(meta):
                return True
            else:
                return False
    return False

# Função para monitorar o canal até que ele fique online e abrir o navegador
def monitor_channel(channel_name):
    while True:
        online_status = is_channel_online(channel_name)
        if online_status:
            print(f"O canal {channel_name} está online no momento.")
            webbrowser.open(f"https://www.twitch.tv/{channel_name}")
            break
        else:
            print(f"O canal {channel_name} está offline no momento. Verificando novamente em 5 minutos...")
            time.sleep(300)  # Esperar 5 minutos antes de verificar novamente

# Função para assistir ao canal e verificar se ele fica offline
def watch_channel(channel_name):
    while True:
        online_status = is_channel_online(channel_name)
        if not online_status:
            print(f"O canal {channel_name} ficou offline. Encerrando o navegador.")
            break
        else:
            print(f"O canal {channel_name} ainda está online. Verificando novamente em 5 minutos...")
            time.sleep(300)  # Esperar 5 minutos antes de verificar novamente


# Leia com atenção!


channel_name = input("Digite o nome do canal que você quer monitorar: ")
#channel_name = 'Luizdngomes'

"""
Para fixar o canal a monitorar basta descomentar o channel_name e inserir entre as aspas o nome do canal

Para ser questionado toda vez, channel_name = input deve estar descomentado e o channel_name = 'Luizdngomes' deve estar comentado

"""

monitor_channel(channel_name)
watch_channel(channel_name)