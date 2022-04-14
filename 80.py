import requests
response = requests.get("https://api.github.com/users/avielb/repos")
for repo in response.json():
    print(repo["full_name"])
