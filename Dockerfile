FROM python:3.14.3-alpine3.23
WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache --virtual .build-dependencies gcc musl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-dependencies

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
