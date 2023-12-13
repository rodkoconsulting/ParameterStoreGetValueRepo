import json
import unittest

from ParameterStoreGetValue import app
class TestHandlerCase(unittest.TestCase):
    def test_response(self):
        print("testing response")
        event = {"Name": "/sam/vpcProd"}
        result = app.lambda_handler(event, None)
        print(result)
        self.assertEqual(result['body'], "vpc-0d6712c4bd670aca6")

if __name__ == '__main__':
    unittest.main()
