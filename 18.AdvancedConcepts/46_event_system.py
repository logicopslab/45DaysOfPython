# event_system.py

class EventManager:
    def __init__(self):
        self.listeners = []

    def subscribe(self, func):
        self.listeners.append(func)

    def unsubscribe(self, func):
        if func in self.listeners:
            self.listeners.remove(func)

    def notify(self, data):
        for listener in self.listeners:
            listener(data)


# Example listeners
def email_service(data):
    print(f"[Email Service] Sending email for event: {data}")


def log_service(data):
    print(f"[Logger] Event logged: {data}")


def analytics_service(data):
    print(f"[Analytics] Tracking event: {data}")


def main():
    event_manager = EventManager()

    # Subscribe services
    event_manager.subscribe(email_service)
    event_manager.subscribe(log_service)
    event_manager.subscribe(analytics_service)

    # Trigger event
    print("\nTriggering USER_REGISTERED event...\n")
    event_manager.notify("USER_REGISTERED")

    # Unsubscribe one service
    event_manager.unsubscribe(log_service)

    print("\nTriggering ORDER_PLACED event...\n")
    event_manager.notify("ORDER_PLACED")


main()
