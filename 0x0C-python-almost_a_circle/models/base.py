#!/usr/bin/python3
"""
A class base.
"""
import json
import csv


class Base:
    """A new base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs
        to a file
        """
        file_name = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dicts)

        with open(file_name, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string
        representation json_string
        """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                data = file.read()
                objects = cls.from_json_string(data)
                instances = []
                for obj in objects:
                    instances.append(cls.create(**obj))
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""

        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height,
                                    obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV"""

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                instances = []
                if cls.__name__ == "Rectangle":
                    for row in reader:
                        instances.append(cls.create(
                            id=int(row[0]), width=int(row[1]),
                            height=int(row[2]), x=int(row[3]),
                            y=int(row[4])
                        ))
                elif cls.__name__ == "Square":
                    for row in reader:
                        instances.append(cls.create(
                            id=int(row[0]), size=int(row[1]),
                            x=int(row[2]), y=int(row[3])
                        ))
                return instances
        except FileNotFoundError:
            return []
