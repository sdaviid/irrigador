>This is a proposal test project

## Proposta

O projeto foi desenvolvido na base de um cenário fictício, a ideia é um sistema que guarda os dados de plantas, irrigadores, os dias da semana, horário e por quanto tempo devera regar uma planta.

Em um cenário real seria necessário cadastrar um irrigador, as plantas a qual pertence, determinar horários/dias da semana e tempo para regar, e neste irrigador configura-lo para comunicar-se a API fazendo o check do que e quando deverá regar uma planta.

O irrigador também tera que enviar uma resposta para o endpoint de log para determinar se houve sucesso ou não.

Como eu não tenho experiencia em detalhes sobre uma plantação, alguns detalhes como Ph da água, quantidade de água usada e não entendo o mundo das plantas, decidi não guardar essas informações no sistema para não haver equívocos.

Na proposta foi definido a criação de CRUDs para realizar ações assim como modelagem de seus objetos.

## Execução

Primeiramente instalar as dependências

```sh
python -m pip install -r requirements.txt
```

E então

```sh
uvicorn app.main:app
```
E poderá acessar os docs a partir de:

[localhost:8000/docs](localhost:8000/docs)
[localhost:8000/redoc](localhost:8000/redoc)

## Funcionamento

O sistema possui 4 controles: irrigador, planta, dia para regar, log

O primeiro passo é criar a identidade para o irrigador, adicionar as plantas e o identificador do irrigador, cadastrar os dias da semana, horário e tempo que devera manter ativo o processo de regar, por fim para controle adicionar o log se foi bem sucedido ou não.

## Testes

Os testes se encontram na pasta ``tests/``

Para executa-lo

```sh
python -m pytest -v
```