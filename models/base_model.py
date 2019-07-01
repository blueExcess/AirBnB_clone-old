#!/usr/bin/python3
"""Contains base class for all models for AirBnB project."""

import uuid



class BaseModel():
    """Base class for all model classes."""
    id = str(uuid.uuid(4))
    
