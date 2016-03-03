# -*- coding: utf-8 -*-
# from coroweb import get
import orm
import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from Model import User, Comment, Blog, next_id

# @get('/')
# def index(request):
    # users = yield from User.findAll()
    # return {
		# '__template__': 'test.html',
		# 'users': users
	# }
    
# import logging; logging.basicConfig(level=logging.INFO)

# import asyncio,os,json,time
# from datetime import datetime
# from aiohttp import web
# import orm
# import Model
# from config import configs
# from coroweb import add_routes, add_static,add_route,get
# from jinja2 import Environment, FileSystemLoader
# from Model import User, Comment, Blog, next_id

# @get('/')
# def index(request):
    # users = yield from User.findAll()
    ##users = yield from User.find('001456476568298a475c0dd329d473f959d181bd616542a000')
    # logging.info(users)
    # return web.Response(body=b'<h1>Awesome</h1>')
@get('/')
def index(request):
    users = yield from User.findAll()
    return {
		'__template__': 'test.html',
		'users': users
	}
    
