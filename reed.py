import datetime
import requests
from requests.auth import HTTPBasicAuth

ROOT_URL = 'https://www.reed.co.uk/api/1.0/search?'
JOB_DETAILS_ROOT = 'https://www.reed.co.uk/api/1.0/jobs/'

class ReedClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def search(self, **args) -> list:
        '''
        Perform a job search with given arguments.
        '''
        return self.process_search_request(ROOT_URL, args)

    def process_search_request(self, url: str, args) -> list:
        '''
        Process job search request using requests library and retrieve all results.
        '''
        auth = HTTPBasicAuth(username=self.api_key, password='')
        args.setdefault('resultsToTake', 100)  # Set default batch size
        total_jobs = []
        results_fetched = 0

        while True:
            response = requests.get(url, auth=auth, params=args)
            if response.status_code != 200:
                response.raise_for_status()
            
            data = response.json()
            total_results = data['totalResults']
            jobs = data['results']
            total_jobs.extend(jobs)
            print(total_jobs)

            results_fetched += len(jobs)
            if results_fetched >= total_results:
                break

            args['resultsToSkip'] = results_fetched

        total_jobs.sort(key=lambda x: datetime.datetime.strptime(x['date'], "%d/%m/%Y"), reverse=True)
        return total_jobs
    
    def job_details(self, job_id: int) -> dict:
        '''
        Retrieve details of the job with given id.
        '''

        if not type(job_id) is int:
            raise ValueError("'job_id' must be type 'int'")

        url = JOB_DETAILS_ROOT + str(job_id)
        return self.process_job_details_request(url)

    def process_job_details_request(self, url: str) -> dict:
        '''
        Process a job details request using requests library.
        '''
        auth = HTTPBasicAuth(username=self.api_key, password='')
        r = requests.get(url, auth=auth)

        if not r:
            r.raise_for_status()

        return r.json()