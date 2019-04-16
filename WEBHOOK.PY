#!/usr/bin/env python
# coding=utf-8

import os, time
from wsgiref.simple_server import make_server

__author__ = 'liu'
import logging
 
logging.basicConfig(level=logging.INFO,
                    filename='./log.out',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

def newPost(environ):
    if environ['REQUEST_METHOD'] == "POST":
        print(environ)
        logging.info('new post')
        os.system('git add .')
        os.system('git commit -m "merge"')
        os.system('git pull origin master')
        logging.info('git pull finish')
    

def update(environ):
    if environ['REQUEST_METHOD'] == "POST":
        logging.info('post update')
        os.system('git add .')
        os.system('git commit -m "%s"' % time.asctime(time.localtime(time.time())))
        os.system('git pull origin master')
        logging.info('git pull finish')

route_map = {
    '/new': newPost,
    '/update': update
}

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    environ['PATH_INFO'] = '/' + environ['PATH_INFO'].split('/')[-1]
    print(environ['PATH_INFO'])
    if environ['PATH_INFO'] in route_map: 
        route_map[environ['PATH_INFO']](environ)
    return [b'Hello, webhook!']

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()

