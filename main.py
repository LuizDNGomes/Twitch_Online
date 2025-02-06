import re

# Função para verificar se o canal está online a partir do conteúdo do arquivo
def is_channel_online(file_content):
    # Expressão regular para encontrar o status online
    pattern = re.compile(r'"isLiveBroadcast":true')
    match = pattern.search(file_content)
    return bool(match)

# Função para extrair o nome do streamer a partir do conteúdo do arquivo
def extract_streamer_name(file_content):
    # Expressão regular para encontrar o nome do streamer
    pattern = re.compile(r'channel=(\w+)&amp;')
    match = pattern.search(file_content)
    if match:
        return match.group(1)
    return None

# Função para verificar o status online de um canal específico
def check_channel_status(channel_name):
    try:
        # Ler o conteúdo do arquivo
        with open(f'{channel_name}.txt', 'r', encoding='utf-16') as f:
            file_content = f.read()

        # Extrair o nome do streamer
        streamer_name = extract_streamer_name(file_content)

        if streamer_name:
            print(f"O streamer atualmente transmitindo é: {streamer_name}")
            # Verificar se o canal está online
            online_status = is_channel_online(file_content)
            if online_status:
                print("O canal está online no momento.")
            else:
                print("O canal está offline no momento.")
        else:
            print("Nome do streamer não encontrado no arquivo.")
    except FileNotFoundError:
        print(f"Arquivo {channel_name}.txt não encontrado.")

# Perguntar ao usuário o nome do canal
channel_name = input("Digite o nome do canal que você quer consultar: ")
check_channel_status(channel_name)