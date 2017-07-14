# _*_ coding: utf-8 _*_
import json
import requests

URL = 'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([URL, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_method():
    response = requests.get(build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'))
    print (better_print(response.text))


def params_request():
    params = {'since': 11}
    response = requests.get(build_uri('users'), params=params)
    print (better_print(response.text))
    print (response.request.headers)
    print (response.url)
   

if __name__ == '__main__':
#    request_method()
    params_request()