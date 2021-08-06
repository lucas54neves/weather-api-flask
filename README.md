# weather-api-flask

Weather API with Flask

## Principais comandos

### Utilizando o docker-compose (recomendado)

#### Para subir os serviços

```
docker-compose up
```

#### Para subir os serviços em background

```
docker-compose up -d
```

### Utilizando Docker

#### Para criar a imagem

```
docker build -t weather .
```

#### Para rodar o container

```
docker run -p 5000:5000 weather
```

#### Para rodar o container em background

```
docker run -dp 5000:5000 weather
```

### Utilizando venv

#### Instalar virtual environment

```
python3 -m venv venv
```

#### Ativar venv

```
source venv/bin/activate
```

#### Para rodar os testes

```
python src/tests.py
```

#### Para rodar a aplicação

```
python src/app.py
```
