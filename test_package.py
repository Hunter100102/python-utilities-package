from utilities.api_utils import fetch_data

url = "https://api.github.com/repos/Hunter100102/python-utilities-package"
data = fetch_data(url)

print("Repository Name:", data.get("name"))
print("Stars:", data.get("stargazers_count"))
print("Forks:", data.get("forks_count"))
