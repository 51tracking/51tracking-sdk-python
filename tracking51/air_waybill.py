from .const import ErrInvalidAirWaybillFormat, ErrMissingAwbNumber

from .exception import Tracking51Exception

from .request import make_request

from .util import is_empty

__all__ = ['create_an_air_waybill']

def create_an_air_waybill(params):
    if is_empty(params.get('awb_number')):
        raise Tracking51Exception(ErrMissingAwbNumber)
    if len(params['awb_number']) != 12:
        raise Tracking51Exception(ErrInvalidAirWaybillFormat)
    path = '/awb'
    response = make_request('POST', path, params)
    return response