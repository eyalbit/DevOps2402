import requests
#response = requests.get("https://api.github.com/users/avielb")
response = requests.get("https://api.github.com/users/avielb/repos")
#print( response.json())
#if response.status_code == 200:
 #   print("github is up and running")

for r in response.json():
    print(r["full_name"])
