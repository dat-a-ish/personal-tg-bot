FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY base/requirments.txt ./base/requirments.txt

RUN pip install -r base/requirments.txt

COPY . .

CMD ["python", "-m", "base.bot_logic.bot_handler"]