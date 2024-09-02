```python
import requests
from queue import Queue
import threading
import itertools

class ExampleClass(object):
    def __init__(self, data):
        self.data = data

    def print_data(self):
        print("Data:", self.data)

def fetch_url(url):
    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        print("Request Error:", e, url)

def process_data():
    data_points = range(100) 
    for data in data_points:
        print("Processing data:", data)

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b  

def use_lambda():
    pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
    # Sorting with a lambda function
    pairs.sort(key=lambda x: x[0])
    print("Sorted pairs:", pairs)

def thread_function(name, queue):
    while not queue.empty():
        item = queue.get()
        print("Thread", name, "got", item)
        queue.task_done()

def main():
    urls = ["http://example.com", "http://example.net", "http://example.org"]
    results = list(map(fetch_url, urls))

    queue = Queue()
    for i in range(5):
        queue.put(i)

    thread_a = threading.Thread(target=thread_function, args=("A", queue))
    thread_b = threading.Thread(target=thread_function, args=("B", queue))

    thread_a.start()
    thread_b.start()

    print("Threads started")

    example = ExampleClass("example data")
    example.print_data()
    process_data()
    try:
        print("10 / 3 equals", divide(10, 3))
    except ValueError as e:
        print(e)
    use_lambda()

    queue.join()

if __name__ == "__main__":
    main()
```