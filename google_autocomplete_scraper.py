import requests
import json 

searchword = ""

URL="http://suggestqueries.google.com/complete/search?client=firefox&q=" + searchword
#URL="http://suggestqueries.google.com/complete/search?client=chrome&q=" + searchword

response = requests.get(URL)

result = json.loads(response.content.decode('utf-8')) 

for completion in result[1]:
    print(completion)
