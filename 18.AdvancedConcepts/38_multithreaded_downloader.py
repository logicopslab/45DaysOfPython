# multithreaded_downloader.py

import threading
import time


def download_file(file_name):
    print(f"Starting download: {file_name}")
    time.sleep(2)  # Simulate download time
    print(f"Completed download: {file_name}")


def main():
    files = ["file1.txt", "file2.txt", "file3.txt"]

    threads = []

    for file in files:
        t = threading.Thread(target=download_file, args=(file,))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("\nAll downloads completed")


main()
