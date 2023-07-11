#!/usr/bin/python3
"""
A class Student.
"""


class Student:
    """A class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            v_dict = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    v_dict[k] = v
            return v_dict

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
