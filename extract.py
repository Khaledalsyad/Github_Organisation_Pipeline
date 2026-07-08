from config import GETHUB_ORG, GITHUB_TOKEN, PER_PAGE, REQUEST_TIMEOUT
import requests
from typing import Generator
from decorators.retry import retry
from decorators.timer import timer_decorator
from decorators.logger import logger_decorator


headers = {
    'Authorization': f'Bearer {GITHUB_TOKEN}'
}


@logger_decorator
@timer_decorator
@retry(retries=3)
def extract_data() -> Generator:
    """
    Extract data from GitHub API
    """
    
    for orgnization in GETHUB_ORG:
        page = 1
        while True:
            url = f"https://api.github.com/orgs/{orgnization}/repos"
            parmas = {
                'page' : page,
                'per_page' : PER_PAGE
            }

            response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT, params = parmas)

            if response.status_code !=200:
                print(f'Erorre {response.status_code}')
                break
            data = response.json() 

            if not data:
                break

            yield orgnization, data

            page += 1
