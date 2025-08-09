import smtplib

FROM = "test@guitarshop.local"
TO = "root@guitarshop.local"
msg = """Subject: Test Email

Hello, this is a test message.
"""

with smtplib.SMTP("localhost", 25) as server:
    server.sendmail(FROM, [TO], msg)

print("Email sent!")