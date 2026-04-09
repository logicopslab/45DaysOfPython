# load_balancer.py

servers = ["Server1", "Server2", "Server3"]
current_index = 0


def get_next_server():
    global current_index

    server = servers[current_index]
    current_index = (current_index + 1) % len(servers)

    return server


def simulate_requests(num_requests):
    for i in range(1, num_requests + 1):
        server = get_next_server()
        print(f"Request {i} handled by {server}")


def main():
    num_requests = int(input("Enter number of requests: "))
    simulate_requests(num_requests)


main()
