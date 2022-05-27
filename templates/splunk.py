import requests

endpoint = "https://splunk:8089"
auth = ('admin', 'secret123')

def get_splunk_index_list():
    url = f"{endpoint}/services/data/indexes?datatype=event"
    data = {'output_mode':'json'}
    response = requests.get(url, data=data, auth=auth, verify=False).json()
    return [index['name'] for index in response['entry']]

def get_splunk_index(app):
    index = f"{app}_index"
    if index in get_splunk_index_list():
        data = {
            'output_mode':'json'
        }
        response = requests.get(f"{endpoint}/services/data/indexes/{index}", data=data, auth=auth, verify=False).json()
    else:
        data = {
            'name': index,
            'datatype': 'event',
            'output_mode':'json'
        }
        response = requests.post(f"{endpoint}/services/data/indexes", data=data, auth=auth, verify=False).json()
    index = response['entry'][0]
    index.pop('acl', None)
    index.pop('author', None)
    index.pop('content', None)
    index.pop('fields', None)
    index.pop('links', None)
    return index

def get_splunk_input_http_list():
    url = f"{endpoint}/services/data/inputs/http"
    data = {'output_mode':'json'}
    response = requests.get(url, data=data, auth=auth, verify=False).json()
    print()
    return [index['name'] for index in response['entry']]


def get_splunk_input_http(app):
    if f"http://{app}" in get_splunk_input_http_list():
        url = f"{endpoint}/servicesNS/nobody/splunk_httpinput/data/inputs/http/http%3A%252F%252F{app}"
        data = {
            'output_mode':'json'
        }
        response = requests.get(url, data=data, auth=auth, verify=False).json()
    else:
        data = {
            'name': f'{app}',
            'index': f'{app}_index',
            'description': f'{app.capitalize()} Token',
            'index': f'{app}_index',
            'source': f'{app}_run_monitor',
            'output_mode':'json'
        }
        response = requests.post(f"{endpoint}/services/data/inputs/http", data=data, auth=auth, verify=False).json()
    input_http = response['entry'][0]
    input_http.pop('acl', None)
    input_http.pop('author', None)
    input_http['description'] = input_http['content']['description']
    input_http['token'] = splunk_token = input_http['content']['token']
    input_http.pop('content', None)
    input_http.pop('fields', None)
    input_http.pop('links', None)
    return input_http, splunk_token