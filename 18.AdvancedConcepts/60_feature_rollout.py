# feature_rollout.py

import hashlib


def get_user_bucket(user_id):
    # Create a deterministic hash value (0–99)
    hash_value = hashlib.md5(user_id.encode()).hexdigest()
    bucket = int(hash_value, 16) % 100
    return bucket


def is_feature_enabled(user_id, rollout_percentage):
    bucket = get_user_bucket(user_id)

    if bucket < rollout_percentage:
        return True
    return False


def simulate():
    users = ["user1", "user2", "user3", "user4", "user5"]

    rollout_percentage = int(input("Enter rollout percentage (0-100): "))

    for user in users:
        enabled = is_feature_enabled(user, rollout_percentage)

        status = "ENABLED" if enabled else "DISABLED"
        print(f"{user}: {status}")


def main():
    simulate()


main()
