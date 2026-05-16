# replication_simulator.py

leader = {}
followers = [
    {},
    {}
]


def write_data(key, value):
    leader[key] = value

    print(f"Leader updated: {key} = {value}")

    replicate_data(key, value)


def replicate_data(key, value):
    for i, follower in enumerate(followers):
        follower[key] = value
        print(f"Replicated to Follower-{i+1}")


def show_cluster_state():
    print("\nLeader State:")
    print(leader)

    for i, follower in enumerate(followers):
        print(f"Follower-{i+1} State:")
        print(follower)


def main():
    write_data("user1", "Ravi")
    write_data("status", "active")

    show_cluster_state()


main()
