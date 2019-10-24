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
        """
        Takes a list of dictionaries and returns
        JSON string representation
        """
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves string representation of onjects and saves
        them in a file
        """
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
                # print(x)
                # if '_Rectangle__id' == i:
                #    continue
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

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string: returns list of dictionaries
        """
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create: creates an instance of a class
        updates class, and returns that instance
        """
        # print(cls)
        # print(dictionary)
        name = cls.__name__
        # print("create on ->", name)
        # print("name -> ", name)
        if name == "Square":
            a = cls(size=1)
            # print("-->", cls.id)
            a.update(**dictionary)
        if name == "Rectangle":
            a = cls(width=1, height=1)
            a.update(**dictionary)
        return a

    @classmethod
    def load_from_file(cls):
        """
        loads from file and creates instances
        """
        listOfInst = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as f:
                    # print("the listy", i)
                l = Base.from_json_string(f.read())
        except FileNotFoundError:
            return listOfInst
        # print("from fjs -> ", l)
        for x in l:
            # print("x is", x)
            listOfInst.append(cls.create(**x))
        return listOfInst
