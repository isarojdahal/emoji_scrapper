"""
	AUTHOR : Saroj Dahal / @originalsaroj
	VERSION: 1.0.0.0
"""

import requests
from bs4 import BeautifulSoup
import json

response = requests.get("https://www.gstatic.com/youtube/img/emojis/emojis-svg-1.json").json()

for index in range(0, 1476):
    url = response[index]['image']['thumbnails'][0]['url']
    another_response = requests.get(url)
    file_name_index = str(url).index("emoji_")
    url = str(url)
    file_name = url[file_name_index:]
    with open(file_name, "wb") as f:
        f.write(another_response.content)
