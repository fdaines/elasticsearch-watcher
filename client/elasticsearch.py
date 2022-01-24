import json
import requests

from config import get_elasticsearch_url, get_elasticsearch_apikey

def get_plain_response(endpoint):
    response = requests.request('GET', get_elasticsearch_url() + endpoint, headers={'apikey': get_elasticsearch_apikey()})
    return response.text

def get_json_response(endpoint):
    response = requests.request('GET', get_elasticsearch_url() + endpoint, headers={'apikey': get_elasticsearch_apikey()})
    return json.loads(response.text)
