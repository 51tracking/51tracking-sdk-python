
from .request import make_request

__all__ = ['get_all_couriers']

api_modul = 'couriers'

def get_all_couriers():
    path = api_modul + '/all'
    response = make_request('GET', path, None)
    return response
