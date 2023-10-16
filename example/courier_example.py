import tracking51

tracking51.api_key = 'you api key'

def get_all_couriers():
    try:
        result = tracking51.courier.get_all_couriers()
        return result
    except tracking51.exception.Tracking51Exception as ce:
        print(ce)

def detect(params):
    try:
        result = tracking51.courier.detect(params)
        return result
    except tracking51.exception.Tracking51Exception as ce:
        print(ce)

if __name__ == '__main__':
    result = get_all_couriers()
    print(result)

    params = {'tracking_number': '92612903029511573030094547'}
    result = detect(params)
    print(result)