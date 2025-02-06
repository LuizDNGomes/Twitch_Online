import requests
from bs4 import BeautifulSoup
import time
import webbrowser
from datetime import datetime

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
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M')
        if online_status:
            print(f"[{timestamp}] O canal {channel_name} está online no momento.")
            webbrowser.open(f"https://www.twitch.tv/{channel_name}")
            break
        else:
            print(f"[{timestamp}] O canal {channel_name} está offline no momento. Verificando novamente em 5 minutos...")
            time.sleep(300)  # Esperar 5 minutos antes de verificar novamente

# Função para assistir ao canal e verificar se ele fica offline
def watch_channel(channel_name):
    while True:
        online_status = is_channel_online(channel_name)
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M')
        if not online_status:
            print(f"[{timestamp}] O canal {channel_name} ficou offline. Encerrando o navegador.")
            break
        else:
            print(f"[{timestamp}] O canal {channel_name} ainda está online. Verificando novamente em 5 minutos...")
            time.sleep(300)  # Esperar 5 minutos antes de verificar novamente




#channel_name = input("Digite o nome do canal que você quer monitorar: ")

channel_name = 'Luizdngomes'

# Leia com atenção!

"""

Para fixar o canal a monitorar:

#channel_name = input("Digite o nome do canal que você quer monitorar: ")

channel_name = 'nome do canal'

------------------------------------------------

Para ser questionado toda vez:

channel_name = input("Digite o nome do canal que você quer monitorar: ")

#channel_name = 'Luizdngomes'


"""

monitor_channel(channel_name)
watch_channel(channel_name)