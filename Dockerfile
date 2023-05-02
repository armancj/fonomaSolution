FROM python:latest
LABEL authors="mandi"

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt clean && \
    rm -rf /var/cache/apt/*

RUN pip install -U pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

COPY . .

RUN useradd -m -d /src -s /bin/bash app \
    && chown -R app:app /* && chmod +x /*

WORKDIR .
USER app

CMD ["./scripts/start-dev.sh"]
ENTRYPOINT ["top", "-b"]