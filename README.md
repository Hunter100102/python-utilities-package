# 🧰 Advanced Python Utilities Package

[![Python Tests](https://github.com/yourusername/advanced-python-utilities/actions/workflows/python-tests.yml/badge.svg)](https://github.com/yourusername/advanced-python-utilities/actions)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A modular, testable, and CLI-enabled Python package designed to streamline **file handling**, **API data fetching**, and **function logging**. Built using Python best practices — perfect for automation, data engineering, and backend tasks.

---

## 🚀 Features

✅ Read & write JSON, CSV, and XML files  
✅ Fetch data from any public API with retry support  
✅ Log every function call with timestamps  
✅ Command-line interface (CLI) with `click`  
✅ Unit tested with `pytest`  
✅ CI/CD with GitHub Actions  

---

## 📦 Installation

### 1. Clone the repository
git clone https://github.com/yourusername/advanced-python-utilities.git
cd advanced-python-utilities

### 2. Create a virtual enviroment
Depending on if you are utilizing py or python for your python commands will dictate the nomeclature of the next command. It will either be py -m venv venv or python -m venv venv
Then actiavet the enviroment with either .\venv\Scripts\Activate.ps1 or source venv/bin/activate either should work on windows.

### 3. Install dependencies
pip install -e
Now the CLI should be able to be globally utllized: pyutils --help

🔧 Usage Examples
📁 File Handling
python
Copy
Edit
from utilities.file_utils import read_json, write_csv

data = read_json("sample.json")
write_csv("output.csv", [{"name": "Alice"}, {"name": "Bob"}])
🌐 API Data Fetching
python
Copy
Edit
from utilities.api_utils import fetch_data

result = fetch_data("https://jsonplaceholder.typicode.com/posts")
print(result[0])
📝 Logging Decorator
python
Copy
Edit
from utilities.logger import log_function_call

@log_function_call
def greet(name):
    return f"Hello, {name}!"

greet("Cody")
🖥️ CLI Commands
bash
Copy
Edit
# Fetch API data
pyutils get-api-data https://jsonplaceholder.typicode.com/posts

# Read a JSON file
pyutils read-json-file sample.json

# Read a CSV file
pyutils read-csv-file sample.csv
✅ Run Tests
This project uses pytest for unit testing.

bash
Copy
Edit
pytest
Tested features include:

JSON read/write

API data fetching

### CI/CD Features
This repo also includes GitHub actions that will install dependencies and run pytest automatically each time the repo is pushed to GitHub. The status of these tests can be found under the Actions tab in Github. 

🙋‍♂️ Author
William Cody Hunter
📧 spc.cody.hunter@gmail.com
💼 LinkedIn
