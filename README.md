# weather-api-flask

Weather API with Flask

## Principais comandos

### Utilizando venv

#### Instalar virtual environment

```
python3 -m venv venv
```

#### Ativar venv

```
source venv/bin/activate
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
