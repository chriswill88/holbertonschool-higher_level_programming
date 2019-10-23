#!/usr/bin/python3
import json
"""
models/base is a modual that contains the Base class
"""


class Base:
    """
    Base class - creates base object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constrictor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
        listy = []
        extra = len("_Rectangle__")
        filename = cls.__name__ + ".json"
        for objects in list_objs:
            listy.append(objects.__dict__)
        dicty = json.loads(json.dumps(listy))
        for x in dicty:
            for i in x:
		if len(i) > extra:
			i = i[extra:]
                print("dicty --", i, x[i])

        with open(filename, 'w') as f:
            f.write(Base.to_json_string(listy))
