import urllib2
import itertools
from Queue import Queue
import thread

class ExampleClass(object):
    def __init__(self, data):
        self.data = data

    def print_data(self):
        print "Data:", self.data

def fetch_url(url):
    try:
        response = urllib2.urlopen(url)
        return response.read()
    except urllib2.HTTPError as e:
        print "HTTP Error:", e.code, url
    except urllib2.URLError as e:
        print "URL Error:", e.reason, url

def process_data():
    data_points = xrange(100) 
    for data in data_points:
        print "Processing data:", data

def divide(a, b):
    return a / b  

def use_lambda():
    pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
    # Sorting with a lambda function
    pairs.sort(cmp=lambda x, y: cmp(x[0], y[0]))
    print "Sorted pairs:", pairs

def thread_function(name, queue):
    while not queue.empty():
        item = queue.get()
        print "Thread", name, "got", item

def main():
    urls = ["http://example.com", "http://example.net", "http://example.org"]
    results = map(fetch_url, urls)

    queue = Queue()
    for i in range(5):
        queue.put(i)

    thread.start_new_thread(thread_function, ("A", queue))
    thread.start_new_thread(thread_function, ("B", queue))

    print "Threads started"

    example = ExampleClass("example data")
    example.print_data()
    process_data()
    print "10 / 3 equals", divide(10, 3)
    use_lambda()

if __name__ == "__main__":
    main()