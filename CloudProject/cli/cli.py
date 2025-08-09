import requests
import smtplib

def send_test_email():
    FROM = "test@guitarshop.local"
    TO = "root@guitarshop.local"
    msg = """Subject: Test Email from CLI

    Hello, this is a test email sent from the CLI.
    """
    try:
        with smtplib.SMTP("localhost", 25) as server:
            server.sendmail(FROM, [TO], msg)
        print("Test email sent successfully!")
    except Exception as e:
        print(f"Failed to send test email: {e}")

services = [
    'main_app_server',
    'frontend_app_server',
    'database',
    'load_balancer',
    'redis',
    'email',
    'send_test_email',
    'minIO',
    'admin',
    'identity_service'
]


#all containers are already running, just calling
def maindriver():
    print("Welcome to Our Local Cloud Environment")
    print("Please select one of the following services:")
    for i, service in enumerate(services, start=1):
        print(f"{i}. {service}")
    print("exit")

    loop = True
    while loop:
        choice = input("Select a service: ").strip()
        if choice.isdigit():
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(services):
                service = services[choice_index]
            else:
                print("Invalid selection.")
                continue
        elif choice in services:
            service = choice
        elif choice.lower() == 'exit':
            print("Exiting...")
            break
        else:
            print("Invalid input. Try again.")
            continue

        print("Routing to:", service)

        try:
            if service == 'main_app_server':

                print("http://localhost")
            elif service == 'frontend_app_server':
                print("Open http://localhost:8080 in your browser.")
            elif service == 'database':
                print("Database running on localhost:3306.")
            elif service == 'load_balancer':
                print("Access via http://localhost")
            elif service == 'redis':
                print("Redis available on port 6379.")
            elif service == 'email':
                print("Email server ready.")
            elif service == 'send_test_email':
                send_test_email()
                print("http://localhost:8025/")
            elif service == 'minIO':
                print("MinIO Web UI: http://localhost:9001")
                print("MinIO User: minioadmin")
                print("MinIO password: minioadmin123")
            elif service == 'admin':
                r = requests.get("http://localhost:8001/admin/products")
                print(r.json())
            elif service == 'identity_service':
                r = requests.get("http://localhost/login", cookies={"session": "dummy"})
                print(r.json())
        except Exception as e:
            print("Error connecting to service:", e)


if __name__ == '__main__':
    maindriver()
