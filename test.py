import requests

# URL to fetch data from
url = "https://uk.indeed.com/jobs?q=python&l=&from=searchOnHP"

# Headers as specified in your fetch request
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,und;q=0.7,hu;q=0.6",
    "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "upgrade-insecure-requests": "1"
}

# Making the GET request
response = requests.get(url, headers=headers)

# Check if the response was successful
if response.status_code == 200:
    # Processing the response here if the status code is OK
    print(response.text)  # or response.json() if JSON is expected
else:
    print(f"Failed to fetch data: HTTP status code {response.status_code}")
