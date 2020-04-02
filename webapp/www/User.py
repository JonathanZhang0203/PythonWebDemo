# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:31:25 2020

@author: Administrator
"""


from orm import Model, StringField, IntegerField

class User(Model):
    __table__ = 'users'
    
    id = IntegerField(primary_key=True)
    name = StringField()
    
'''
user = User(id=1, name='admin')

user.insert()

users = User.findAll()

'''