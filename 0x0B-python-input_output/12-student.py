#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dic = self.__dict__
        newdic = {}
        if attrs is None:
            return dic
        for i in dic:
            try:
                for x in attrs:
                    if i is x:
                        newdic[i] = dic[i]
            except Exception:
                pass
        return newdic
