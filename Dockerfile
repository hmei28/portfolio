FROM python:3.10.9-slim

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
ADD requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt
    
COPY src /app
WORKDIR /app/

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio.wsgi"]
