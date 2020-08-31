Controle de Estoque
Como rodar o projeto?

    Clone esse repositório
    Crie um virtualenv com Python 3.
    Ative a virtualenv
    Instale as dependências
    Rode as migrações

    1- git clone https://github.com/WellingtonMarinho13/estoque.git
    2- cd estoque 
    3- python3 -m venv .venv 
    4- source .venv/bin/activate 
    5- pip install -r requirements.txt 
    6- python contrib/env_gen.py 
    7- python manage.py migrate
