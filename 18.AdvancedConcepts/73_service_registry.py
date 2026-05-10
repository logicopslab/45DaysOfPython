# service_registry.py

services = {}


def register_service(name, address):
    services[name] = address
    print(f"Registered {name} at {address}")


def unregister_service(name):
    if name in services:
        del services[name]
        print(f"Unregistered {name}")


def discover_service(name):
    return services.get(name, "Service not found")


def show_services():
    print("\nActive Services:")
    for name, address in services.items():
        print(f"{name} -> {address}")


def main():
    register_service("AuthService", "10.0.0.1")
    register_service("PaymentService", "10.0.0.2")
    register_service("CacheService", "10.0.0.3")

    show_services()

    print("\nDiscovering AuthService:")
    print(discover_service("AuthService"))

    unregister_service("CacheService")

    show_services()


main()