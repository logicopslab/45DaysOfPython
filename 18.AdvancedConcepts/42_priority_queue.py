# priority_queue.py

import heapq


task_queue = []


def add_task(priority, task):
    heapq.heappush(task_queue, (priority, task))
    print(f"Task '{task}' added with priority {priority}")


def process_task():
    if task_queue:
        priority, task = heapq.heappop(task_queue)
        print(f"Processing task: {task} (priority {priority})")
    else:
        print("No tasks to process")


def view_tasks():
    print("\nCurrent Queue:")
    for item in task_queue:
        print(item)


def main():
    add_task(2, "Write report")
    add_task(1, "Fix bug")
    add_task(3, "Email client")

    view_tasks()

    process_task()
    process_task()
    process_task()


main()
