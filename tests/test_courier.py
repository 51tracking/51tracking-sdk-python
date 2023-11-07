
from tracking51 import courier

def test_get_all_couriers():
    response = courier.get_all_couriers()
    assert response['meta']['code'] == 200

