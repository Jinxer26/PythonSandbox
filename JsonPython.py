import json
import requests

a = requests.get("https://api.npoint.io/3b4e5f228fd809e2c654")

print(type(a.json()))