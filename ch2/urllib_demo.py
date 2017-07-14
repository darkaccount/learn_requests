# _*_ coding: utf-8 _*_
import urllib.request

URL_GET = 'http://httpbin.org/get'
URL_IP = 'http://httpbin.org/ip'

def use_simple_urllib2():
    response = urllib.request.urlopen(URL_IP)
    print ('>>>>Response Headers:')
    print (response.info())
    print ('>>>>Response Body:')
    print (response.read().decode('utf-8'))


def use_params_urllib2():
    #构建请求参数
    params = {'param1': 'hello', 
              'param2': 'world'}
    params = urllib.parse.urlencode(params)
    print ('Request Params:')
    print (params)
    #发送请求
    response = urllib.request.urlopen('?'.join([URL_GET, '%s']) % params)
    #处理响应
    print ('>>>>Response Headers:')
    print (response.info())
    print ('>>>>Status Code:')
    print (response.getcode())
    print ('>>>>Response Body:')
    print (response.read().decode('utf-8'))




if __name__ == '__main__':
    print ('>>>Use simple urllib2:')
    use_simple_urllib2()
    print ('>>>Use params urllib2:')
    use_params_urllib2()
