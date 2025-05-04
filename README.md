# 🚀 Desafio: Configurações de Ambiente com Docker Compose

Projeto desenvolvido como parte do desafio da [Rocketseat](https://www.rocketseat.com.br/) para configurar ambientes com Docker Compose.

## 📄 Descrição

Este projeto consiste em uma aplicação Python (`app.py`) que se conecta a um banco de dados MySQL. A configuração do ambiente é feita utilizando `Dockerfile` e `docker-compose.yml`, que definem dois serviços principais:

- **app**: aplicação Python
- **mysql**: banco de dados MySQL

## 📦 Estrutura dos Contêineres

### 🐍 Serviço `app` (Python)

- Arquivo principal: `app.py`
- Construído a partir de um `Dockerfile` próprio
- Conectado ao MySQL por meio de uma rede Docker

### 🐬 Serviço `mysql`

- Imagem oficial do MySQL
- Volume configurado para persistência dos dados
- Variáveis de ambiente definidas no `docker-compose.yml`, como senha de root e nome do banco

## 🔐 Variáveis de Ambiente

As variáveis estão configuradas diretamente no arquivo `docker-compose.yml`. Entre elas:

- `MYSQL_ROOT_PASSWORD`: define a senha do usuário root do MySQL
- `MYSQL_DATABASE`: define o nome do banco que será criado

## 📁 Volumes

Um volume é utilizado para garantir que os dados do banco de dados persistam mesmo após o container ser encerrado.

## 🌐 Rede

Todos os serviços estão conectados à mesma rede Docker personalizada chamada `primeira-rede`, permitindo a comunicação entre os containers.

## ▶️ Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/CharlesThomaz/DesafioConfiguracaoAmbienteDockerComposeRocketSeat.git
   cd seu-repositorio
