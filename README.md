
## Configuração de ambiente  

**Passo 1**  
Verifique a versão do python3.  
      ``$ python3 --version``  

**Passo 2**  
Se não existe, execute:  
**Ubuntu**  
      ``$ sudo apt-get install python3.4``  

Feito isso, é necessário instalar o ambiente virtual (**virtualenv**).  
**Passo 3**  
Verifique se já tem o virtualenv:  
	``$ virtualenv --version``  
	
**Passo 4**  
Se não tem instale, execute:  
	``$ sudo apt-get install python-virtualenv``  

**Passo 5**   
Crie o ambiente virtual:  
	``python3 -m venv virtual``  

**Passo 6**  
Ative o ambiente virtual:  
	``$ source virtual/bin/activate``  

Ao final disso o terminal deve estar dessa forma:  
	``(virtual) ~/my_app $``  

Instale as dependências:
 ``pip install -r requirements.txt``

## Executando a aplicação
Com as dependências instaladas basta executar o comando:
	``python3 gibblauncher-api.py``

Agora, acesse acesse a seguinte url no seu navegador:
	``localhost:5000``
