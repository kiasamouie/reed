from reed import ReedClient
from urllib.parse import urlencode

reed = ReedClient(api_key=r"46af4632-d4f3-46ed-86f2-7ac016565ea7")
params = {
    "keywords": "aws",
    'minimumSalary': 55000,
}
filename = urlencode(params).replace('&', '_')
results = reed.search(**params)
reed.excel(results, filename)
# reed.json(results, filename)