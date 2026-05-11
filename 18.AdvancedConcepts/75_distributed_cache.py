# distributed_cache.py

cache_nodes = {
    "Node1": {},
    "Node2": {},
    "Node3": {}
}


def get_node(key):
    nodes = list(cache_nodes.keys())

    # Simple hash-based distribution
    index = hash(key) % len(nodes)

    return nodes[index]


def set_cache(key, value):
    node = get_node(key)

    cache_nodes[node][key] = value

    print(f"Stored '{key}' in {node}")


def get_cache(key):
    node = get_node(key)

    value = cache_nodes[node].get(key)

    return value if value else "Key not found"


def show_cache():
    print("\nDistributed Cache State:")
    for node, data in cache_nodes.items():
        print(node, "->", data)


def main():
    set_cache("user1", "Ravi")
    set_cache("user2", "John")
    set_cache("session1", "abc123")

    show_cache()

    print("\nRetrieve user1:")
    print(get_cache("user1"))


main()