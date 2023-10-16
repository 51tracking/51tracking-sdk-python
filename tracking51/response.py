import json

from .exception import Tracking51Exception

def process_response(response):
    try:
        json_content = response.json()
    except json.JSONDecodeError:
        raise Tracking51Exception('response json type conversion failed')
    return json_content