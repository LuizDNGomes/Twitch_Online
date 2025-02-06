Este código faz o seguinte:

Pergunta ao usuário o nome do canal que ele quer consultar.
Lê o conteúdo do arquivo correspondente ao canal.
Extrai o nome do streamer do conteúdo do arquivo.
Verifica se o canal está online com base nos metadados do arquivo.
Exibe o status do canal (online ou offline).

To do:
#Pensando
 
>main_v1.py:

>> Nessa versão o código apenas informa se o canal está ou não online
>> Se sim ou se não, ele informa ao usuário o status e pede um novo canal
>> Se o usuário digitar 'sair', o programa encerra
----------------------------------------------------------------------

>main_v2.py:


>> Pergunta ao usuário o nome do canal que ele quer monitorar.
>> Acessa a página da Twitch do canal especificado.
>> Analisa o conteúdo da página para encontrar os metadados que indicam se o canal está online.
>> Se o canal estiver online, abre o navegador e começa a assistir ao canal.
>> Verifica a cada 5 minutos se o canal ainda está online.
>> Se o canal ficar offline, encerra o navegador e avisa ao usuário.

>main_v2.py:

>> Correção para aparecer o dia e hora a cada prompt
>> Melhorias nos comentários


OBS: 

>>Para fixar o canal a monitorar:

>>>#channel_name = input("Digite o nome do canal que você quer monitorar: ")

>>>channel_name = 'nome do canal'

------------------------------------------------

>>Para ser questionado toda vez:

>>>channel_name = input("Digite o nome do canal que você quer monitorar: ")

>>>#channel_name = 'Luizdngomes'
