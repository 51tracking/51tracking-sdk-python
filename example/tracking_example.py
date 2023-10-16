import tracking51

tracking51.api_key = 'you api key'

def create_tracking(params):
    try:
        result = tracking51.tracking.create_tracking(params)
        return result
    except tracking51.exception.Tracking51Exception as ce:
        print(ce)

def get_tracking_results(params):
    try:
        result = tracking51.tracking.get_tracking_results(params)
        return result
    except tracking51.exception.Tracking51Exception as ce:
        print(ce)

def batch_create_trackings(params):
    try:
        result = tracking51.tracking.batch_create_trackings(params)
        return result
    except tracking51.exception.Tracking51Exception as ce:
        print(ce)

def update_tracking_by_id(id_string, params):
    try:
        result = tracking51.tracking.update_tracking_by_id(id_string, params)
        return result
    except tracking51.exception.Tracking51Exception as ce:
        print(ce)

def delete_tracking_by_id(id_string):
    try:
        result = tracking51.tracking.delete_tracking_by_id(id_string)
        return result
    except tracking51.exception.Tracking51Exception as ce:
        print(ce)

def retrack_tracking_by_id(id_string):
    try:
        result = tracking51.tracking.retrack_tracking_by_id(id_string)
        return result
    except tracking51.exception.Tracking51Exception as ce:
        print(ce)

if __name__ == '__main__':
    params = {'tracking_number': '92612903029511573030094547','courier_code':'usps'}
    result = create_tracking(params)
    print(result)

    # params = {'tracking_numbers': '92612903029511573030094547', 'courier_code': 'usps'}
    # params = {'tracking_numbers': '92612903029511573030094547,92612903029511573030094548', 'courier_code': 'usps'}
    params = {'created_date_min': '2023-10-09T06:00:00+00:00', 'created_date_max': '2023-10-10T13:45:00+00:00'}
    result = get_tracking_results(params)
    print(result)

    params = [{'tracking_number': '92612903029511573030094593', 'courier_code': 'usps'},
              {'tracking_number': '92612903029511573030094594', 'courier_code': 'usps'}]
    result = batch_create_trackings(params)
    print(result)

    params = {'customer_name': 'New name', 'note': 'New tests order note'}
    id_string = "9a2f732e29b5ed2071d4cf6b5f4a3d19"
    result = update_tracking_by_id(id_string, params)
    print(result)

    id_string = "9a2f7d1e8b912b729388c5835c188c28"
    result = delete_tracking_by_id(id_string)
    print(result)

    id_string = "9a2f732e29b5ed2071d4cf6b5f4a3d19"
    result = retrack_tracking_by_id(id_string)
    print(result)