# _*_ coding: utf-8 _*_
import requests


def download_image():
    '''
    demo:下载图片
    '''
    url = 'https://www.baidu.com/img/bd_logo1.png'
    response = requests.get(url, stream=True)
    with open('img.jpg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)


def download_image_improved():
    '''
    demo:下载图片
    '''
    url = 'https://www.baidu.com/img/bd_logo1.png'
    response = requests.get(url, stream=True)
    from contextlib import closing
    with closing(requests.get(url, stream=True)) as response:
        with open('img1.jpg', 'wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)

 
download_image_improved()