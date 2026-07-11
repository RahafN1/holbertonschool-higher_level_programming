# C - RESTful API

## Description
This project is an introduction to working with APIs, from the command line up to building and securing a full API of your own. It covers the fundamentals of the HTTP/HTTPS protocol, consuming data from a public API using both `curl` and Python, building a simple API from scratch with Python's built-in `http.server` module, building a more complete API using the Flask framework, and finally exploring common API security and authentication techniques.

In this project, we focus on:
- Understanding the basics of HTTP and HTTPS
- Consuming data from a REST API using command-line tools (`curl`)
- Consuming and processing API data using Python (`requests`, `json`, `csv`)
- Building a simple API server using Python's `http.server` module
- Building a RESTful API using the Flask framework
- Implementing basic API security and authentication techniques

The main goal of this project is to understand how APIs work on both the client side (consuming data) and the server side (building and securing endpoints).

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/RahafN1/holbertonschool-higher_level_programming.git
   ```
2. Move into the project directory:
   ```
   cd holbertonschool-higher_level_programming/restful-api
   ```
3. Install the required Python packages:
   ```
   pip install requests flask
   ```
4. Run any script using:
   ```
   python3 <filename>.py
   ```

## Requirements
- Ubuntu 20.04 LTS
- Python 3.8+
- `curl` command-line tool
- `requests` library
- `Flask` framework
- pycodestyle (PEP 8) coding style

## Examples

**Fetching data with curl:**
```
curl https://jsonplaceholder.typicode.com/posts
```

**Fetching and printing posts with Python:**
```python
from task_02_requests import fetch_and_print_posts

fetch_and_print_posts()
```

**Running a simple API server:**
```
python3 task_03_http_server.py
```

## Testing
You can test each script individually by creating a `main_XX.py` file that imports the relevant functions and runs them, then executing it with `python3 main_XX.py`. For the server-based tasks, run the server file directly and send requests to it using `curl` or a browser. Do not include `main_XX.py` files in the repository.

## Files

| File | Description |
|---|---|
| `0-basics_of_http.md` | Notes on the basics of HTTP/HTTPS |
| `1-curl_requests.md` | Notes and commands for consuming data from an API using `curl` |
| `task_02_requests.py` | Fetches and processes posts from an API using Python's `requests` library |
| `task_03_http_server.py` | A simple API built using Python's `http.server` module |
| `task_04_flask.py` | A RESTful API built using the Flask framework |
| `task_05_security.py` | Implementation of basic API security and authentication techniques |

## Authors
Rahaf Alabdalh
