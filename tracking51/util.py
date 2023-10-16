import tracking51

from .exception import Tracking51Exception

from .const import ErrEmptyAPIKey

def get_api_key():
    '''Get 51Tracking API key'''
    if tracking51.api_key is not None and tracking51.api_key != '':
        return tracking51.api_key
    else:
        raise Tracking51Exception(ErrEmptyAPIKey)

def build_query(params):
    kv_pairs = [f'{key}={value}' for key, value in params.items()]

    result = '&'.join(kv_pairs)

    return result

def is_empty(value):
    if value is None:
        return True
    if isinstance(value, (str, list, tuple, dict)):
        return not bool(value)
    return False