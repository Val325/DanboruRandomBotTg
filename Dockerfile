FROM alpine:latest
LABEL maintainer="telegramg:@garriMal"

WORKDIR /pythonbot
COPY . .
COPY requirements.txt .
RUN apk add --no-cache python3 py3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/pythonbot/app.py"]
