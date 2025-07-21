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
    for service in services:
        print(service)
    print("exit")

    loop = True
    while loop:
        choice = input("Select a service:")
        if choice in services:
            service = services[services.index(choice)]
            print("Starting:", service)
            #call specified container
            #will add later

        elif choice == 'exit':
            print("Exiting...")
            loop = False
        else:
            print("Please select one of the following services:")
            for service in services:
                print(service)


if __name__ == '__main__':
    maindriver()
