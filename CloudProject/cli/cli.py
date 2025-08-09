import requests

services = [
    'main_app_server',
    'frontend_app_server',
    'database',
    'load_balancer',
    'redis',
    'email',
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
        choice = input("Select a service:")
        if choice.isdigit():
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(services):
                service = services[choice_index]
                print("Starting:", service)
                continue
        elif choice in services:
            print("Starting:", choice)

        elif choice == 'exit':
            print("Exiting...")
            loop = False
        else:
            print("Please select one of the following services:")
            for i, service in enumerate(services, start=1):
                print(f"{i}. {service}")


if __name__ == '__main__':
    maindriver()
