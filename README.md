# SCTEC Challenge – Enterprise API

API REST desenvolvida em **Django Rest Framework** para gerenciamento de empreendimentos.  
A aplicação permite cadastrar, consultar, atualizar e remover informações sobre empresas e seus responsáveis.

O sistema foi desenvolvido como parte de um desafio técnico, com foco em boas práticas de arquitetura, organização de código e cobertura de testes.

---
# Descrição da solução

A solução consiste em uma **API RESTful** responsável pelo gerenciamento de empreendimentos.

Cada empreendimento possui informações como:

- Nome do empreendimento
- Nome do empreendedor responsável
- Município de Santa Catarina
- Segmento de atuação
- E-mail ou meio de contato
- Status (ativo ou inativo)

A API fornece endpoints para:

- Criar empreendimentos
- Listar empreendimentos
- Consultar um empreendimento específico
- Atualizar empreendimentos
- Remover empreendimentos
- Filtrar registros por diversos critérios

Também foram implementados:

- Filtros avançados
- Paginação
- Serialização customizada de enums
- Testes automatizados
- Estrutura modular de projeto

---
# Tecnologias utilizadas

Principais tecnologias utilizadas no desenvolvimento:

- **Python 3**
- **Django**
- **Django Rest Framework**
- **SQLite**
- **Pytest**
- **Factory Boy**
- **Django Filter**

Ferramentas auxiliares:

- Postman (testes de API)
- Git / GitHub
- Virtualenv

---
# Estrutura do projeto

A estrutura foi organizada visando separação de responsabilidades e reutilização de código.

```
sctec-challenge
│
├── core/ # Componentes reutilizáveis da aplicação
│ ├── models.py # BaseModel com UUID e timestamps
│ ├── pagination.py # Paginação padrão da API
│ ├── permissions.py # Permissões reutilizáveis
│ ├── exceptions.py # Exceções customizadas
│
├── enterprises/ # Módulo responsável pelos empreendimentos
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── filters.py
│ ├── tests/
│ │ ├── factories.py
│ │ ├── test_enterprise_views.py
│ │ └── test_enterprise_filters.py
│
├── config/ # Configurações do projeto Django
│ ├── settings.py
│ ├── urls.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---
# Funcionalidades da API

### Criar empreendimento

POST /api/v1/enterprises/

### Listar empreendimentos

GET /api/v1/enterprises/

### Buscar empreendimento por ID

GET /api/v1/enterprises/{id}/

### Atualizar empreendimento

PUT /api/v1/enterprises/{id}/

### Remover empreendimento

DELETE /api/v1/enterprises/{id}/

---
# Filtros disponíveis

A API permite filtragem por:

- Nome (name)
- Empreendedor (entrepreneur_name)
- Município (municipality)
- Segmento (segment)
  - Tecnologia = 0
  - Comércio = 1
  - Indústria = 2
  - Serviços = 3
  - Agronegócio = 4
- Status (status)
  - Inativo = 0
  - Ativo = 1
- Email (email)
- Intervalo de criação (created_after, created_before)
- Intervalo de atualização (updated_after, updated_before)

Exemplo:

GET /api/v1/enterprises/?segment=2

GET /api/v1/enterprises/?status=1

---

# Como executar o projeto

```
## 1 - Clonar o repositório

git clone https://github.com/j-rdel/sctec-challenge.git

cd sctec-challenge

---

## 2 - Criar ambiente virtual

python -m venv .venv

---

## 3 - Ativar ambiente virtual

Linux / Mac:

source .venv/bin/activate


Windows:

.venv\Scripts\activate

---

## 4 - Instalar dependências

pip install -r requirements.txt

---

## 5 - Executar migrations

python manage.py migrate

Esse comando criará automaticamente o banco de dados **SQLite**.

---

## 6 - Executar o servidor

python manage.py runserver

A API estará disponível em:

http://127.0.0.1:8000/api/v1/enterprises/
```
---

# Executando os testes

Os testes automatizados utilizam **pytest** e **factory_boy**.

Para executá-los:

```
pytest
```

Os testes cobrem:

- filtros da API
- endpoints
- criação de registros
- comportamento esperado da listagem

---

# Vídeo Pitch

O vídeo de apresentação da solução pode ser acessado no link abaixo:

➡️ **[Link do vídeo pitch](COLE_AQUI_O_LINK_DO_VIDEO)**

---

# Autor

Desenvolvido por **Jardel Urban**.