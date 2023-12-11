import json
import os
from urllib.request import Request, urlopen

AWS_SESSION_TOKEN = os.environ.get('AWS_SESSION_TOKEN')
PARAMETER_STORE_URL = 'http://localhost:2773/systemsmanager/parameters/get?name={parameter_name}&withDecryption=true'
# comment addded to verify Codpipeline functionality


def get_parameter_name(event):
    return event['Name'].replace('/', '%2F')


def make_parameter_store_request(parameter_name):
    url = PARAMETER_STORE_URL.format(parameter_name=parameter_name)
    req = Request(url)
    req.add_header('X-Aws-Parameters-Secrets-Token', AWS_SESSION_TOKEN)
    return urlopen(req)


def get_parameter_value(event):
    name = get_parameter_name(event)
    response = make_parameter_store_request(name)
    return json.loads(response.read())['Parameter']['Value']


def handle_errors(action):
    try:
        return action()
    except Exception as e:
        print(f'Error: {e}')
        raise


def lambda_handler(event, context):
    key = handle_errors(lambda: get_parameter_value(event))
    return key
