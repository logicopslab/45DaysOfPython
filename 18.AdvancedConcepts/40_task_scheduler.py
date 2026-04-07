# task_scheduler.py

import time


tasks = []


def add_task(name, delay):
    run_time = time.time() + delay
    tasks.append((name, run_time))
    print(f"Task '{name}' scheduled in {delay} seconds")


def run_scheduler():
    print("\nScheduler started...\n")

    while tasks:
        current_time = time.time()

        for task in tasks[:]:
            name, run_time = task

            if current_time >= run_time:
                print(f"Executing task: {name}")
                tasks.remove(task)

        time.sleep(1)


def main():
    add_task("Task1", 3)
    add_task("Task2", 5)
    add_task("Task3", 7)

    run_scheduler()


main()
