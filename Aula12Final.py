import requests
cep = int(input('Entre com CEP, só números e 8 dígitos: '))

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    #print(response.status_code)
    #print(response.json())
    # retorna todos os dados da request feita pela api
    # print(type(response.json()))
    # descubra o tipo da resposta
    dados_cep = response.json()
    print(dados_cep['cep'])
    print(dados_cep['logradouro'])
    print(dados_cep['bairro'])
    print(dados_cep['localidade'])
    print(dados_cep['uf'])
    print(dados_cep['ddd'])
    return dados_cep
if __name__ == '__main__':
    retorna_dados_cep(cep)
