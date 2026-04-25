# audit_log_system.py

from datetime import datetime


# Main data store
data_store = {}

# Audit log list
audit_log = []


def log_action(user, action, key, old_value, new_value):
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user": user,
        "action": action,
        "key": key,
        "old_value": old_value,
        "new_value": new_value
    }
    audit_log.append(entry)


def add_or_update(user, key, value):
    old_value = data_store.get(key)

    data_store[key] = value

    if old_value is None:
        log_action(user, "CREATE", key, None, value)
    else:
        log_action(user, "UPDATE", key, old_value, value)

    print(f"{key} set to {value}")


def delete_key(user, key):
    if key in data_store:
        old_value = data_store[key]
        del data_store[key]

        log_action(user, "DELETE", key, old_value, None)
        print(f"{key} deleted")
    else:
        print("Key not found")


def view_data():
    print("\nCurrent Data Store:")
    for k, v in data_store.items():
        print(f"{k}: {v}")


def view_audit_log():
    print("\nAudit Log:")
    for entry in audit_log:
        print(entry)


def main():
    user = "admin"

    add_or_update(user, "feature_flag", True)
    add_or_update(user, "timeout", 30)
    add_or_update(user, "timeout", 60)

    delete_key(user, "feature_flag")

    view_data()
    view_audit_log()


main()
