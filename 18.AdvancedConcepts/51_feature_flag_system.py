# feature_flag_system.py

# Simulated feature configuration
feature_flags = {
    "new_dashboard": True,
    "beta_feature": False,
    "logging_enabled": True
}


def is_feature_enabled(feature_name):
    return feature_flags.get(feature_name, False)


def dashboard():
    if is_feature_enabled("new_dashboard"):
        print("Showing NEW dashboard")
    else:
        print("Showing OLD dashboard")


def beta_feature():
    if is_feature_enabled("beta_feature"):
        print("Accessing beta feature")
    else:
        print("Beta feature is disabled")


def logging(message):
    if is_feature_enabled("logging_enabled"):
        print(f"[LOG]: {message}")


def main():
    print("---- Application Start ----\n")

    dashboard()
    beta_feature()
    logging("User accessed dashboard")

    print("\n---- Toggling Features ----\n")

    # Dynamically change feature flags
    feature_flags["beta_feature"] = True
    feature_flags["new_dashboard"] = False

    dashboard()
    beta_feature()
    logging("Features updated at runtime")


main()
