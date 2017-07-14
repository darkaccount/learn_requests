# _*_ coding: utf-8 _*_
import json
import requests
from requests import exceptions

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


def json_request():
    json = {'name': 'fathermooc2', 'eamil': 'helloaa@imooc.org'}
    response = requests.patch(build_uri('user'), auth=('imoocdemo', 'imoocdemo123'), json=json)
    print (better_print(response.text))
    print (response.request.headers)
    print (response.request.body.decode('utf-8'))
    print (response.status_code)


def timeout_request():
    try:
        response = requests.get(build_uri('user/emails'), timeout=0.6)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print ('>>>>TimeoutError:')
        print (e)
    except exceptions.HTTPError as e:
        print ('>>>>HTTPError:')
        print (e)
    else:
        print ('>>>>Normal:')
        print (response.text)
        print (response.status_code)


def hard_requests():
    from requests import Request, Session
    s = Session()
    headers = {'User-Agent': 'fake1.3.4'}
    req = Request('Get', build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'), headers=headers)
    prepped = req.prepare()
    print (prepped.body)
    print (prepped.headers)

    resp = s.send(prepped, timeout=5)
    print (resp.status_code)
    print (resp.request.headers)
    print (resp.text)


if __name__ == '__main__':
#    request_method()
#    params_request()
#    json_request()
#    timeout_request()
    hard_requests()