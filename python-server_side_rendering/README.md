# Python - Server-Side Rendering

## Description
This project is an implementation of Server-Side Rendering (SSR) techniques using Python and Flask. Server-side rendering is a technique where web pages are generated on the server and sent to the client as fully formed HTML, as opposed to client-side rendering, where the browser builds the page using JavaScript and dynamic data.

In this project, we focus on:
- Implementing a simple templating program to generate personalized text files
- Building basic and dynamic HTML templates using Flask and Jinja2
- Reading and displaying data from multiple sources, including JSON, CSV, and SQLite
- Handling dynamic content, query parameters, and user input in a web application

The main goal of this project is to understand how server-side rendering works and how templating engines like Jinja2 can be used to build dynamic, efficient, and SEO-friendly web applications.

## Installation
Clone the repository:
```
git clone https://github.com/RahafN1/holbertonschool-higher_level_programming.git
```

Move into the project directory:
```
cd holbertonschool-higher_level_programming/python-server_side_rendering
```

Install the required dependencies:
```
pip install Flask
```

Run the Flask application:
```
python3 task_01_index.py
```

## Requirements
- Ubuntu 20.04 LTS
- Python 3.8.5 or higher
- Flask
- pycodestyle (version 2.8.*)
- All files must be executable
- All modules, classes, and functions must have documentation

## Examples
```python
from task_00_intro import generate_invitations

with open('template.txt', 'r') as file:
    template_content = file.read()

attendees = [
    {"name": "Alice", "event_title": "Python Conference",
     "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop",
     "event_date": "2023-08-20", "event_location": "San Francisco"},
]

generate_invitations(template_content, attendees)
```

## Testing
You can test the Flask application by running the corresponding task file and accessing the routes through your browser or a tool like `curl`:
```
curl "http://localhost:5000/products?source=json"
curl "http://localhost:5000/products?source=csv&id=1"
```

## Files
| File | Description |
| --- | --- |
| `task_00_intro.py` | Generates personalized invitation files from a template |
| `task_01_index.py` | Basic Flask application serving a static HTML template |
| `task_02_dynamic.py` | Dynamic Flask template using loops and conditions |
| `task_03_files.py` | Displays product data from JSON or CSV files |
| `task_04_database.py` | Extends dynamic data display to include SQLite |
| `templates/` | Folder containing all HTML/Jinja templates |
| `products.json` | Sample product data in JSON format |
| `products.csv` | Sample product data in CSV format |

## Authors
Rahaf Alabdalh
