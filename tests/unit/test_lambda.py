import json
import unittest

from ParameterStoreGetValue import app
class TestGetParameterNameCase(unittest.TestCase):
    def test_get_parameter_name(self):
        print("testing get_parameter_name")
        event = {"Name": "/sam/vpcProd"}
        name = app.get_parameter_name(event)
        print(name)
        self.assertEqual(name, "%2Fsam%2FvpcProd")

if __name__ == '__main__':
    unittest.main()
