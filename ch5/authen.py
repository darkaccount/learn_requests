# _*_ coding: utf-8 _*_
import requests

BASE_URL = 'https://api.github.com'


def construct_url(end_point):
    return '/'.join([BASE_URL, end_point])


def basic_auth():
    '''
    基本认证
    '''
    response = requests.get(construct_url('user'), auth=('imoocdemo', 'imoocdemo123'))
    print ('>>>Text:')
    print (response.text)
    print ('>>>Headers:')
    print (response.request.headers)


basic_auth()