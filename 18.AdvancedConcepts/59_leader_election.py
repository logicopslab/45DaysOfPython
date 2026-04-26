# leader_election.py

import random


class Node:
    def __init__(self, node_id, priority):
        self.node_id = node_id
        self.priority = priority
        self.is_leader = False

    def __repr__(self):
        return f"Node({self.node_id}, priority={self.priority})"


def elect_leader(nodes):
    # Select node with highest priority
    leader = max(nodes, key=lambda node: node.priority)

    for node in nodes:
        node.is_leader = False

    leader.is_leader = True
    return leader


def simulate():
    # Create nodes with random priority
    nodes = [Node(i, random.randint(1, 100)) for i in range(1, 6)]

    print("Nodes:")
    for node in nodes:
        print(node)

    leader = elect_leader(nodes)

    print("\nLeader elected:")
    print(f"{leader} is the leader")

    # Simulate leader failure
    print("\nSimulating leader failure...")
    nodes.remove(leader)

    new_leader = elect_leader(nodes)

    print("New Leader:")
    print(f"{new_leader} is the leader")


def main():
    simulate()


main()
