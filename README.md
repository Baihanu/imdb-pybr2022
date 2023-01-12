# imdb-pybr2022


Repositório do Tutorial de [Raspagem de Dados IMBD](https://pretalx.com/python-brasil-2022/talk/JGXM7G/) para a Python Brasil 2022.



## Para Desenvolver:

1. Clone o repositório.
2. Crie um virtualenv com Python 3.9.
3. Ative o virtualenv.
4. Instale as dependências.
5. Adicione as variáveis de ambiente referentes à sua realidade.

### Ambientes Linux:
```
python3 -m venv .venv
source .venv/bin/activate
cp env-sample .env
pip install -r requirements.txt
```
### Ambientes Windows:
```
Set-ExecutionPolicy Unrestricted -Scope Process
py -3 -m venv .venv
.venv\Scripts\activate
copy env-sample .env
pip install -r requirements.txt
```
### Caso queira liberar os scripts como Admnistrador no Ambiente Windows:
[Clique aqui](https://docs.vmware.com/en/vRealize-Automation/7.6/com.vmware.vra.iaas.hp.doc/GUID-9670AFC5-76B8-4321-822A-BCE05800DB5B.html)

# Para Rodar o Código:
```
python -m imdb
```