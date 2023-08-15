#!/usr/bin/env python3
""" Base model module """

from models.engine.file_storage import FileStorage as Storage
from models.base_model import BaseModel
from models.user import User

storage = Storage()
storage.reload()
