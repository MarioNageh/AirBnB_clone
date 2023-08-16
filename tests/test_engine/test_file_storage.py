#!/usr/bin/python3
"""
Test cases for FileStorage class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import os


class TestFileStorage(unittest.TestCase):
    """
    test class
    """
    fs = FileStorage()

    def test_default_values(self):
        """test default value"""

        initial_count = len(self.fs.all())
        new_base_model = BaseModel()
        self.fs.new(new_base_model)

        self.fs.save()
        self.fs.reload()

        updated_count = len(self.fs.all())
        self.assertEqual(updated_count, initial_count + 1)
        obj_key = f"BaseModel.{new_base_model.id}"
        self.assertIn(obj_key, self.fs.all())
        reloaded_obj = self.fs.all()[obj_key]
        self.assertEqual(reloaded_obj.updated_at, new_base_model.updated_at)

        os.remove("file.json")
        new_base_model = BaseModel()
        new_base_model.save()
        self.assertTrue(os.path.exists("file.json"))
