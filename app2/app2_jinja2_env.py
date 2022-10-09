# coding: utf8
""" 
@File: app2_jinja2_env.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/27 1:30
"""

from jinja2 import Environment
from django.template.defaultfilters import date


def app2_jinja2_environment(**options):
    env = Environment(**options)
    env.globals.update({
        'date': date
    })
    
    return env

