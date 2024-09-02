```python
import urllib.request
from queue import Queue
import threading
import itertools

class ExampleClass:
    def __init__(self, value):
        self.value = value

    def print_data(self):
        print(f"Value: {self.value}")

def process_data(data):
    return [x**2 for x in data]

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def use_lambda():
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))
    return squared_numbers

def thread_function(q):
    q.put('item from thread')

def sort_list(lst):
    lst.sort()

def main():
    try:
        url = 'http://example.com'
        response = urllib.request.urlopen(url)
        print(response.read())
    except Exception as e:
        print(f"Error: {e}")

    q = Queue()
    t = threading.Thread(target=thread_function, args=(q,))
    t.start()
    print(q.get())
    t.join()

    numbers = [1, 2, 3, 4, 5]
    sort_list(numbers)
    print(numbers)

    example_instance = ExampleClass(10)
    print(example_instance.value)
    example_instance.print_data()

    data = [1, 2, 3, 4, 5]
    processed_data = process_data(data)
    print(processed_data)

    result = divide(10, 2)
    print(result)

    squared_numbers = use_lambda()
    print(squared_numbers)

    # Example usage of itertools
    numbers = [1, 2, 3, 4, 5]
    for num in itertools.cycle(numbers):
        print(num)
        if num == 5:
            break

if __name__ == "__main__":
    main()
```