# quorum_consensus.py

import random


nodes = {
    "Node1": True,
    "Node2": True,
    "Node3": True,
    "Node4": True,
    "Node5": True
}


def request_vote(node):
    # Simulate random agreement/disagreement
    vote = random.choice([True, True, False])

    print(f"{node} voted:", "YES" if vote else "NO")

    return vote


def achieve_quorum():
    total_nodes = len(nodes)
    required = (total_nodes // 2) + 1

    votes = 0

    print(f"\nQuorum required: {required} votes\n")

    for node in nodes:
        if request_vote(node):
            votes += 1

    print(f"\nTotal YES votes: {votes}")

    if votes >= required:
        print("Consensus achieved")
    else:
        print("Consensus failed")


def main():
    achieve_quorum()


main()
