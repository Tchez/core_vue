# Projeto core_vue

    Adding Vue

## Cliente

> Nome do Cliente

## Dados do Projeto

> **Data da Criação** : 08/08/2023  
> **Django Version** : 4.2  
> **Python Version**: 3.10  
> **PostgreSQL Version** : 14.2

## Analista Responsável

> Marco  
> agtec@palmas.to.gov.br

### Gerando a nova Secret Key

Para gerar uma nova SecretKey a ser utilizada no arquivo .env execute o comando a seguir (com o virtualenv ativado)

```shell
python contrib/secret_gen.py  
```

----

## Deploy

### Para realizar o deploy do projeto em ambiente de homologação deve-se seguir os seguintes passos

[ ] Adicionar o diretório static do core no sistema de versionamento

### Para realizar o deploy do projeto em ambiente de produção deve-se seguir os seguintes passos

[ ] Configurar o arquivo com as variáveis de ambiente docker-compose.yml  
[ ] Configurar o arquivo Dockerfile

----

## Docker

### Como utilizar

Caso deseje desenvolver utilizando a tecnologia de containers (Docker) listamos abaixo os comandos para executar no
projeto

> Para usuários Windows é necessário garantir que o WSL2 esteja configurado e tenha instalado o Docker Desktop

### Criando a imagem e executando o container

```shell
docker-compose up -d
```

### Executando em ambiente de desenvolvimento

```shell
docker-compose --f docker-dev.yml up -d
```

### Forçando a geração da nova imagem e container

```shell
docker-compose -f docker-dev.yml up -d --force-recreate --no-deps
```

### Mostrando as imagens geradas

```shell
docker images ls
```

### Mostrando os containers gerados

```shell
docker container ls
```

### Acessando o terminal de um container executando em backgroud

```shell
docker container exec -it core_vue_django bash
```

### Saindo do terminal de um container que foi acesso via comando exec, sem **manter o container**

    CTRL + P, CTRL + Q

### Criando a SECRET_KEY

```shell
docker container exec -it core_vue_django bash -c "python contrib/secret_gen.py"
```

O comando acima retorna uma string similar a esta
***gvN3L7UR_4ADJrUjnLGdjzZuvFoT01gqYyFfQkY0Qava7DigkWS63YP8UBl7saAcV3E***

### Executando o makemigrations

```shell
docker container exec -it core_vue_django bash -c "python manage.py makemigrations"
```

### Executando o migrations

```shell
docker container exec -it core_vue_django bash -c "python manage.py migrate"    
```

### Executando o build da app Usuario

```shell
docker container exec -it core_vue_django bash -c "python manage.py build usuario"
```

### Executando o comando para gerar o SuperUser

```shell
docker container exec -it core_vue_django bash -c "python mock_superuser.py"
```

### Executando o comando para gerar os dados Fake do models Usuario

```shell
docker container exec -it core_vue_django bash -c "python mock_data.py"
```

### Criando uma nova app

```shell
docker container exec -it core_vue_django bash -c "python manage.py startapp NomeDaNovaApp"
```

### Container`s do Projeto

> Django core_vue_django
> PostgreSQL core_vue_database

### Network do Projeto

> core_vue_network

### Dados do container do PostgreSQL

> Nome do Banco de Dados: core_vue_db
> Usuário do Banco de Dados: core_vue_dbmanager_2LiyBoLHeHo5yG
> Senha do Banco de Dados: senha_padrao_deve_ser_mudada
> Volume: core_vue_db

### Acessando o projeto no navegador

http://localhost:8000

----

## Licença

[MIT](https://mit-license.org/)

Powered By

![Python](https://www.python.org/static/img/python-logo.png)
![Django](https://static.djangoproject.com/img/logo-django.42234b631760.svg)
