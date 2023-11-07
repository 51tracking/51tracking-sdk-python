import tracking51

tracking51.api_key = 'you api key'

def get_all_couriers():
    try:
        result = tracking51.courier.get_all_couriers()
        return result
    except tracking51.exception.Tracking51Exception as ce:
        print(ce)
    except Exception as e:
        print("other error:", e)

if __name__ == '__main__':
    result = get_all_couriers()
    print(result)
