from reed import ReedClient
from urllib.parse import urlencode

reed = ReedClient(api_key=r"0da53af5-3512-4e3d-939f-5c773ffb495d")
params = {
    "keywords": "python",
    'minimumSalary': 55000,
}
filename = urlencode(params).replace('&', '_')
results = reed.search(**params)
reed.excel(results, filename)
# reed.json(results, filename)