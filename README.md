# 📂 CN Images – Upload de Arquivos com React, Django e Nginx

Projeto full-stack com upload de arquivos, frontend em React, backend em Django e infraestrutura com Docker + Nginx.

---

## 🚀 Funcionalidades

- Upload de arquivos via interface web (React + Bootstrap)
- Backend com Django + Django REST
- Armazenamento dos uploads em volume Docker (e também visível localmente)
- Servido por Nginx com proxy reverso
- Containers orquestrados com Docker Compose
- Build de produção do React incluso

---

## 📦 Estrutura do Projeto

meu_projeto/
├── backend/                  # Projeto Django + app uploads
│   ├── meu_projeto/         # Configurações do Django (settings, urls, wsgi, etc.)
│   ├── uploads/             # App responsável pelo upload de arquivos
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/                # Aplicação React (Create React App)
│   ├── src/                 # Código-fonte do React (App.js, etc.)
│   ├── public/              # Arquivos públicos (index.html, favicon, etc.)
│   └── Dockerfile           # Dockerfile para build da aplicação React
│
├── nginx/                   # Configuração do Nginx
│   └── nginx.conf
│
├── media/                   # Pasta de arquivos enviados (mapeada localmente)
├── docker-compose.yml       # Orquestração dos serviços com Docker
└── README.md                # Documentação do projeto


---

## 🛠️ Como rodar o projeto

1. **Clone o repositório**

```bash
git clone https://github.com/Fransueudes/cn-images.git
cd cn-images
```
Build dos containers e execução

```bash
docker-compose up --build
```

Acesse:
Frontend: http://localhost
Uploads: /api/upload/
Arquivos enviados: /media/

## 📤 Upload de Arquivo
Acesse http://localhost, selecione um arquivo e envie.
O backend salva no volume /app/media/, que também está espelhado na pasta ./media local.

## 🧰 Tecnologias
React + Bootstrap
Django + Django REST Framework
PostgreSQL
Redis
Gunicorn
Nginx
Docker & Docker Compose

## 👤 Autores
Fransueudes Alexandre Freitas
Joao Antonio dos Santos Ilario
📍 Palmas - TO
