import requests
from bs4 import BeautifulSoup

#------------------------------------------------
# Nessa versão o código apenas informa se o canal está ou não online
# Se sim ou se não, ele informa ao usuário o status e pede um novo canal
# Se o usuário digitar 'sair', o programa encerra


# TODO: Código deve abrir a página e ficar assistindo até o canal ficar online, se online, informar ao usuário e fechar a página. Verificar a cada 5 minutos
#------------------------------------------------

def is_channel_online(channel_name):
    url = f"https://www.twitch.tv/{channel_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Verificar o meta tags 'isLiveBroadcast'
    meta_tags = soup.find_all('meta')
    for meta in meta_tags:
        if 'isLiveBroadcast' in str(meta):
            if 'true' in str(meta):
                return True
            else:
                return False
    return False

# Loop para continuar perguntando ao usuário até que ele decida sair
while True:
    channel_name = input("Digite o nome do canal que você quer consultar (ou 'sair' para encerrar): ")
    if channel_name.lower() == 'sair':
        break
    online_status = is_channel_online(channel_name)

    if online_status:
        print(f"O canal {channel_name} está online no momento.")
    else:
        print(f"O canal {channel_name} está offline no momento.")