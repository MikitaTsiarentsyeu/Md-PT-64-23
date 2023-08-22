import unittest
from unittest.mock import MagicMock

def get_data_from_api(api):
    response = api.get('/data')
    if response:
        data = response.json()
        return data
    
class ApiTest(unittest.TestCase):

    def test_get_data_from_api(self):
        mock_api = MagicMock()

        resp = {
            'status': 200,
            'data': ['item 1', 'item 2']
        }

        mock_api.get.return_value.json.return_value = resp['data']

        result = get_data_from_api(mock_api)

        self.assertEqual(result, resp['data'])
        # mock_api.get.assert_called_once_with("/data")

if __name__ == "__main__":
    unittest.main()
