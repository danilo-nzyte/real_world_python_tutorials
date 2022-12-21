import requests
import json

def get_character_results():
    data = {"data": {"endpoint": "character", "api_params": {}}}
    headers = {"Content-Type": "application/json"}
    results = requests.post("<INSERT FUNCTION URL>", data=json.dumps(data), headers=headers)
    return results.json()

def load_bq_data(results):
    data = {"data": {"dataset": "rick_and_morty", "table": "character", "results": results}}
    headers = {"Content-Type": "application/json"}
    results = requests.post("<INSERT FUNCTION URL>", data=json.dumps(data), headers=headers)
    return "DONE"

if __name__ == "__main__":
    results = get_character_results()
    load_bq_data(results)