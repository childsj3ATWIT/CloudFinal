FROM alpine:latest

RUN apk add --no-cache postfix busybox

COPY main.cf /etc/postfix/main.cf

# Add virtual alias mapping so all @guitarshop.local emails go to test@guitarshop.local
COPY virtual /etc/postfix/virtual

# Create empty mail log file with correct permissions
RUN touch /var/log/maillog && chmod 644 /var/log/maillog

CMD sh -c "syslogd -O /var/log/maillog && postfix start-fg"

EXPOSE 25