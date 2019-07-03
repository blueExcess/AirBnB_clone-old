#!/usr/bin/python3
from model.base_models import BaseModel


class Review(BaseModel):
    """ Review class for user reviews """

    place_id = ''
    user_id = ''
    text = ''
