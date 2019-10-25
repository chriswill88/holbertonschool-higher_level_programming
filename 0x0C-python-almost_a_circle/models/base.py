#!/usr/bin/python3
"""A modual that contains the class.
Our other created classes will be inheriting from.
"""
import json


class Base:
    """ Creates base object.
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
        # print("ld = ", list_dictionaries)
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves string representation of onjects and saves
        them in a file
        """
        # print("listbjs = ", list_objs)
        name = ""
        listy = []
        new_list = []
        newdict = {}
        dicty = {}
        extra = len("_Rectangle__")
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for objects in list_objs:
                listy.append(objects.__dict__)
                dicty = json.loads(json.dumps(listy))
            for x in dicty:
                # print("1 list", x)
                for i in x:
                    if cls.__name__ == "Square":
                        print(i)
                        if extra < len(i) and i[extra:] == "width":
                            name = "size"
                        elif extra < len(i) and i[extra:] == "height":
                            continue
                        elif len(i) > extra:
                            name = i[extra]
                        else:
                            name = i
                    else:
                        # print(x)
                        # if '_Rectangle__id' == i:
                        #    continue
                        if len(i) > extra:
                            name = i[extra:]
                        else:
                            name = i
                    newdict[name] = x[i]
                # print("newdict->", newdict)
                # print("dicty --", name, x[i])
                new_list.append(dict(newdict))
        # print("the new dict -->", newdict)
        # print(new_list)
        else:
            new_list = []
        with open(filename, 'w') as f:
            f.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string: returns list of dictionaries
        """
        if json_string is None:
            return []
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
