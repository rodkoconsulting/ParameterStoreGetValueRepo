import json
import unittest
import boto3

class TestHandlerCase(unittest.TestCase):
    def test_response(self):
        print("testing response from lambda function")
        event = {"Name": "/sam/vpcProd"}
        lambda_client = boto3.client('lambda')
        lambda_response = lambda_client.invoke(FunctionName="ParameterStoreGetValueFunction_DEV",
                                               InvocationType='RequestResponse', Payload=json.dumps(event))
        result = json.load(lambda_response['Payload'])
        print(result)
        self.assertEqual(result['body'], "vpc-0d6712c4bd670aca6")


if __name__ == '__main__':
    unittest.main()
