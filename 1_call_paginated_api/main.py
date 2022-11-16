from typing import List

from ramapi import get_endpoint
from models import ApiParameters, CharacterSchema


ENDPOINT = "character"


def get_all_paginated_results(
    endpoint: str, pages: int, params: ApiParameters
) -> List[CharacterSchema]:
    results = []
    for page in range(1, pages + 1):
        params.page = page
        print(f"Calling page {page}")
        response = get_endpoint(endpoint, params)
        results.extend(response.results)
    return results


if __name__ == "__main__":
    params = ApiParameters()
    response = get_endpoint(ENDPOINT, params)
    results = get_all_paginated_results(ENDPOINT, response.info.pages, params)
    print(f"Total records: {len(results)}")
