#!/usr/bin/env python3
""" File storage module """
import json
from models.base_model import BaseModel


class FileStorage:
    """The Storage class"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        :param obj:
        :return:
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def reload(self):
        """
        Deserializes the JSON objects in JSON file (path: __file_path)
        """
        try:
            data = {}
            with open(self.__file_path, 'r') as f:
                data = json.load(f)

            for key, value in data.items():
                model = BaseModel(**value)
                self.__objects[key] = model
        except Exception as e:
            pass

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(data, f, indent=4)
