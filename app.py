```python
import urllib.request
import itertools
from queue import Queue
import threading

class ExampleClass:
    def __init__(self, data):
        self.data = data

    def print_data(self):
        print("Data:", self.data)

def fetch_url(url):
    try:
        response = urllib.request.urlopen(url)
        content = response.read()
        if not content:
            return None
        return content
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} {url}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason} {url}")

def process_data():
    data_points = range(100) 
    for data in data_points:
        print("Processing data:", data)

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b  

def use_lambda():
    pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
    # Sorting with a lambda function
    pairs.sort(key=lambda x: x[0])
    print("Sorted pairs:", pairs)

def thread_function(name, queue):
    try:
        while not queue.empty():
            item = queue.get()
            print(f"Thread {name} got {item}")
    except Exception as e:
        print(f"Error in thread {name}: {e}")

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
    except ZeroDivisionError as e:
        print(e)
    use_lambda()

if __name__ == "__main__":
    main()
```