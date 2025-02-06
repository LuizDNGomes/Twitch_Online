import requests
from bs4 import BeautifulSoup

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

# Verificar o status do canal "luizdngomes"
channel_name = "luizdngomes"
online_status = is_channel_online(channel_name)

if online_status:
    print(f"O canal {channel_name} está online no momento.")
else:
    print(f"O canal {channel_name} está offline no momento.")