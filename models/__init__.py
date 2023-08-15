#!/usr/bin/env python3
""" Base model module """

from models.engine.file_storage import FileStorage as Storage

storage = Storage()
storage.reload()
