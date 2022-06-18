# ScannerMicroService

## Observação

Os comandos em python podem ser inicializados ou por `python3` ou por `py` dependendo da configuração da variável global e se python2 está instalado

## Criando ambiente virtual

Para criar um ambiente virutal no Windows bastar utilizar os comandos:

`python3 -m venv nomeDoAmbiente` ou `py -m venv nomeDoAmbiente`

O ambiente virtual irá conter todos os pacotes necessários da aplicação sem ter a necessidade de instala-los globalmente.
## Inicializando ambiente

Para iniciar o ambiente virtual no ambiente Windows abra o powershell e digite `venv/Scripts/activate`

## Instalando pacotes

Para installar um pacote local devemos ativar a venv (passo acima) e utilizar o comando `pip install nomePacote`.
Também é possível utilizar um arquivo de texto para instalar vários pacotes de uma vez (normalmente esse txt contém todos os pacotes utilizado pela venv)
`pip install -r requirements.txt`
Com o arquivo requirements.txt nesse repositório já teremos o necessário para rodar.

## Rodando API flask SIMPLES

Com a venv aberta utilize o comando `py main.py`, com isso, teremos a API rodando.

## EndPoints

Por tratar de testes, estaremos num ambiente local portanto (localhost)

No caminho inicial apenas teremos uma mensagem padrão 'Scanner Funfa'

home -> localhost:portaPadrãoFlask/

No caminho birdView, temos apenas o method post aplicado que atualmente apenas recebe um arquivo (Da para mundar para apenas json via codificação base64). 
De resposta após teremos o retorno da imagem com a bird view aplicada no formato base 64 (não tem nenhum tratamento no momento em relação aos request e response)

birdView -> localhost:portaPadrãoFlask/birdView

## Verificando Retorno

No repositório temos um arquivo que envia uma imagem e descodifica a resposta da API e mostra o resultado, para executa-lo escreva com a venv aberta `py caminho/testeImagemRetornada`



