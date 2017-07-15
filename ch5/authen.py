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


def basic_oauth():
    headers = {'Authorization': 'token 177da5836a8409032569c4b6052cb4b5d2c18e80'}
    # user/emails
    response = requests.get(construct_url('user/emails'), headers=headers)
    print ('>>>Headers:')
    print (response.request.headers)
    print ('>>>Text:')
    print (response.text)
    print ('>>>>Status_code:')
    print (response.status_code)
   

from requests.auth import AuthBase


class GithubAuth(AuthBase):

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        #requests + headers
        r.headers['Authorization'] = ' '.join(['token', self.token])
        return r
    

def oauth_advanced():
    auth = GithubAuth('177da5836a8409032569c4b6052cb4b5d2c18e80')
    response = requests.get(construct_url('user/emails'), auth=auth)
    print ('>>>Text:')
    print (response.text)
 
oauth_advanced()