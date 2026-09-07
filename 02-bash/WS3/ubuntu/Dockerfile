FROM ubuntu:latest

RUN apt-get update && apt-get install -y bash

WORKDIR /app

COPY monitor.sh .
COPY analiza.sh .

RUN chmod +x monitor.sh analiza.sh

CMD ["tail", "-f", "/dev/null"]
