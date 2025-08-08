FROM alpine:latest

RUN apk add --no-cache postfix

COPY main.cf /etc/postfix/main.cf

CMD ["sh", "-c", "postfix start-fg"]

EXPOSE 25
