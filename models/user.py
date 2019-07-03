#!/usr/bin/python3
""" class user """
from model.base_models import BaseModel


class User(BaseModel):
    """ Class user for application users: """
    email = ""
    password = ""
    first_name = ""
    last_name ""
