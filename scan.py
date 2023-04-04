import requests

url = input("Enter URL to scan: ")

response = requests.get(url)

if response.status_code == 200:
    print("URL is valid and active")
else:
    print("URL is not valid or inactive")
