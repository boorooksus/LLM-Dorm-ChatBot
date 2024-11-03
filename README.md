# LLM-ChatBot

## Overview

<br>

>

## Developing

```bash
# Windows
my_env\Scripts\activate

# Linux/macOS
source llm_env/bin/activate

pip install fastapi uvicorn

uvicorn app.main:app --reload
```

## Database

```bash
brew services start postgresql

psql postgres

psql postgres -U council

```

## Docker

```bash
pip freeze > requirements.txt

docker build -t llm-dorm-chatbot .
docker run -p 8000:8000 llm-dorm-chatbot

```

## Docker Compose

```bash
docker-compose -f docker-compose.yml -f docker-compose.override.yml up -d
```
