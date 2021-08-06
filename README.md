# weather-api-flask

Weather API with Flask

API que busca os dados climáticos de uma cidade no Clima Tempo e persiste os dados em um banco de dados relacional SQLite.

## Sumário

1. [Endpoints](#endpoints)

   1.1. [/cidade](#/cidade)
  
   1.1. [/analise](#/analise) 
  
   1.1. [/cidades](#/cidades)

2. [Comandos principais](#principais-comandos)

### Endpoints <a name="endpoints" />

#### /cidade?id=<ID_CIDADE> <a name="/cidade" />

Busca as informações climáticas da cidade a partir de seu ID na API do Clima Tempo e persiste os dados em um banco de dados SQLite.

**Method:** GET

**Exemplos de IDs de cidades:**

- São Carlos, SP: 3680
- Lavras, MG: 8810
- São Paulo, SP: 3477

#### /analise?data_inicial=<DATA_INICIAL>&data_final=<DATA_FINAL> <a name="/analise" />

Realiza uma análise nos dados coletados. Informa em formato JSON a cidade com maior temperatura (**cityWithHigherTemperature**) e a média de precipitação por cidade (**precipitationAverage**).

Formato de data esperado:
- **data_inicial:** 2021-08-01
- **data_final:** 2021-08-20

**Method:** GET

#### /cidades <a name="/cidades" />

Lista todas as cidades já salvas no banco de dados.

**Method:** GET

### Principais comandos <a name="principais-comandos" />

#### Utilizando o docker-compose (recomendado)

##### Para subir os serviços

```
docker-compose up
```

##### Para subir os serviços em background

```
docker-compose up -d
```

#### Utilizando Docker

##### Para criar a imagem

```
docker build -t weather .
```

##### Para rodar o container

```
docker run -p 5000:5000 weather
```

##### Para rodar o container em background

```
docker run -dp 5000:5000 weather
```

#### Utilizando venv

##### Instalar virtual environment

```
python3 -m venv venv
```

##### Ativar venv

```
source venv/bin/activate
```

##### Para rodar os testes

```
python src/tests.py
```

##### Para rodar a aplicação

```
python src/app.py
```
