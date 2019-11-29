"""
reference: https://site.nicovideo.jp/search-api-docs/search.html
"""

import requests
import json

url = "https://api.search.nicovideo.jp/api/v2/video/contents/search"
params = {'q': 'BB素材',
          'targets': 'tagsExact',
          'fields': 'contentId,title,viewCounter,mylistCounter,lengthSeconds,thumbnailUrl,categoryTags',
          '_sort': '-viewCounter'}

response = requests.get(url=url, params=params)

data = response.json()
print(json.dumps(data, indent=4))
