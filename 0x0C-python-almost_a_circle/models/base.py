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
        new_list = []
        newdict = {}
        extra = len("_Rectangle__")
        filename = cls.__name__ + ".json"
        for objects in list_objs:
            listy.append(objects.__dict__)
            dicty = json.loads(json.dumps(listy))
        for x in dicty:
            # print("1 list", x)
            for i in x:
                if '_Rectangle__id' == i:
                    continue
                if len(i) > extra:
                    name = i[extra:]
                else:
                    name = i
                newdict[name] = x[i]
                # print("dicty --", name, x[i])
            new_list.append(dict(newdict))
        # print("the new dict -->", newdict)
        # print(new_list)
        with open(filename, 'w') as f:
            f.write(Base.to_json_string(new_list))
